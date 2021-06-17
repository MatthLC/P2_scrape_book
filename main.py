import requests
from bs4 import BeautifulSoup
import csv
import os

list_book_from_category = {}
category_name_link = {}

list_category = []
category_link = []

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

# Create directory for output:
def create_dir(p_name):
	try:
		os.mkdir('./' + p_name)
	except FileExistsError:
		pass

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
	#URL
	db['product_page_url'] = p_url

	#title
	db['title']=find_add_to_db('div', 'class', 'col-sm-6 product_main', 'h1').text

	#product description
	db['product_description'] = find_add_to_db('article', 'class', 'product_page', '').findAll('p')[3].text
	product_info = dict(zip(build_list('th'),build_list('td')))

	for db_cle, db_name in db.items():
		for info_cle, info_info in product_info.items():
			if db_name == info_cle:
				db[db_cle] = info_info

	#image url
	db['image_url'] = 'http://books.toscrape.com/' + find_add_to_db('div', 'class', 'item active', 'img')['src'][6:]

	#category
	db['category'] = find_add_to_db('ul','class','breadcrumb','').text.split()[2]
		
# Save as CSV
def output_csv(p_name):
	with open('./output/' + p_name + '.csv', 'a', encoding='utf-8') as create_csv:
		writer = csv.DictWriter(create_csv,db.keys())
		#TODO: Multiple headers
		writer.writeheader()
		writer.writerow(db)

# List all categories from the website
def f_list_category():
		titre_li = soup.find('ul',{'class':'nav nav-list'})

		for link in titre_li.findAll('a'):
			list_category.append(link.get_text().replace('\n','').strip())
		
		for li in titre_li.findAll('li'):
			category_link.append('http://books.toscrape.com/' + li.find('a')['href'])
		
		for i in range(1,len(list_category)):
			for j in range(1,len(category_link)):
				if i == j:
					category_name_link[list_category[i]] = category_link[i]
		return category_name_link

# List all page from categories
def f_all_page():
		list_book_from_category[cle] = []
	
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
def f_all_book():
	soup = init_soup(page)

	if soup:
		li_all = soup.findAll('li',{'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

		for li in li_all:
			list_book_from_category[cle].append('http://books.toscrape.com/catalogue/' + li.find('a')['href'][9:])
	
	return list_book_from_category



# ======= Lancement =======
if __name__ == '__main__':

	create_dir('output')
	
	#list category
	soup = init_soup('https://books.toscrape.com/')
	if soup:

		category_name_link = f_list_category()

	# Extraction des liens pour chaque catégories
	#	Pour chaque page
	#		Pour chaque livre
	
	for cle, category in category_name_link.items():

		page_all = f_all_page()
		
		# book's link for all page
		for page in page_all:

			list_book_from_category = f_all_book()
	
	for cle_category, page_book in list_book_from_category.items():
		for web_book in page_book:
			
			soup = init_soup(web_book)

			if soup:
								
				book(web_book)
				
				output_csv(cle_category)
	
				