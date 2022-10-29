*French version*

# Web Scraping "books.toscrape.com"

## 1. Descriptif

Programme "Scraper" qui permet de collecter les données de n'importe quel livre du site [books.toscrape.com](http://books.toscrape.com).<br>

Le programme extrait les informations suivantes :

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

puis stock ces données dans un fichier CSV et l'enregistre dans un dossier "Books\_To\_Scrape".

Il doit également télécharger les images de couverture des livres dans un sous-dossier "Images".


## 2. Technologies


## 3. Prérequis
* Python 3.9 ( lien de téléchargement: <https://www.python.org/downloads>)

## 4. Installation du programme

* Cloner le dépôt en utilisant le terminal sous Mac/Linux ou l'invite de commandes sous Windows :<br>

	```
	git clone git@github.com:SelHel/Scraper-Books_to_Scrape.git
	```

* Ensuite, placez vous dans le dossier courant :

	```
	cd Scraper-Books_to_Scrape-main
	```
* Puis créez votre environnement virtuel :

	```
	python -m venv <your-virtual-env-name>
	```

* Activez votre environnement virtuel :

	```
	<your-virtual-env-name>\Scripts\activate.bat (sous Windows)
	```
	ou
	
	```
	source <your-virtual-env-name>/bin/activate (sous Mac/Linux)
	```

* Installez les dépendances avec la commande suivante :

	```
	pip install -r requirements.txt
	```

* Puis lancez le programme avec la commande :
        ```
	python main.py
	```
	
* Un menu va apparaître il ne vous restera plus qu'a choisir parmi les différentes options.

## 5. Résultat

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

*Engish version*

# Web Scraping "books.toscrape.com"

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
