# PriceCrawler
## A web-crawler to find prices in Amazon/MagaLu

Usage: python3 <price_crawler.py> <site_URL> 

# First Method: BeautifulSoup4 + Requests
It essentially does a GET request via `requests.get`, and parses the HTML via `bs4.BeautifulSoup`, then proceeds to find the correct `span` tag with the `price` (and the `author`, if it's searching for books).


# Second Method: Selectolax + Httpx
It does a GET request via `httpx.get` and parses the HTML via `selectolax.parser.HTMLParser`, then proceeds to find the correct `span` tag with the `price` (and the `author`, if it's searching for books).

# Comparison
```
import timeit

# code snippet to be executed only once
mysetup = '''
from bs4 import BeautifulSoup
from requests import get
'''
 
# code snippet whose execution time
# is to be measured
mycode = '''
def main():
    URL = r"https://www.amazon.com.br/que-Dialética-Coleção-Primeiros-Passos/dp/8511010238"
    ## Accessing the URL
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

    webpage = get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")


    ## Creating print-statement
    price = soup.find('span', class_="a-price").find('span').string

    ## Output phrase
    phrase = f"O preço é de {price}"

'''
 
# timeit statement
print ("The time of execution of the first program is :",
       timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 100000))

# code snippet to be executed only once
mysetup = '''
from selectolax.parser import HTMLParser
import httpx
import unicodedata
'''
 
# code snippet whose execution time
# is to be measured
mycode = '''
def main():
    URL = r"https://www.amazon.com.br/que-Dialética-Coleção-Primeiros-Passos/dp/8511010238"
    ## Accessing the URL
    html = httpx.get(URL)
    parser = HTMLParser(html.content)

    ## Price
    price = unicodedata.normalize('NFKC', parser.css_first('span#price').text())
    price = price.split()[1].replace('.', '').replace(',', '.')

    ## Output phrase
    phrase = f"O preço é de {price}"

'''
 
# timeit statement
print ("The time of execution of the second program is :",
       timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 100000))


```

Both times of execution vary while running this script consecutively; sometimes the second script outperforms the first, sometimes the opposite happens. Perhaps it has to do with the GET requests, which are the main bottleneck for these kind of scripts.