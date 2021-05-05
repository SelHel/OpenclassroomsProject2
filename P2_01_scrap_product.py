from bs4 import BeautifulSoup
import re
import requests

# Scrapping d'un livre

def get_and_parse(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    if result.ok:
        return(soup)

def scrap_book(url_book):
    soup = get_and_parse(url_book)
    # Je récupère l'url de la page du produit.
    product_page_url = url_book
    # Je récupère le code UPC.
    universal_product_code = soup.find('table', class_="table table-striped").find_all('td')[0].text
    # Je récupère le titre du livre
    title = soup.find('div', {'class': 'product_main'}).h1.text
    # Je récupère le prix du produit taxes incluses
    price_including_tax = soup.find('table', class_="table table-striped").find_all('td')[3].text[2:]
    # Je récupère le prix du produit hors taxes
    price_excluding_tax = soup.find('table', class_="table table-striped").find_all('td')[2].text[2:]
    # Je récupère le nombre de produits disponibles
    number_available = (re.sub("[^0-9]", "", soup.find('table', class_="table table-striped").find_all('td')[5].text))
    # Je récupère la description du produit
    product_description = soup.find('article', {'class': 'product_page'}).find_all('p')[3].text
    # Je récupère le nom de la catégorie
    category = soup.find('a', href = re.compile('../category/books/')).text
    # Je récupère la note des avis
    review_rating = soup.find('p', class_ = re.compile('star-rating')).get('class')[1]
    # Je récupère l'url de l'image 
    image_url = (url_book.replace('index.html', '') + soup.find('img').get('src'))