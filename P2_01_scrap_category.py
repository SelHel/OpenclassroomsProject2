from bs4 import BeautifulSoup 
import re
import requests
import os
from P2_01_scrap_product import scrap_book, get_and_parse

# Scrapping de tous les livres d'une categorie

def scrap_category(url_category):
    category_name = url_category.split("/")[6].split("_")[0].capitalize() # Je récupère le nom de la catégorie
    outf = open('data/' + category_name + '-data.csv', 'w') # Je créé un fichier csv avec le nom de chaque catégorie.
    books_urls = [] # Je déclare une variable qui va contenir les urls de tous les livres de la catégorie.
    # Je boucle sur toutes les pages de la catégorie et récupère les urls.
    for i in range(1,9):
        if i == 1:
            url_category
        else:
            url_category.replace("index", "page-" + str(i))
        
        soup = get_and_parse(url_category)
        link = ["/".join(url_category.split("/")[:-1]) + "/" + x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]
        books_urls.extend(link)
        print(link)
    
    outf.write('product page url,universal product code,title,price including tax, price excluding tax, number available, product description, category, review rating, image url\n')
    for row in books_urls:
        scrap_book(row)
        outf.write(product_page_url + ',' + universal_product_code + ',' + title + ',' + price_including_tax + ',' + price_excluding_tax + ',' + number_available + ',' + product_description + ',' + category + ',' + review_rating + ',' + image_url + ',' +'\n')
    outf.close()


