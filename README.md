# webscraping-tutorial

## Need to know:
* HTTP requests
    * basically just what they are - requests & responses sent back and forth from computer to server
* HTTP Headers
    * Have a basic idea of what they are (meta data that provides information to the server about your request)
    * Know how to implement them in code (https://curl.trillworks.com/ - mentioned below, will be a savior for this)
    * Always delete 'Accept-Encoding'
* HTML
    * language websites are built in - know what HTML tags are basically
* CSS
    * language for website styling - you will use to more accurately find the information you are looking for in the HTML
    * know what CSS selectors are ie. id's and classes
* JSON
    * response format from APIs
    * know how to traverse through JSON

## Resources:
* Chrome Developer Tools
    * Mac: Option + Command + i, Windows: Ctrl + Shift + i or F12
    * Need to be familiar with the 'Elements' and 'Network' tabs
    * In the Network tab you will find the exact request you will be trying to replicate (a lot of the requests you will see in hear are irrelevant, use the search function to find what you are looking for)
    * In the Elements tab you will find the HTML, use the search functionality or the box with the arrow in it button (use on actual browser window) to find the element you are looking for, right click > copy > copy selector will be useful when parsing HTML
* https://curl.trillworks.com/
    * When you find the request you are looking for in the Network tab, right click > copy > copy as curl
    * Paste into box on left side and the site will translate the curl into code
    * This is just an easy shortcut so you don't have to memorize the exact format for requests
