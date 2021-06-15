import requests
from bs4 import BeautifulSoup
import csv
import os

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

def create_dir(p_name):
	# Create directory for output:
	try:
		os.mkdir('./' + p_name)
	except FileExistsError:
		pass

def init_soup(p_url):
	url = p_url
	check_url = requests.get(url)

	if check_url.ok:
		soup = BeautifulSoup(check_url.text, 'html.parser')
		return soup


def find_add_to_db(p_arg1, p_arg2, p_arg3, p_add_find):
	if p_add_find != '':
		f_var = soup.find(p_arg1, {p_arg2 : p_arg3}).find(p_add_find)
	else:
		f_var = soup.find(p_arg1, {p_arg2 : p_arg3})
	return f_var

def build_list(p_object):
	product_info_trs = soup.findAll('tr')
	
	f_list = []
	for obj in product_info_trs:
		f_list.append(obj.find(p_object).text)

	return f_list

def book():	
	#URL
	db['product_page_url'] = url

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
		
		
def output_csv(p_name):
	with open('./output/' + p_name + '.csv', 'a', encoding='utf-8') as create_csv:
		writer = csv.DictWriter(create_csv,db.keys())
		#TODO: Multiple headers
		writer.writeheader()
		writer.writerow(db)

if __name__ == '__main__':
	create_dir('output')

	url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
	
	soup = init_soup(url)

	if soup != None:
		book()
		output_csv('livre')