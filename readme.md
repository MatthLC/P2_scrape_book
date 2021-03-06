# **Scrape Book v1.0.0**

Outils d'analyse de données de livres en ligne présents sur le site : http://books.toscrape.com/

Ce projet stock les principales informations des livres au format CSV ainsi que les images des couvertures de livre.
 
## **Prérequis**

Ce projet est développé avec la version de Python 3.9, il est par conséquent recommandé d'installer cette version avant de continuer.


## **Initialisation de l'environnement**

### 1. Cloner la branche Main vers un répertoire local

- Créer un dossier sur votre ordianteur pour y disposer les fichiers présents sous GitHub

- Ouvrir un terminal (Ex: Windows PowerShell) et se positionner dans le dossier en question avec la commande cd, par exemple:

```
cd d:
cd -- "D:\mon_dossier"
```

### 2. Créer un environnement virtuel et installer les librairies à l'aide du fichier requirements.txt

- Créer l'environnement:


`python -m venv venv`

- Activer l'nvironnement (L'environnement est activé une fois son nom affiché dans le terminal) : 

    - Windows:

    `venv/Scripts/Activate.ps1` 

    - Inux et MacOS:  

    `source venv/bin/activate`

- Installer les librairies : 

`pip install -r requirements.txt`


## **Lancement du projet**

### 1. Lancer le programme main.py sous l'environnement virtuel, dans le terminal:

`py main.py`

### 2. Patienter jusqu'à l'affichage de toutes les catégories (Entre 30 secondes et 1 minute)
### 3. Saisir le/les numéros des catégories concernées séparés par un espace :

Exemple pour extraire 3 catégories:

`2 10 23`

Extraction de toutes les catégories :

`0`

Quitter l'application:

`999`

### 4. Patienter jusqu'à la fin du traitement (:warning: Ne pas ouvrir les fichiers CSV pendant le scraping :warning:)

## **Enregistrement des fichiers :**

les données sont stockées au format CSV sous la struture suivante :

```
 product_page_url
 universal_ product_code
 title
 price_including_tax
 price_excluding_tax
 number_available
 product_description
 category
 review_rating
 image_url
```

Les résultats seront disponibles dans le dossier "output" créé par l'application à la racine du projet.

Il existe un dossier par catégorie, ce dossier contient le fichier CSV correspondant ainsi que les images des couvertures de livre.

Bon à savoir : le précédent dossier de la catégorie lancée sera supprimé, veillez à copier dans un autre dossier les résultats que vous voulez concerver.(Si je lance deux fois la catégorie "Fiction", le dossier créé au premier lancement sera supprimé et recréé pour le nouveau lancement)

