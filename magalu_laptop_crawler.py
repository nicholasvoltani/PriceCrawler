#!/usr/bin/python3

import sys
from selectolax.parser import HTMLParser
import httpx
from datetime import datetime

def main(URL):
    ## Accessing the URL
    html = httpx.get(URL)
    parser = HTMLParser(html.content)

    ## Price
    price = float(parser.css('span.price-template__text')[0].text().replace(".", "").replace(",", "."))

    ## Today
    today = datetime.today().strftime('%Y-%m-%d')

    ## Output phrase
    phrase = f"{today}, {price}"

    print(phrase)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 quicker_laptop_crawler.py <URL>")
        sys.exit(0)

    URL = sys.argv[1]
    main(URL=URL)

