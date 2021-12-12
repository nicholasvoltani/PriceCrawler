# PriceCrawler
## A web-crawler to find prices in Amazon/MagaLu

Usage: python3 <price_crawler.py> <site_URL> 

# First Method: BeautifulSoup4 + Requests
It essentially does a GET request via `requests.get`, and parses the HTML via `bs4.BeautifulSoup`, then proceeds to find the correct `span` tag with the `price` (and the `author`, if it's searching for books).


# Second Method: Selectolax + Httpx
It does a GET request via `httpx.get` and parses the HTML via `selectolax.parser.HTMLParser`, then proceeds to find the correct `span` tag with the `price` (and the `author`, if it's searching for books).

