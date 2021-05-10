from bs4 import BeautifulSoup
import re
import requests
import os
import wget
import shutil

# Scraping a book

# This function is used to check and analyze a url.
def get_and_parse(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    if result.ok:
        return(soup)

# This function retrieves the books urls from any page of the site
def get_books_urls(url):
    soup = get_and_parse(url)
    return(["/".join(url.split("/")[:-1]) + "/" + x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]) # remove the index.html part of the base url before returning the results

# This function retrieves the all books urls of the site
def get_all_books_urls():
    pages_urls = []
    books_urls = []
    new_page = "https://books.toscrape.com/catalogue/page-1.html"
    while requests.get(new_page).status_code == 200:
        pages_urls.append(new_page)
        new_page = pages_urls[-1].split("-")[0] + "-" + str(int(pages_urls[-1].split("-")[1].split(".")[0]) + 1) + ".html"
    for page in pages_urls:
        books_urls.extend(get_books_urls(page))
    return books_urls

# This function extracts all the information of a book and writing the data to a csv file and makes a directory with the category name to stores it.
def scrap_book(url_book):
    soup = get_and_parse(url_book)
    product_page_url = url_book 
    universal_product_code = soup.find('table', class_='table table-striped').find_all('td')[0].text 
    title = soup.find('div', {'class': 'product_main'}).h1.text 
    price_including_tax = soup.find('table', class_='table table-striped').find_all('td')[3].text[2:] 
    price_excluding_tax = soup.find('table', class_='table table-striped').find_all('td')[2].text[2:] 
    number_available = (re.sub('[^0-9]', '', soup.find('table', class_='table table-striped').find_all('td')[5].text)) 
    product_description = soup.find('article', {'class': 'product_page'}).find_all('p')[3].text 
    category = soup.find('a', href = re.compile('../category/books/')).text.replace(' ', '_') 
    review_rating = soup.find('p', class_ = re.compile('star-rating')).get('class')[1] 
    image_url = (url_book.replace('index.html', '') + soup.find('img').get('src')) 
    os.makedirs('Books_To_Scrape/' + category, exist_ok=True) 
    cur_dir = os.path.dirname(__file__)
    path_file = 'Books_To_Scrape/' + category + '/' + category + '-data.csv'
    liste_path = os.path.join(cur_dir, path_file)
    #print('Product page url: ' + product_page_url + '\n' + 'Universal product code: ' + universal_product_code + '\n' + 'Title: ' + title + '\n' + 'Price incluging tax: ' + price_including_tax + '\n' + 'Price excluding tax: ' + price_excluding_tax + '\n' + 'Number available: ' + number_available + '\n' + 'Product description: ' + product_description + '\n' + 'Category: ' + category + '\n' + 'Review rating: ' + review_rating + '\n' + 'Image url: ' + image_url)

    if os.path.exists(liste_path): 
        with open(path_file, 'a') as file:
            file.write(product_page_url + '|' + universal_product_code + '|' + title + '|' + price_including_tax + '|' + price_excluding_tax + '|' + number_available + '|' + product_description + '|' + category + '|' + review_rating + '|' + image_url + '|' +'\n')
    else:
        with open(path_file, 'w') as file: 
            file.write('product page url, universal product code, title, price including tax, price excluding tax, number available, product description, category, review rating, image url\n')
            file.write(product_page_url + '|' + universal_product_code + '|' + title + '|' + price_including_tax + '|' + price_excluding_tax + '|' + number_available + '|' + product_description + '|' + category + '|' + review_rating + '|' + image_url + '|' +'\n')
    

# This function makes a directory with the category name and extracts the image from the url in this directory.
def download_image(url):
    soup = get_and_parse(url)
    title = (re.sub('[^a-zA-Z0-9 ]', '',soup.find('div', {'class': 'product_main'}).h1.text)) # Get title of the book
    title = re.sub('[ ]', '_', title)[0:30]
    category_name = soup.find('a', href = re.compile('../category/books/')).text.replace(' ', '_') # Get category name
    image_url = (url.replace('index.html', '') + soup.find('img').get('src')) # Get image url
    cur_dir = os.path.dirname(__file__)
    os.makedirs('Books_To_Scrape/' + category_name + '/' + 'Images/' , exist_ok=True) # Make a directory "images" in category directory
    path_image = 'Books_To_Scrape/' + category_name + '/' + 'Images/' + title +'.jpg'
    list_path = os.path.join(cur_dir, path_image)
    if not os.path.isfile(list_path): # Download image if it does not exist
        wget.download(image_url, 'Books_To_Scrape/' + category_name + '/' + 'Images/' + title +'.jpg', bar = None)