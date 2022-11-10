import requests
import pyodbc 
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ING-ICG5;'
                      'Database=TESTPAVSECOM;'
                      'Trusted_Connection=yes;')


url = "https://api.vtex.com/victoriassecretbeautyar/pricing/prices/4"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'X-VTEX-API-AppKey' : "vtexappkey-victoriassecretbeautyar-JNQSFS",
    'X-VTEX-API-AppToken' : "YRANKKORVOXQMPGRGCMHMAACTYHHERYQPXKAMDQEXBMSVFNIHSNSIVNXRYTLCGMEQHBOFFEDLIJLOIGOKZALDFHTKMJOKFBQOIBODYDBOKHZLCJISEADGAALZHESVPTG"
    }


payload = {
    
    "listPrice": 800,
    "basePrice": 800,
    "costPrice": 800,
    
}

df = pd.read_sql_query("SELECT refproveedor, pbruto FROM vwstockarticulos where fechamodificado >= '20211201' and idtarifav = 58 and codalmacen = 'EB1'", conn)
print(df)

for i in range(len(df)) :
    skuid = df.loc[i, "refproveedor"]
    pbruto =  df.loc[i, "pbruto"]

    dfsql = pd.DataFrame([[pbruto, pbruto, pbruto]],columns=['lisprice','baseprice','costprice'])
    data = dfsql.to_json(orient='records')
    print(data)

# response = requests.request("PUT", url, json=payload, headers=headers)

# print(response.text)