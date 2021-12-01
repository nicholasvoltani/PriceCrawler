import sys
#from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser

#from requests import get
import httpx

def main(URL):
    ## Accessing the URL
    html = httpx.get(URL)
    parser = HTMLParser(html.content)

    ## Price
    price = float(parser.css_first('span.a-price').text().split('R$')[1].replace('.', '').replace(',', '.'))

    ## Output phrase
    phrase = f"O preço é de {price}"

    print(phrase)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 quicker_laptop_crawler.py <URL>")
        sys.exit(0)

    URL = sys.argv[1]
    main(URL = URL)
    
