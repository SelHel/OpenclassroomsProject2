# Scraping "books.toscrape.com"

Programme "Scraper" qui récupère les informations de n'importe quel livre du site [Books to Scrape](http://books.toscrape.com).

## Descriptif

Le programme doit être capable d'extraire les informations des livres et de les écrire dans un fichier CSV et l'enregistré dans un sous-dossier du dossier courant.

Liste des informations à récupérer:

* Product page url
* Universal product code
* Title
* Price including tax
* Price excluding tax
* number_available
* product_description
* category
* review_rating
* image_url 

Il doit également télécharger les images de couverture des livres dans un sous-dossier Images.

Le repository contient quatre scripts:  

* main.py 
* P2\_01\_scrap\_product.py
* P2\_01\_scrap\_category.py
* P2\_01\_scrap\_all\_categories.py

### A) main.py

Le script *"main.py"* est le script principal qui va permettre à l'utilisateur d'accéder à un menu et d'effectuer un choix parmi les 4 options suivantes :

1. Récupérer les informations d'un seul livre en entrant l'url du livre et les stocker dans un fichier csv.
2. Récupérer les informations et les images de tous les livres d'une seule catégorie en entrant l'url de la catégorie et les stocker dans un fichier csv et un dossier images.
3. Récupérer les informations et les images de tous les livres du site.
4. Quitter le programme


##### B) P2\_01\_scrap\_product.py

Le script "P2\_01\_scrap\_product.py" contient les fonctions *scrap\_book* et *download\_image* qui comme leur nom l'indique vont permettre de scraper les informations d'un seul livre et de télécharger son image de couverture.

##### C) P2\_01\_scrap\_category.py

Le script "P2\_01\_scrap\_category.py" contient la fonction *scrap\_category* qui va permettre de scraper les informations et les images de tous les livres d'une catégorie.


##### D) P2\_01\_scrap\_all\_categories.py

Le script "P2\_01\_scrap\_all\_categories.py" contient la fonction *scrap\_all\_categories* qui va permettre de scraper les informations et les images de tous les livres du site.

## Prérequis
* Python 3.9 ( lien de téléchargement: <https://www.python.org/downloads>)

## Démarrage du programme

Après avoir téléchargé le dossier **OpenclassroomsProject2-main.zip** depuis ce lien [GitHub](https://github.com/SelHel/OpenclassroomsProject2).  
Extraire les fichiers dans un dossier de votre choix.  
Ensuite, en utilisant le terminal sur Mac et Linux ou l'invite de commandes sur Windows :

1. Placez vous dans le dossier courant
2. Créez un environnement virtuel
3. Activez votre environnement environnement virtuel
4. Installez les modules nécessaires au bon fonctionnement du programme depuis le fichier requirements.txt

```
 /Users/../OpenclassroomsProject2-main
 python3 -m venv env
 cd env
 cd bin
 source activate 
 pip install -r requirements.txt

```
Toujours dans le terminal revenez à la racine du dossier courant grâce à la commande "cd .."

```
cd ..
cd ..
 /Users/../OpenclassroomsProject2-main

```
Puis lancez le script *"main.py"*

```
python main.py

```
Un menu va apparaître il ne vous restera plus qu'a choisir parmi les différentes options.

## Résultat

Après avoir exécuter une des commandes, un dossier "Books\_To\_Scrape" sera créer dans le dossier courant.  
Il se décomposera comme suit :

* Dossier : "Books\_To\_Scrape"
	* Sous-dossier : "Nom de la catégorie du livre"
  		* Sous-dossier : "Images" (uniquement si vous scraper une catégorie ou toutes les catégories)
		* Fichier : "*Nom de la catégorie du livre*-data".csv

## Auteur

Selim Helaoui