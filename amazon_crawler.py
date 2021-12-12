import sys
from bs4 import BeautifulSoup
from requests import get


def main(URL):
    ## Accessing the URL
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

    webpage = get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")


    ## Creating print-statement
    price = soup.find(id="price").string.split("\xa0")[1]
    title = soup.find(id="productTitle").string.replace('\n','')

    ## Fetching the (first) author
    authors = soup.find('span', class_='author notFaded')
    try:
        ## Has dropdown information on author 
        author = authors.find('a', class_="a-link-normal contributorNameID").string
    except:
        ## Fetch author as usual
        author = authors.find('a', class_="a-link-normal").string

    ## Output phrase
    phrase = f"\nO valor de {title}, de {author}, é de R${price}"

    ## Looking if price is a discount or not
    try: 
        original_price = soup.find(id="listPrice").string.split("\xa0")[1]
        phrase += f"; originalmente estava a R$ {original_price}; descont de {price*100/original_price}%."

    except:
        phrase += "; não há nenhum desconto no momento."

    ## Output information
    print(phrase)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 amazon_crawler.py <URL>")
        sys.exit(0)

    URL = sys.argv[1]
    main(URL=URL)