### Scrape Book

Outils d'analyse de données de livres en ligne présents sur le site : http://books.toscrape.com/
Ce projet stock les principales informations des livres au format CSV ainsi que les images des couvertures de livre.
 

- **Initialisation de l'environnement**

1. Cloner la branche Main vers un répertoire local
2. Creer un environnement virtuel et installer les librairies à l'aide du fichier requirements.txt

- **Installation du projet**

1. Lancer le programme Main sous votre environnement virtuel
2. Patienter j'usquà l'affichage de toutes les catégories
3. Saisir le/les numéros des catégories concernées séparés par un espace :
> 0 : Extraction de toutes les catégories
> 999 : Quitter l'application
> (Ex : 2 10 23)

- **Enregistrement des fichiers :**

les données sont stockées au format CSV sous la struture suivante :
> product_page_url
> universal_ product_code (upc)
> title
> price_including_tax
> price_excluding_tax
> number_available
> product_description
> category
> review_rating
> image_url

Les résultats seront disponibles dans le dossier "output" créé par l'application.
Un Dossier est créé par catégorie, chaque dossier contient le fichier CSV correspondant et les images des couvertures de livre.

