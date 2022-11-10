import requests
from requests.auth import HTTPBasicAuth
import json


url_flow = "https://bathbody.myvtex.com/api/pvt/transactions/"
url = "https://bathbody.myvtex.com/api/oms/pvt/orders/1068440948586-01/payment-transaction" #Retrieve Payment transaction
#url_td = "https://bathbody.myvtex.com/api/pvt/transactions/" #transaction details
url_prices = "https://api.vtex.com/victoriassecretbeautypa.myvtex.com/pricing/prices/64"
url_tran = "https://bathbody.myvtex.com/admin/pci-gateway/#/transactions/1373541795CB4B318BFB25C29C9BD43E"
url_referencia = "http://10.2.0.147/api-peru/public/index.php/api/stocktarifas"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'Key' : "it@grupodavid.com",
    'Authorization' : "Bearer " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU1OTc0Nzc0ZGMxZDFkYmU2ZDFiYjRmMTk3ZjU1ZGIzYzRhMTEyM2Q3ZDBiNzYzZjg2OTA2NzEyZTNkNDEwMmUyOGE5YjdjMDVlZGYzYjU5In0.eyJhdWQiOiIxIiwianRpIjoiNTU5NzQ3NzRkYzFkMWRiZTZkMWJiNGYxOTdmNTVkYjNjNGExMTIzZDdkMGI3NjNmODY5MDY3MTJlM2Q0MTAyZTI4YTliN2MwNWVkZjNiNTkiLCJpYXQiOjE2MTE4NzI3NDAsIm5iZiI6MTYxMTg3Mjc0MCwiZXhwIjoxNjQzNDA4NzQwLCJzdWIiOiI1Iiwic2NvcGVzIjpbXX0.AKFuAbNfa-XkghDBlVbyf-HbMFy83RRKTNq11uwSclukI73-G2sermxnDmHqfDrkcNZoCOOH0qcKkumCtw6AQGBeYDY9ZY1PsXc51PzqKQPrSDIkOtLQPF6Rs7tyk6h4gDSx0hrt56QvsrAbTAycjVLAaXVA1TtbyDkhCgSiJXM319tbUqdmhcL85Lxft3-cPbXxihM3QSLFb4VFod5VsBRcax9hH34FrDl-jhInE6Cpk6U-vZkFYHcbuGVdxJpwwEdoTpfque-cOtAI2YVyc2t0QwPFjBE_8ezsRLPm_Ji4Giz0trE8JAfxT-Daa-By53SO3ItxPP9EVdlFAeN1sz8NiEkDatWVEmTzv5NcJd1vTj2SZj1E_q8Q67yYha3P4wEWN2x37xkgK-JFr1W0Kxw7-q73cuj3jaO4DOgiQr-7rWWQNOmo9MYdWjm4I6QReRpqRhcAPMgUsEWadEr48_aaVgJ4w4VasW7yRdV84OEZ_xwuiI7dBJkj5HovOm_bSAWZY4nX2pqio7d54BzpEo4OqzI-q9iRDo-VGuhctnpLlfD_ICZanONfy1PiL8uLYkXPdEBHxbkVS3M7RHxQSaVtq6emsiUdGYGzmvc-1uN30Y8k9kolyVIG-tbUyMSIp87B8BQp3QwCsZzZqDUpsaiYxQIw8UXkNx4_33Afpc4"
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
