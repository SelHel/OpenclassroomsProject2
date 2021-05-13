from bs4 import BeautifulSoup 
import re
import requests
import os
import shutil
from scrap_book import *

# Scraping all books in category

# This function extracts the information and images from all books of all category's pages. 
def scrap_category(category_url):
    soup = get_and_parse(category_url)
    category_name = soup.find('div', {'class': 'page-header action'}).h1.text # Get category name
    cur_dir = os.path.dirname(__file__) # Get current directory path
    path_dir = 'Books_To_Scrape/' + category_name # Get category directory path
    liste_path = os.path.join(cur_dir, path_dir)
    if os.path.isdir(liste_path):  # Check if the directory already exists 

        if os.path.isfile(path_dir + '/' + category_name + '-data.csv'): # If the CSV file already exists, remove it
            os.remove(path_dir + '/' + category_name + '-data.csv')
        
    else:                          # If it does not exist make a directory
        os.makedirs('Books_To_Scrape', exist_ok=True)
    
    category_pages_url = [] # Make a list to store the URLs of category pages
    test_url = category_url.replace('index', 'page-1') # Replace the end of the URL by page-1
    response = requests.get(test_url)
    if response.ok: # Check if url exists
        new_page = test_url #category_url.replace('index', 'page-1')
        i = 2
        while requests.get(new_page).status_code == 200: # While status code is 200 append the page URL in the list
            category_pages_url.append(new_page)
            new_page = category_url.replace('index', 'page-' + str(i)) # Try to access to the next pages by adding 1 to the page URL
            i += 1
    else:
        category_pages_url.append(category_url) # If page-1 doesn't exist, append index page URL of the category to the list

    for page_url in category_pages_url: # Make a list and store all books URLs for each category's page
        soup = get_and_parse(page_url)
        books_url = ['/'.join(page_url.split('/')[:-1]) + '/' + x.div.a.get('href') for x in soup.find_all('article', class_ = 'product_pod')] # Get books URLs 

        for book in books_url: # Extracts the information and image for each category's book
            book_dict = scrap_book(book, print_product=False)
            download_image(book_dict)

    print("Done scraping " + category_name)