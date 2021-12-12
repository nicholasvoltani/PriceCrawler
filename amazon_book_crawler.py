import sys
from bs4 import BeautifulSoup
from requests import get


def main(URL):
    ## Accessing the URL
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

    webpage = get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml", from_encoding='utf8')


    ## Creating print-statement
    price =float(soup.find('span', id="price").string.split()[1].replace(",", "."))
    title = soup.find('span', id="productTitle").string.strip('\n')

    ## Fetching the (first) author
    authors = soup.find('span', class_='author notFaded')
    
    ## Code idea from G. Solis: tries running first command; if False/None/''/etc, runs second line after `or`
    author = (authors.find('a', class_="a-link-normal contributorNameID") 
          or authors.find('a', class_="a-link-normal")).string  

    ## Output phrase
    phrase = f"\nO valor de {title}, de {author}, é de R${price:.2f}"

    ## Looking if price is a discount or not; code idea from G. Solis
    if (listPrice := soup.find('span', id="listPrice")) is not None:
        original_price = float(listPrice.string.split()[1].replace(",", "."))
        phrase += f'; originalmente estava a R$ {original_price:.2f} ' \
                  f'(desconto de {(1 - price/original_price)*100:.2f}%).'
    else:
        phrase += "não há nenhum desconto no momento."

    ## Output information
    print(phrase)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 amazon_crawler.py <URL>")
        sys.exit(0)

    URL = sys.argv[1]
    main(URL=URL)