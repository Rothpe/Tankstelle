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

# Search for DIV Tag with attribute ng-controller="SpritsortenController"
rootDivTags = soup.find_all('div')
for rootDivTag in rootDivTags:
    ngController = rootDivTag.get('ng-controller')
    ngInit = rootDivTag.get('ng-init')

    if ngController == "SpritsortenController":
        foundType = ""

        subDivs = rootDivTag.find_all("div", class_="fuel-price-type")
        for subDiv in subDivs:
            # First Span Tag
            spans = subDiv.find("span")
            for spanContent in spans:
                foundType += spanContent.string

        # Remove init(' ') from string, and convert to double
        price = float(ngInit.replace("init('", "").replace("')", "").replace(",", "."))
        # print(type(ngInit))
        print(foundType + ": " + str(price))
        # Marker \n means NEW Entry
        # Marker : seperates Name and Price
        read_write_serial(foundType + ":" + str(price))

# Code example to parse from Browser to compare

# <div class="fuel-price-entry" ng-controller="SpritsortenController" ng-init="init('1,289')">
# 		<div class="fuel-price-type"><span>Super E5</span><span class="mtsk-label"> MTS-K Preis </span></div>
#     <div class="price-box">
# 			<div class="price-input" ng-class="{'price-dirty': dirty}">
# 				<span ng-click="minus()" class="decrease-price">-</span><span class="price-field"><span ng-bind="display_preis">1.28 </span> <sup ng-bind="suffix">9</sup></span><span ng-click="plus()" class="increase-price">+</span>
# 			</div>
#       <button
#         ng-cloak
#         ng-click="melden('True','48922', 'Super E5  (DE)', '7')"
#         ng-show="dirty"
#         class="report-price"
#         type="submit">
#         <img
#           src="/static/img/melder_icon_standard.png"
#           class="report_price_symbol"/>
#           <span
#             class="report_price_label">
#             MTS-K Beschwerde
#           </span>
#         </button>
#     </div>
#   </div>
