import requests
import json
from xml.etree import ElementTree as ET
import os
from xml.dom import minidom

url = "https://bathbodyur.myvtex.com/api/catalog_system/pvt/products/GetIndexedInfo/3348"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'X-VTEX-API-AppKey' : "vtexappkey-bathbodyur-DXWXGX",
    'X-VTEX-API-AppToken' : "YTFFDKYGLKHXVRKGRBUKVPJIMKNDEGVXLJTEICZIQAFODHKESIKOFEQIJWTTWVBEOJLMYFXOCLUUKUEEZIKVVHRGSLULJFLVZAZTWYGNKWMUKWXPSOTOKFJHRETMLMEW"
    }

response = requests.request("GET", url, headers=headers)


document_file = open("xmlVtex.xml", "r") # Open a file in read-only mode
original_doc = document_file.read() # read the file object
document = minidom.parse('xmlVtex.xml')

# with open('Vtex.xml', "w") as f:
#      f.write(response.text) 
# tree = ET.parse('xmlVtex.xml', parser = ET.XMLParser(encoding = 'iso-8859-5'))

# xmltest = ET.fromstring(xml.encode("utf-8"))

# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.fromstring('xmlVtex.xml', parser=parser)
# xml    = ET.parse('xmlVtex.xml')
# root = xml.getroot()
# print(root)