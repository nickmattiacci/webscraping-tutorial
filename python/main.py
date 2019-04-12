import requests # import library for sending HTTP requests
from bs4 import BeautifulSoup  # import library for parsing HTML

r = requests.get('http://books.toscrape.com') # make request to URL
if r.status_code != 200: # check if there is an error - 200 status code means successful
    print('Error getting website')
else:
    soup = BeautifulSoup(r.text, 'html.parser') # load HTML into parser
    books = soup.find_all('article') # each book is in an article HTML tag
    for book in books: # iterate through books
        title = book.find('h3').text # price is in H3 tag, within the article element
        price = book.find('p', class_ = 'price_color').text # price is in p tag with 'price_color' class, within the article element
        print('Title: ', title) # print title
        print('Price: ', price) # print price
        print('--------------') # print line for readability
