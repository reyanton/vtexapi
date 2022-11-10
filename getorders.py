import platform
import requests
import json
import pandas as pd
from datetime import datetime, timedelta, timezone
import timezone as tz
import getconfigdata as conn_data
import send_email as sm

dia = datetime.now()
os = platform.system()

conn_data.dataconnection("localhost", "root","*Mysql2019*","ecompam")
listconfig = json.loads(conn_data.getdataconfig())
appkey = listconfig[0][1]
apptoken = listconfig[1][1]
vtex_url = listconfig[2][1]

if os == 'Windows': file_path = listconfig[3][1]
else: file_path = listconfig[4][1]

file_name_excel = file_path + dia.strftime("%Y%m%d-%H%M%S") + ".xlsx"

dia = dia - timedelta(days=1) #Fecha de busqueda
strDia = dia.strftime("%Y/%m/%d") 
strFechas = tz.asignar_time(strDia,strDia)
strRango = "creationDate:[" + strFechas + "]"

urllistord = vtex_url + "/oms/pvt/orders?per_page=100&page="
urlord = vtex_url +  "/oms/pvt/orders"
querystring =  {"f_creationDate":strRango}
headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'X-VTEX-API-AppKey' : appkey,
    'X-VTEX-API-AppToken' : apptoken
    }

list_orders = []
orders_det = []
totorders = 0
countorders = 0
numpag = 0
pag = 0

while True:
    urllist = urllistord + str(pag+1)
    
    if numpag != 0 and numpag == pag: break
    
    responselist = requests.request("GET", urllist, headers=headers, params=querystring)
    
    jsonlist = json.loads(responselist.text)
    #print(jsonlist)
    if numpag == 0: 
        numpag = int(jsonlist['paging']['pages'])
    
    for item in jsonlist['list']:
        #if item['status'] == 'canceled':
        list_orders.append(item['orderId'])

    pag = pag + 1

for lst in list_orders:
    urlorder = urlord + "/" + lst
    
    responseorder = requests.request("GET", urlorder, headers=headers, params=querystring)
    #print(responseorder.text)
    jsonorder = json.loads(responseorder.text)
    localdate = datetime.strptime(jsonorder['creationDate'][:10] + ' ' + jsonorder['creationDate'][11:19], '%Y-%m-%d %H:%M:%S') - timedelta(hours=5) 
    localdate = datetime.strftime(localdate, '%Y-%m-%d %H:%M:%S')
    orders_det.append((lst, 
        localdate,
        jsonorder['statusDescription'],
        (float(jsonorder['value'])/100),
        jsonorder['clientProfileData']['firstName'] + ' ' + jsonorder['clientProfileData']['lastName'],
        jsonorder['paymentData']['transactions'][0]['payments'][0]['paymentSystemName'],
        jsonorder['paymentData']['transactions'][0]['payments'][0]['firstDigits'] + '****' + jsonorder['paymentData']['transactions'][0]['payments'][0]['lastDigits'],
        jsonorder['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['nsu']
        ))
    
    'print(float(jsonorder['totals'][2]['value']/100))

    totorders = totorders + (float(jsonorder['value'])/100)
    countorders = countorders + 1
    
df = pd.DataFrame.from_records(orders_det, columns =['OrderId', 'Fecha', 'Estatus', 'Monto', 'Cliente', 'Pago','Tarjeta','Transacción']) 
df.to_excel (file_name_excel, index = False, header=True)

#sm.data_mail(file_name_excel, "reinaldovillarroel@grupodavid.com;pedromartinez@grupodavid.com;johanaruiz@grupodavid.com;histriadelahoz@grupodavid.com", dia.strftime("%d-%m-%Y"))

print(df)
print("total : ", totorders)
print("#ordenes : ", countorders)
