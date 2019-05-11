from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.clever-tanken.de/tankstelle_details/48922")
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

priceRows = soup.find_all("div", class_="price-row")
for priceRow in priceRows:
    foundType = ""
    price = None
    name = None
    spans = priceRow.find_all("span")
    for span in spans:
        spanID = span.get('id')
        if spanID is not None and str(spanID).startswith('current-price'):
            price = float(span.string)

    divs = priceRow.find_all("div", class_="price-type-name")
    for div in divs:
        name = str(div.string)

    if price is not None and name is not None:
        print(name + ':' + "{:5.2f}".format(price))
