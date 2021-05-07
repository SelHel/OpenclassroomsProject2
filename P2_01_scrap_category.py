from bs4 import BeautifulSoup 
import re
import requests
import os
import shutil
from P2_01_scrap_product import *

# Scraping all books in category

# This function extracts the information and images from all books of all category's pages. 
def scrap_category(category_url):
    soup = get_and_parse(category_url)
    category_name = soup.find('div', {'class': 'page-header action'}).h1.text # Get category name
    cur_dir = os.path.dirname(__file__)
    path_dir = 'Books_To_Scrape/' + category_name
    liste_path = os.path.join(cur_dir, path_dir)
    if os.path.isdir(liste_path):                # check if the directory already exists
        shutil.rmtree('Books_To_Scrape/' + category_name)
    else:                                        # if it does not exist make a directory
        os.makedirs('Books_To_Scrape', exist_ok=True)
    
    category_pages_url = [] # Make a list to store URLs of category pages
    test_url = category_url.replace('index', 'page-1') # Replace the end of the url by page-1
    reponse = requests.get(test_url)
    if reponse.ok: # If page-1 exist
        for i in range(1, 9): # Try to access to the next pages
            url_page = category_url.replace('index', 'page-' + str(i))
            reponse = requests.get(url_page)
            if reponse.ok:
                category_pages_url.append(url_page) # Append the url in the list
    else:
        category_pages_url.append(category_url) # If page-1 doesn't exist, append index page URL of the category to the list

    for page_url in category_pages_url: # Make a list and store all books urls for each category's page
        soup = get_and_parse(page_url)
        books_url = ['/'.join(page_url.split('/')[:-1]) + '/' + x.div.a.get('href') for x in soup.find_all('article', class_ = 'product_pod')] # Get books URLs 

        for book in books_url: # Extracts the information and image for each category's book
            download_image(book)
            scrap_book(book)



