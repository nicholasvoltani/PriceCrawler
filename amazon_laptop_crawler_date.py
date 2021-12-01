import sys
from bs4 import BeautifulSoup
from requests import get
from datetime import datetime


def main(URL):
    ## Accessing the URL
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    webpage = get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    ## Creating print-statement
    price = soup.find('span', class_="a-price").find('span').string.strip("R$").replace('.', '').replace(',', '.')

    ## Today
    today = datetime.today().strftime('%Y-%m-%d')

    ## Output phrase
    phrase = f"{today}, {price}"


    print(phrase)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 amazon_crawler.py <URL>")
        sys.exit(0)

    URL = sys.argv[1]
    main(URL=URL)

