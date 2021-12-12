import sys
from datetime import datetime
from selectolax.parser import HTMLParser
import httpx


def main(URL):
    ## Accessing the URL
    html = httpx.get(URL)
    parser = HTMLParser(html.content)


    ## Creating print-statement
    price = unicodedata.normalize('NFKC', parser.css_first('span#price').text())
    price = price.split()[1].replace('.', '').replace(',', '.')
    
    title = parser.css_first('span#productTitle').text()
    authors = soup.find('span', class_ = 'author notFaded')
    
    ## Code idea from G. Solis: tries running first command; if False/None/''/etc, runs second one after `or`
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
    main(URL = URL)