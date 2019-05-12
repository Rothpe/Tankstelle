# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
import serial
import time

def read_write_serial(command):
    print("writing to serial: " + command)
    s.write(command.encode())
    time.sleep(1)
    line = s.readline()
    print("recieved from serial: " + line.decode())


# from https://tutorials-raspberrypi.de/arduino-raspberry-pi-miteinander-kommunizieren-lassen/
s = serial.Serial('COM3', 9600, timeout=5)  # Namen ggf. anpassen
time.sleep(10)
read_write_serial("#\n")
read_write_serial("#\n")

# Load Website into DOM Tree (https://de.wikipedia.org/wiki/Document_Object_Model)
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
        print(name + ':' + "{:5.2f}".format(price) + "9")
        # Marker \n means NEW Entry
        # Marker : seperates Name and Price
        read_write_serial(name + ':' + "{:5.2f}".format(price) + "9")


