*English version follows*

# Scraping "books.toscrape.com"

Programme "Scraper" qui récupère les informations de n'importe quel livre du site [Books to Scrape](http://books.toscrape.com).

## Descriptif

Le programme doit être capable d'extraire les informations suivantes :

* Product page url
* Universal product code
* Title
* Price including tax
* Price excluding tax
* Number available
* Product description
* Category
* Review rating
* Image url 

puis de les écrire dans un fichier CSV et l'enregistrer dans un dossier "Books\_To\_Scrape".

Il doit également télécharger les images de couverture des livres dans un sous-dossier "Images".

Le repository contient quatre scripts:  

* main.py 
* scrap\_book.py
* scrap\_category.py
* scrap\_all\_categories.py

### A) main.py

Le script *"main.py"* est le script principal qui va permettre à l'utilisateur d'accéder à un menu et d'effectuer un choix parmi les 4 options suivantes :

1. Récupérer les informations d'un livre en entrant son url et de les afficher dans le terminal.
2. Récupérer les informations et les images de tous les livres d'une seule catégorie en entrant son url et les stocker dans un fichier csv et un dossier images.
3. Récupérer les informations et les images de tous les livres du site et les stocker dans un fichier csv et un dossier images.
4. Quitter le programme.


##### B) scrap\_book.py

Le script *"scrap\_book.py"* contient les fonctions *scrap\_book* et *download\_image* qui comme leur nom l'indique vont permettre de scraper les informations d'un seul livre et de télécharger son image de couverture.

##### C) scrap\_category.py

Le script *"scrap\_category.py"* contient la fonction *scrap\_category* qui va permettre de scraper les informations et les images de tous les livres d'une catégorie.


##### D) scrap\_all\_categories.py

Le script *"scrap\_all\_categories.py"* contient la fonction *scrap\_all\_categories* qui va permettre de scraper les informations et les images de tous les livres de toutes les catégories du site.

## Prérequis
* Python 3.9 ( lien de téléchargement: <https://www.python.org/downloads>)

## Démarrage du programme

Après avoir téléchargé le dossier **Build_A_Web_Scraper_With_Python-main.zip** depuis ce lien [GitHub](https://github.com/SelHel/Build_A_Web_Scraper_With_Python.git).  
Extraire les fichiers dans un dossier de votre choix.  
Ensuite, en utilisant le terminal sur Mac et Linux ou l'invite de commandes sur Windows :

1. Placez vous dans le dossier courant
2. Créez un environnement virtuel
3. Activez votre environnement virtuel
4. Installez les modules nécessaires au bon fonctionnement du programme depuis le fichier requirements.txt

```
 /Users/../Build_A_Web_Scraper_With_Python-main
 python3 -m venv env
 source env/bin/activate 
 pip install -r requirements.txt

```
Puis lancez le script *"main.py"*

```
python main.py

```
Un menu va apparaître il ne vous restera plus qu'a choisir parmi les différentes options.

## Résultat

Après avoir exécuté une des commandes, un dossier "Books\_To\_Scrape" sera créé dans le dossier courant.  
Il se décomposera comme suit :

* Dossier : "Books\_To\_Scrape"
	* Sous-dossier : "Nom de la catégorie du livre"
  		* Sous-dossier : "Images" (uniquement si vous scrapé une catégorie ou toutes les catégories)
		* Fichier : "*Nom de la catégorie du livre*-data".csv

## Auteur

Selim Helaoui



----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------

                                 
# Scraping "books.toscrape.com"

"Scraper" program that retrieves information from any book on the website [Books to Scrape](http://books.toscrape.com).

## Description

The program must be able to extract the following information:

* Product page url
* Universal product code
* Title
* Price including tax
* Price excluding tax
* Number available
* Product description
* Category
* Review rating
* Image url 

Then write them to a CSV file and save it to a "Books\_To\_Scrape" directory and downloads the cover images of the books in a sub-directory "Images".

The repository contains four scripts:

* main.py 
* scrap\_book.py
* scrap\_category.py
* scrap\_all\_categories.py

### A) main.py

*"main.py"* is the main script allowing the user to access menu and choose from four options:

1. Scrape a single book and print the information in terminal.
2. Scrape a category and store the data in csv file and the images in subdirectory.
3. Scrape all books on the website and store the data in csv file and the images in subdirectory.
4. Exit the program.

##### B) scrap\_book.py

*"scrap\_book.py"* script contains the *scrap\_book* and *download\_image* functions. They scrape book's information and upload its cover image. 

##### C) scrap\_category.py

*"scrap\_category.py"* script contains the *scrap\_category* function. This function scrape information and images from all books in a category.


##### D) scrap\_all\_categories.py

*"scrap\_all\_categories.py"* script contains the *scrap\_all\_categories* function. This function scrape information and images from all books on the website.

## Requirements

* Python 3.9 ( download link: <https://www.python.org/downloads>)

## Starting the program

Download the directory **Build_A_Web_Scraper_With_Python-main.zip** from this link [GitHub](https://github.com/SelHel/Build_A_Web_Scraper_With_Python.git).	
Extract files in directory of your choice.
Then using the terminal on Mac and Linux or the command prompt on Windows:

1. In current directory
2. Create a virtual environment
3. Activate the virtual environment
4. Install the necessary modules from requirements.txt file.

```
 /Users/../Build_A_Web_Scraper_With_Python-main
 python3 -m venv env
 source env/bin/activate 
 pip install -r requirements.txt

```
Run the script *"main.py"*

```
python main.py

```
Menu will appear. Then you will choose from different options.

## Result

After executing a choice, "Books\_To\_Scrape" directory will be created in the current directory.  
It will be like that :

* Directory : "Books\_To\_Scrape"
	* Subdirectory : "Book's Category name"
  		* Subdirectory : "Images" (only if you scrape category or all categories)
		* File : "*Book's Category name*-data".csv


## Author

Selim Helaoui
