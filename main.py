import requests
from bs4 import BeautifulSoup
import csv
import os
import shutil
import copy
import sys
import pdb; 

list_book_from_category = {}
category_name_link = {}
list_category = []
category_link = []
db_for_csv = {}

main_url = 'http://books.toscrape.com/'

db = {	 'product_page_url':'product_page_url'
		,'universal_product_code':'UPC'
		,'title':'title'
		,'price_including_tax':'Price (incl. tax)'
		,'price_excluding_tax':'Price (excl. tax)'
		,'number_available':'Availability'
		,'product_description':''
		,'category':''
		,'review_rating':'Number of reviews'
		,'image_url':'image_url'
		}

def create_output_directory(p_name):
	try:
		os.mkdir('./' + p_name)
	except FileExistsError:
		pass
	except Exception:
		sys.exit("Un problème est survenue, veuillez contacter l'administrateur")

def delete_csv(p_file):
	try:
		shutil.rmtree('./output/' + p_file)
	except OSError:
		pass

def replace_special_characters(p_string, p_type):
	if p_type == '/':
		result = p_string.replace('\n','/').replace('///','/').replace('//','/')
	if p_type == 'img':
		result = p_string.replace('/',' ').replace(':', ' ').replace('?',' ').replace("\\",' ').replace('"',' ').replace('*',' ').replace('|',' ').replace('?', ' ').replace('<', ' ').replace('>',' ')
	return result

# Set beautifullsoup for the next research
def init_soup(p_url):
	check_url = requests.get(p_url)

	if check_url.ok:
		soup = BeautifulSoup(check_url.text, 'html.parser')
		return soup

# Function for book : find specific argument in soup
def find_add_to_db(p_arg1, p_arg2, p_arg3, p_add_find):
	if p_add_find != '':
		f_var = soup.find(p_arg1, {p_arg2 : p_arg3}).find(p_add_find)
	else:
		f_var = soup.find(p_arg1, {p_arg2 : p_arg3})
	return f_var

# Function for book : product information data
def build_list(p_object):
	product_info_trs = soup.findAll('tr')
	f_list = []

	for obj in product_info_trs:
		f_list.append(obj.find(p_object).text)
	return f_list

# Function for book : specific data
def book(p_url):	
	tempory_db = copy.deepcopy(db)

	tempory_db['product_page_url'] = p_url
	tempory_db['title'] = find_add_to_db('div', 'class', 'col-sm-6 product_main', 'h1').text
	tempory_db['product_description'] = find_add_to_db('article', 'class', 'product_page', '').findAll('p')[3].text
	tempory_db['image_url'] = main_url + find_add_to_db('div', 'class', 'item active', 'img')['src'][6:]
	tempory_db['category'] = replace_special_characters(find_add_to_db('ul','class','breadcrumb','').text, '/').split('/')[3]

	product_info = dict(zip(build_list('th'),build_list('td')))
	for db_cle, db_name in tempory_db.items():
		for info_cle, info_info in product_info.items():
			if db_name == info_cle:
				if db_cle in ['price_including_tax','price_excluding_tax']:
					tempory_db[db_cle] = info_info[2:]
				else:
					tempory_db[db_cle] = info_info
	return tempory_db
		
# Save as CSV
def output_csv(p_name, p_db):
	csv_filename = './output/' + p_name + '/' + p_name + '.csv'
	with open(csv_filename, 'a', encoding='utf-8') as create_csv:
		writer = csv.DictWriter(create_csv, p_db.keys(), delimiter = ';')

		if count_book == 0:
			writer.writeheader()
		writer.writerow(p_db)

# List all categories from the website
def list_all_category(soup):
	titre_li = soup.find('ul',{'class':'nav nav-list'})

	for link in titre_li.findAll('a'):
		list_category.append(link.get_text().replace('\n','').strip())
	
	for li in titre_li.findAll('li'):
		category_link.append(main_url + li.find('a')['href'])
	
	for i in range(1,len(list_category)):
		for j in range(1,len(category_link)):
			if i == j:
				category_name_link[list_category[i]] = category_link[i]

# List all page from categories
def all_pages(category):
		soup = init_soup(category)
	
		if soup:
			page = soup.find('li',{'class':'current'})
			page_all = []
			page_all.append(category)
	
			if page:
				page_nb = page.text.strip().split()[-1]

				for i in range(2, int(page_nb) + 1):
					page_all.append(category.rsplit('/',1)[0] + '/page-' + str(i) + '.html')
			return page_all

# list all books on all pages
def all_books(cle, page):
	if page_number == 1:
		list_book_from_category[cle] = []

	soup = init_soup(page)
	if soup:
		li_all = soup.findAll('li',{'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

		for li in li_all:
			list_book_from_category[cle].append(main_url + 'catalogue/' + li.find('a')['href'][9:])
	
def save_image(p_url, p_path, p_name):
	response = requests.get(p_url, stream = True)
	if response.ok:
		img_filename = './' + p_path + '/' + p_name + '.jpg'
		with open(img_filename, 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response

def replace_characters_in_db():
	db_for_csv['title'] = replace_special_characters(db_for_csv['title'],'img')

# ======= Lancement =======
if __name__ == '__main__':
	print('Veuillez patienter...')
	create_output_directory('output')
	
	#list category
	soup = init_soup(main_url)
	if soup:
		list_all_category(soup)

	for cle, category in category_name_link.items():
		page_all = all_pages(category)
		page_number = 1

		# book's link for all page
		for page in page_all: 
			all_books(cle, page)
			page_number = page_number + 1
	
	# User choice
	# Show all categories
	print('Bienvenue ! Veuillez sélectionner une ou plusieurs catégories :')
	i = 1
	dict_for_user = {}

	print('0. Toutes les catégories')
	for key_name, value_link  in sorted(category_name_link.items()):
		print(str(i) + '. ' + key_name)
		dict_for_user[key_name] = i
		i = i + 1
	print('999. Quitter le programme\n')

	while True:
		user_choice = input('Saisissez les catégories : ').split()
		user_choice_list = {}

		if user_choice == ['0']:
			user_choice_list = list_book_from_category
		
		for choice in user_choice:
			for key_category, number in dict_for_user.items():
				if int(choice) == int(number):
					user_choice_list[key_category] = list_book_from_category[key_category]
			
			for cle_category, page_book in user_choice_list.items():
				count_book = 0
				delete_csv(cle_category)
				create_output_directory('output/' + cle_category)

				for web_book in page_book:
					soup = init_soup(web_book)

					if soup:			
						db_for_csv = book(web_book)
						replace_characters_in_db()
						save_image(db_for_csv['image_url'], 'output/' + cle_category, db_for_csv['title'])
						output_csv(cle_category, db_for_csv)
					count_book = count_book + 1
			
		if user_choice == ['999']:
			break
