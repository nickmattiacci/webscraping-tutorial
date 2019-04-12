# NodeJS
[NodeJS](https://nodejs.org/en/)

## Libraries
#### HTTP Requests
* [Request](https://github.com/request/request)
* [Puppeteer](https://github.com/GoogleChrome/puppeteer)
#### HTML Parser
* [Cheerio](https://github.com/cheeriojs/cheerio)
#### Data
* [Exceljs](https://github.com/exceljs/exceljs)

## Walk Through
Return the HTML of a website:
```javascript
const request = require('request'); // import library for sending HTTP requests
const cheerio = require('cheerio'); // import library for parsing HTML

request('http://books.toscrape.com', (err, resp, body) => { // make request to URL
    if (err || resp.statusCode !== 200) { // check if there is an error - 200 status code means successful
        console.log('Error getting website');
    } else {
        console.log(body) // html will be in body variable
    }
});
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
```javascript
const request = require('request'); // import library for sending HTTP requests
const cheerio = require('cheerio'); // import library for parsing HTML

request('http://books.toscrape.com', (err, resp, body) => { // make request to URL
    if (err || resp.statusCode !== 200) { // check if there is an error - 200 status code means successful
        console.log('Error getting website');
    } else {
        let $ = cheerio.load(body); // load HTML into parser
		$('article').each((index, element) => { // each book is in an article HTML tag
			let title = $('h3', element).text(); // price is in H3 tag, within the article element
			let price = $('p.price_color', element).text(); // price is in p tag with 'price_color' class, within the article element
			console.log('Title: ', title); // print title
			console.log('Price: ', price); // print price
			console.log('---------------'); // print line for readability
		});
    }
});
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
