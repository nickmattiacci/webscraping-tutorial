# Python
[Python](https://www.python.org/download/releases/3.0/)

## Libraries
#### HTTP Requests
* [Requests](http://docs.python-requests.org/en/master/)
#### HTML Parser
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
#### Data
* [Pandas](https://pandas.pydata.org/)

## How to run example
* Download python3
* Download and unzip this repository (the rest will assume you move the folder to your desktop)
* Open terminal
```
cd Desktop/webscraping-tutorial/python
```
* Hit enter
```
pip3 install requests
```
* Hit enter
```
pip3 install beautfulsoup4
```
* Hit enter
```
python3 main.py
```
* Hit enter

## Walk through
Return the HTML of a website:
```python
import requests # import library for sending HTTP requests
from bs4 import BeautifulSoup  # import library for parsing HTML

r = requests.get('http://books.toscrape.com') # make request to URL
if r.status_code != 200: # check if there is an error - 200 status code means successful
    print('Error getting website')
else:
    print(r.text) # html will be in body variable
```

Response:
```
<!DOCTYPE html>
<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html lang="en-us" class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html lang="en-us" class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en-us" class="no-js"> <!--<![endif]-->
    <head>
        <title>
    All products | Books to Scrape - Sandbox
</title>

        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <meta name="created" content="24th Jun 2016 09:29" />
        <meta name="description" content="" />
        <meta name="viewport" content="width=device-width" />
        <meta name="robots" content="NOARCHIVE,NOCACHE" />

        <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
        <!--[if lt IE 9]>
        <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->


            <link rel="shortcut icon" href="static/oscar/favicon.ico" />

.........
```

Parse the HTML and print data of interest:
```python
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
```

Response:
```
Title:  A Light in the ...
Price:  £51.77
---------------
Title:  Tipping the Velvet
Price:  £53.74
---------------
Title:  Soumission
Price:  £50.10
---------------
Title:  Sharp Objects
Price:  £47.82
---------------
Title:  Sapiens: A Brief History ...
Price:  £54.23
---------------
Title:  The Requiem Red
Price:  £22.65
---------------
Title:  The Dirty Little Secrets ...
Price:  £33.34
---------------
Title:  The Coming Woman: A ...
Price:  £17.93
---------------
Title:  The Boys in the ...
Price:  £22.60
---------------

.........
```
