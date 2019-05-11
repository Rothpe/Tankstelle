# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.clever-tanken.de/tankstelle_details/48922")
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

priceRows = soup.find_all("div", class_="price-row")
for priceRow in priceRows:
    foundType = ""
    spans = priceRow.find_all("span")
    for span in spans:
        id = span.get('id')
        if id is not None and str(id).startswith('current-price'): #NICHT current-price-1, denn in Zeile 2 is es current-price-2
            price = float(span.string)

            #print("Test" + ": " + str(price))

divs = soup.find_all("div", class_="price-type-name")
for div in divs:
    name = (div.string)
    #print(name)

    print(str(price) + ": " + str(name))
            

