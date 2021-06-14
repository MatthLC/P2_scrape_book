import requests
from bs4 import BeautifulSoup
import csv



db = {	 "product_page_url":"product_page_url"
		,"universal_product_code":"UPC"
		,"title":"title"
		,"price_including_tax":"Price (incl. tax)"
		,"price_excluding_tax":"Price (excl. tax)"
		,"number_available":"Availability"
		,"product_description":""
		,"category":""
		,"review_rating":"Number of reviews"
		,"image_url":"image_url"
		}

# "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def init_soup(p_url):
	global soup

	url = p_url
	check_url = requests.get(url)

	if check_url.ok:
		soup = BeautifulSoup(check_url.text, 'html.parser')

		book()

def book():	
	#URL
	db["product_page_url"] = url

	#titre
	title = soup.find('div', {'class':'col-sm-6 product_main'}).find('h1')
	db["title"] = title.text

	#product description
	product_page = soup.find('article', {'class':'product_page'})
	db['product_description'] = product_page.findAll('p')[3].text

	#product information
	product_info_trs = soup.findAll('tr')

	trs_name = []
	for trs in product_info_trs:
		trs_name.append(trs.find('th').text)

	tds_name = []
	for tds in product_info_trs:
		tds_name.append(tds.find('td').text)	

	product_info = dict(zip(trs_name,tds_name))

	for db_cle, db_name in db.items():
		for info_cle, info_info in product_info.items():
			if db_name == info_cle:
				db[db_cle] = info_info

	#image url
	img_url = soup.find('div',{'class':'item active'}).find('img')

	db['image_url'] = 'http://books.toscrape.com/' + img_url['src'][6:]
	
	#category
	category = soup.find('ul',{'class':'breadcrumb'}).text
	lst_category = category.split()
	db['category'] = lst_category[2]
		
		
def output_csv(p_name):
	with open(p_name + '.csv', 'a', encoding="utf-8") as create_csv:
		writer = csv.DictWriter(create_csv,db.keys())
		# A faire : Warning plusieurs headers
		writer.writeheader()
		writer.writerow(db)


if __name__ == "__main__":

	url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
	init_soup(url)
	
	output_csv("livre")
		
	print("fonctionne")