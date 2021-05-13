from bs4 import BeautifulSoup
import re
import requests
import os
from scrap_book import *
from scrap_category import *

# Scraping all books from all categories.

# This function extract the information and images of all books from all categories of the website.
def scrap_all_categories(main_url):
    soup = get_and_parse(main_url)
    category_urls = [main_url + x.get('href') for x in soup.find_all('a', href=re.compile('catalogue/category/books'))] # Make a list and store all category urls
    category_urls = category_urls[1:] # Remove the first item from the list because it corresponds to the url "All books".
    for url in category_urls: 
        scrap_category(url)     # Extract the information and images of all books in each category




    

