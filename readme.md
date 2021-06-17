### Scrape Book

Outils d'analyse de données de livre en ligne présent sur le site : http://books.toscrape.com/

- **Enregistrement des fichiers :**

les données sont stockées au format CSV sous la struture suivante :
	- product_page_url
	- universal_ product_code (upc)
	- title
	- price_including_tax
	- price_excluding_tax
	- number_available
	- product_description
	- category
	- review_rating
	- image_url

Il existe un fichier CSV par catégorie.
Les fichiers seront stockés dans le répertoire "/output" à la racine du programme "main.py".
