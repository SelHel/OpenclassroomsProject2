from bs4 import BeautifulSoup
import re
import requests
import os
import wget

CUR_DIR = os.path.dirname(__file__)

# Scrapping d'un livre

# Fonction qui permet de récupérer et d'analyser le contenu d'une url
def get_and_parse(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    if result.ok:
        return(soup)

# Fonction qui permet le scrapping d'un livre et l'écriture des données dans un fichier csv
def scrap_book(url_book):
    soup = get_and_parse(url_book)
    product_page_url = url_book # Je récupère l'url de la page du produit.
    universal_product_code = soup.find('table', class_="table table-striped").find_all('td')[0].text # Je récupère le code UPC.
    title = soup.find('div', {'class': 'product_main'}).h1.text # Je récupère le titre du livre
    price_including_tax = soup.find('table', class_="table table-striped").find_all('td')[3].text[2:] # Je récupère le prix du produit taxes incluses
    price_excluding_tax = soup.find('table', class_="table table-striped").find_all('td')[2].text[2:] # Je récupère le prix du produit hors taxes
    number_available = (re.sub("[^0-9]", "", soup.find('table', class_="table table-striped").find_all('td')[5].text)) # Je récupère le nombre de produits disponibles
    product_description = soup.find('article', {'class': 'product_page'}).find_all('p')[3].text # Je récupère la description du produit
    category = soup.find('a', href = re.compile('../category/books/')).text # Je récupère le nom de la catégorie
    review_rating = soup.find('p', class_ = re.compile('star-rating')).get('class')[1] # Je récupère la note des avis
    image_url = (url_book.replace('index.html', '') + soup.find('img').get('src')) # Je récupère l'url de l'image
    os.makedirs('data/' + category, exist_ok=True) # Je créé un dossier qui porte le nom de la catégorie
    path = 'data/' + category + category + '-data.csv'
    liste_path = os.path.join(CUR_DIR, path)
    
    if os.path.exists(liste_path): # si le fichier existe j'ajoute les informations.
        with open(path, 'a') as file:
            file.write(product_page_url + ',' + universal_product_code + ',' + title + ',' + price_including_tax + ',' + price_excluding_tax + ',' + number_available + ',' + product_description + ',' + category + ',' + review_rating + ',' + image_url + ',' +'\n')
    else:
        with open(path, 'a') as file: # Sinon je créé un fichier et j'ajoute les informations
            file.write('prduct page url,universal product code,title,price including tax, price excluding tax, number available, product description, category, review rating, image url\n')
            file.write(product_page_url + ',' + universal_product_code + ',' + title + ',' + price_including_tax + ',' + price_excluding_tax + ',' + number_available + ',' + product_description + ',' + category + ',' + review_rating + ',' + image_url + ',' +'\n')


# Fonction qui permet de télécharger les images d'une url
def download_image(url):
    soup = get_and_parse(url)
    title = soup.find('div', {'class': 'product_main'}).h1.text.replace(" ","_") # Je récupère le titre du livre
    category_name = soup.find('a', href = re.compile('../category/books/')).text # Je récupère le nom de la catégorie
    image_url = (url.replace('index.html', '') + soup.find('img').get('src')) # Je récupère l'url de l'image
    os.makedirs('data/' + category_name + '/images/' , exist_ok=True) # Je créé un dossier image
    wget.download(image_url, 'data/' + category_name + '/images/' + "/" + title +'.jpg') # Je télécharge l'image