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
url_prices = "https://api.vtex.com/victoriassecretbeautypa.myvtex.com/pricing/prices/64"
url_tran = "https://bathbody.myvtex.com/admin/pci-gateway/#/transactions/1373541795CB4B318BFB25C29C9BD43E"
url_referencia = "https://victoriassecretbeautypa.myvtex.com/api/catalog/pvt/stockkeepingunit/692"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'X-VTEX-API-AppKey' : "vtexappkey-victoriassecretbeautypa-TUQFRY",
    'X-VTEX-API-AppToken' : "EKXHVBENZXTZINZEPFNVXLCMIBWQHFYZGBMDFAYHHPYTNYUJSOQANXISILZTFOFUYUSGAWYOHGOINJYJHMYTOYLJTUUUBEBSJEUTFNIVPBTGIZFZMPMSQMFAIJNGCENC"
    }

#response = requests.request("GET", url_prices, headers=headers, auth=HTTPBasicAuth('reinaldo.vanton@gmail.com', '*-rlp282031-*'))
response = requests.request("GET", url_referencia, headers=headers)
print(response.text)

if response.text != None and response == 200:
    json_list = json.loads(response.text)
    
    #print(json_list)
#     pay_id = json_list['payments'][0]['id']
#     tran_id = json_list['transactionId']

# url_f = url_flow + tran_id
#  #url_td = url_td + tran_id + "/payments/" + pay_id
# print(url_f)
# response_td = requests.request("GET", url_f, headers=headers)
# print(response_td)
