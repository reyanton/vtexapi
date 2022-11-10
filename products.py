import requests
import json
import VtexAPI as Vtex
import pandas as pd

url = "https://bathbody.myvtex.com/api/catalog_system/pvt/sku/stockkeepingunitids?"

#querystring = {"categoryId":"4","_from":"1","_to":"30"}

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'X-VTEX-API-AppKey' : "vtexappkey-bathbody-DZKCBN",
    'X-VTEX-API-AppToken' : "WMADGGFOYDQEDDVGUYXZMQPGQATUPXPJHMDAVXQPGEQBIGGIKJBAVFTGWTNFMKYBOHWRAUKXIISIZNYJUKKGVONBSXDBJKCWFONAJOIPYESNNKGJVELCASFZUVYCQJNY"
    }

prod_list = list()
page = 1

while True:
    strPages = "page=" + str(page) + "&pagesize=100"
    urlprod = url + strPages
    
    responselist = requests.request("GET", urlprod, headers=headers)
    try:
        jsonlist = json.loads(responselist.text)
    except:
        break

    if jsonlist == []: break

    for item in jsonlist:
        prod_list.append(item)

    page = page + 1

   
i = 1
prod_stock = list()

for item in prod_list:
    json_stock = Vtex.get_stock_details(str(item), "1_1")
    json_prod_det = Vtex.get_product_details(str(item))
    
    prod_stock.append((item,
                json_prod_det["RefId"],
                json_prod_det["Name"],
                json_prod_det["IsActive"],
                json_stock[0]["totalQuantity"],
                json_stock[0]["reservedQuantity"],
                json_stock[0]["availableQuantity"]
                    ))
    if i == 10:break
    i = i + 1


df = pd.DataFrame.from_records(prod_stock, columns =['ProdId', 'EAN', 'Name', 'Active', 'Stock', 'Reserved', 'Available'])

print(df)

