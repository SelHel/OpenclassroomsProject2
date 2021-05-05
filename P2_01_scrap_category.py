from bs4 import BeautifulSoup 
import re
import requests
import os
import csv
from P2_01_scrap_product import scrap_book, get_and_parse, download_image

# Scrapping de tous les livres d'une categorie

def scrap_category(url_category):
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
    
    for row in books_urls:
        download_image(row)
        scrap_book(row)


