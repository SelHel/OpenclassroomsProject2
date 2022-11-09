*French version*

# Web Scraping du site "books.toscrape.com"

## 1. Descriptif

Programme "Scraper" qui permet de collecter les données de n'importe quel livre du site [books.toscrape.com](http://books.toscrape.com)<br>

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

Ces données sont stockées dans un fichier CSV enregistré dans un dossier "Books\_To\_Scrape".<br>
Les images de couverture des livres sont également téléchargées et stockées dans un sous-dossier "Images".

## 2. Prérequis

* Python 3+ (lien de téléchargement: <https://www.python.org/downloads>)

## 3. Bibliothèques Python utilisées

* Requests
* BeautifulSoup

## 4. Installation

Cloner le dépôt en utilisant le terminal sous Mac/Linux ou l'invite de commandes sous Windows :<br>
```
git clone git@github.com:SelHel/Scraper-Books_to_Scrape.git
```

Ensuite, placez vous dans le dossier courant :
```
cd Scraper-Books_to_Scrape-main
```

Puis créez votre environnement virtuel :
```
python -m venv <your-virtual-env-name>
```

Activez votre environnement virtuel :
```
<your-virtual-env-name>\Scripts\activate.bat (sous Windows)
```
ou
	
```
source <your-virtual-env-name>/bin/activate (sous Mac/Linux)
```

Vous devez maintenant installer toutes les librairies nécessaires au bon fonctionnement de ce programme, pour cela exécuter la commande suivante :
```
pip install -r requirements.txt
```
	
## 5. Exécution

Pour exécuter le programme lancez le script "main.py" avec la commande suivante :
```
python main.py
```

Un menu va apparaître, il ne vous restera plus qu'a choisir parmi les différentes options.

## 6. Résultat

Après avoir exécuté une des commandes, un dossier "Books\_To\_Scrape" sera créé dans le dossier courant.  
Il se décomposera comme suit :

* Dossier : "Books\_To\_Scrape"
	* Sous-dossier : "Nom de la catégorie du livre"
  		* Sous-dossier : "Images" (uniquement si vous scrapé une catégorie ou toutes les catégories)
		* Fichier : "*Nom de la catégorie du livre*-data".csv

----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------

*Engish version*

# Web Scraping of "books.toscrape.com"

## 1. Description

"Scraper" program that retrieves data from any book on the website [books.toscrape.com](http://books.toscrape.com).<br>

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

## 2. Requirements

* Python 3+ (download link: <https://www.python.org/downloads>)

## 3. Python libraries used

* Requests
* BeautifulSoup

## 4. Installation

Clone repository using Terminal on Mac/Linux or Command Prompt on Windows:<br>
```
git clone git@github.com:SelHel/Scraper-Books_to_Scrape.git
```

Then go to the current directory as follows :
```
cd Scraper-Books_to_Scrape-main
```

Create a virtual environment :
```
python -m venv <your-virtual-env-name>
```

Activate your virtual environment :
```
<your-virtual-env-name>\Scripts\activate.bat (on Windows)
```
or
	
```
source <your-virtual-env-name>/bin/activate (on Mac/Linux)
```

You now need to install all the libraries necessary for this program to work properly, for this run the following command :
```
pip install -r requirements.txt
```

## 5. Execution

Run the program with the following command :

```
python main.py

```
Menu will appear. Then you will choose from different options.

## 6. Result

After executing a choice, "Books\_To\_Scrape" directory will be created in the current directory.  
It will be like that :

* Directory : "Books\_To\_Scrape"
	* Subdirectory : "Book's Category name"
  		* Subdirectory : "Images" (only if you scrape category or all categories)
		* File : "*Book's Category name*-data".csv
