### Scrape Book v1.0.0

Outils d'analyse de données de livres en ligne présents sur le site : http://books.toscrape.com/

Ce projet stock les principales informations des livres au format CSV ainsi que les images des couvertures de livre.
 
- **Prérequis**
Ce projet est développé avec la version de Python 3.9, il est par conséquent recommandé d'installer cette version avant de continuer.


- **Initialisation de l'environnement**

1. Cloner la branche Main vers un répertoire local
    - créer un dossier pour y disposer les fichiers présents sous GitHub
    - Ouvrir un terminal et se positionner dans le dossier en question avec la commande cd, par exemple:
```
cd d:
cd -- "D:\mon_dossier"
```

2. Créer un environnement virtuel et installer les librairies à l'aide du fichier requirements.txt

- créer l'environnement:

```
python -m venv venv
```

- Activer l'nvironnement (L'environnement est activé une fois son nom affiché dans le terminal) : 

    - Windows:
```
    venv/Scripts/Activate.ps1 
```
    - Inux et MacOS:  
```
    source venv/bin/activate
```
    - installer les librairies : 
```
    pip install -r requirements.txt
```

- **Installation du projet**

1. Lancer le programme Main.py sous l'environnement virtuel, dans le terminal:
```
py main.py
```
2. Patienter jusqu'à l'affichage de toutes les catégories
3. Saisir le/les numéros des catégories concernées séparés par un espace :
4. Patienter jusqu'à la fin du traitement (Ne pas ouvrir les fichiers CSV pendant le scraping)


Extraction de toutes les catégories :
```
0
```
Quitter l'application:
```
999
```
Exemple :
```
2 10 23
```

- **Enregistrement des fichiers :**

les données sont stockées au format CSV sous la struture suivante :

```
 product_page_url
 universal_ product_code (upc)
 title
 price_including_tax
 price_excluding_tax
 number_available
 product_description
 category
 review_rating
 image_url
```

Les résultats seront disponibles dans le dossier "output" créé par l'application dans le dossier du projet.

Un Dossier est créé par catégorie, chaque dossier contient le fichier CSV correspondant et les images des couvertures de livre.

