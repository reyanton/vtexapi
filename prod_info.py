import requests
from requests.auth import HTTPBasicAuth
import json

#url = "https://bathbody.myvtex.com/api/catalog_system/pvt/sku/stockkeepingunitbyean/667548949538"
#url = "https://bathbody.myvtex.com/api/catalog/pvt/stockkeepingunit/1089/ean"
#url = "https://bathbody.myvtex.com/api/catalog/pvt/product/1080"

#url = "https://bathbody.myvtex.com/api/catalog/pvt/stockkeepingunit/1012"

url_flow = "https://bathbody.myvtex.com/api/pvt/transactions/"
url = "https://bathbody.myvtex.com/api/oms/pvt/orders/1068440948586-01/payment-transaction" #Retrieve Payment transaction
#url_td = "https://bathbody.myvtex.com/api/pvt/transactions/" #transaction details
url_prices = "https://api.vtex.com/victoriassecretbeautygt.myvtex.com/pricing/prices/34"
url_tran = "https://bathbody.myvtex.com/admin/pci-gateway/#/transactions/1373541795CB4B318BFB25C29C9BD43E"
url_vs = "https://victoriassecretbeautype.myvtex.com/api/catalog/pvt/stockkeepingunit/1010"

url_coll = "https://victoriassecretbeautype.myvtex.com/api/catalog_system/pvt/collection/search"
url_coll_prod = "https://victoriassecretbeautype.myvtex.com/api/catalog/pvt/collection/159/products"

url_benef = "https://bathbodypar.myvtex.com/api/rnb/pvt/benefits/calculatorconfiguration"
url_benef_info = "https://victoriassecretbeautype.myvtex.com/api/rnb/pvt/calculatorconfiguration/4a2ab55f-92ea-4746-a45e-d1c545290adf"

url_index = "https://bathbody.myvtex.com/api/catalog_system/pvt/products/GetIndexedInfo/201"

url_promos = "https://victoriassecretbeautype.myvtex.com/api/rnb/pvt/benefits/calculatorconfiguration"

url_promofull = "https://victoriassecretbeautype.myvtex.com/api/rnb/pvt/calculatorconfiguration/6681811d-9f4e-4d9f-a305-bb2b1cb6aab5"

#querystring = {"page":"1","pageSize":"100"}
#querystring = {"perPage":"100"}
querystring = {"page":"2","pageSize":"15","orderByAsc":"true"}
headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'X-VTEX-API-AppKey' : "vtexappkey-victoriassecretbeautype-GUBDMD",
    'X-VTEX-API-AppToken' : "UVLIZQPJFGJXXCVNYBXSEZKWJUAIIGOWJNQDVQUEHFXLXOHKUCTLUMVUKPZFQHBZSMOKMRRHHSKYCYZUMPNFMDCWSVTGRPNZEYTKAXYCLMEBBWSLPFSBTVMPJRRQYKQR"
    }

#response = requests.request("GET", url_prices, headers=headers, auth=HTTPBasicAuth('reinaldo.vanton@gmail.com', '*-rlp282031-*'))
response = requests.request("GET", url_promofull, headers=headers)
#response = requests.request("GET", url_coll, headers=headers, params=querystring)
print(response.text)

if response.text != None :
     json_list = json.loads(response.text)
     if json_list['collections'] != []:
        print(json_list['collections'])
#     pay_id = json_list['payments'][0]['id']
#     tran_id = json_list['transactionId']

# url_f = url_flow + tran_id
#  #url_td = url_td + tran_id + "/payments/" + pay_id
# print(url_f)
# response_td = requests.request("GET", url_f, headers=headers)
# print(response_td)
