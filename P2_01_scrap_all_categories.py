from bs4 import BeautifulSoup
import re
import requests
import os
from P2_01_scrap_category import scrap_category

# Scrapping de toutes les catégories

main_url = 'http://books.toscrape.com/'
result = requests.get(main_url)
soup = BeautifulSoup(result.text, 'html.parser')

categories_url = [main_url + x.get('href') for x in soup.find_all("a", href=re.compile("catalogue/category/books"))]
categories_url = categories_url[1:] # Je retire le premier élément de ma liste car il correspond à l'url "All books".

for category_url in categories_url:
    scrap_category(category_url)





    

