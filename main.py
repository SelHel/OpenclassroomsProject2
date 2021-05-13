import sys
from scrap_book import *
from scrap_category import *
from scrap_all_categories import *
import requests

menu = """Choose one of the following options: 
1: Scrape a book
2: Scrape a category
3: Scrape all books from all categories
4: Exit

Enter your choice: """ 

choice_menu = ['1', '2', '3', '4']

while True:
    user_choice = input(menu) # Get user's choice

    if user_choice not in choice_menu : # If the user's choice is not in choice menu
        print('Please choose a valid option...')
        continue

    if user_choice == '1': # If the user's choice is 1, scrape book from the user's URL
        user_url = input("Please enter the book's URL: ") # Get user's URL

        if "://books.toscrape.com/catalogue/" in user_url and requests.get(user_url).ok: # If the user's URL exists scrap book
                scrap_book(user_url)            
        else:
            print('Please enter a valid URL...')
    
    elif user_choice == '2': # If the user's choice is 2, scrape category from the user's url
        user_url = input("Please enter the category's url: ") # Get user's URL
        
        if "://books.toscrape.com/catalogue/category/books/" in user_url and requests.get(user_url).ok: # If the user's URL exists scrap category
                scrap_category(user_url)            
        else:
            print('Please enter a valid URL...')
    
    elif user_choice == '3': # If the user's choice is 3, scrape all website
        site_url = "https://books.toscrape.com/"
        scrap_all_categories(site_url)
    
    elif user_choice == '4': # If the user's choice is 4, Exit program
        print('Goodbye!')
        sys.exit()
    
    print("-" * 50)