import sys
from P2_01_scrap_product import *
from P2_01_scrap_category import *
from P2_01_scrap_all_categories import *

menu = """Choose one of the following options: 
1: Scrape a book
2: Scrape a category
3: Scrape all books from all categories
4: Exit

Enter your choice: """ 

choice_menu = ['1', '2', '3', '4']

while True:
    user_choice = input(menu) # Get user's choice

    if user_choice not in choice_menu : # If user's choice is not in choice menu
        print('Please choose a valid option...')
        continue

    if user_choice == '1': # If user's choice is 1, scrape book from user's url
        user_url = input("Please enter the book's url: ") # Get user's url
        all_books_urls = get_all_books_urls() # Make a list and store all product urls
        if user_url not in all_books_urls: # Check if user's url is valid
            print('Please enter a valid url...')
        else:
            scrap_book(user_url)
    
    elif user_choice == '2': # If user's choice is 2, scrape category from user's url
        user_url = input("Please enter the category's url: ") # Get user's url
        main_url = "https://books.toscrape.com/" 
        soup = get_and_parse(main_url)
        category_urls = [main_url + x.get('href') for x in soup.find_all('a', href=re.compile('catalogue/category/books'))] # Make a list and store all category urls
        if user_url not in category_urls: # Check if user's url is valid
            print('Please enter a valid url...')
        else:
            scrap_category(user_url)
    
    elif user_choice == '3': # If user's choice is 3, scrape all website
        main_url = "https://books.toscrape.com/"
        scrap_all_categories(main_url)
    
    elif user_choice == '4': # If user's choice is 4, Exit program
        print('Goodbye!')
        sys.exit()
    
    print("-" * 50)
