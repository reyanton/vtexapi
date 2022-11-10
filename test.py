import requests


headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'X-VTEX-API-AppKey' : "vtexappkey-victoriassecretbeautype-GUBDMD",
    'X-VTEX-API-AppToken' : "UVLIZQPJFGJXXCVNYBXSEZKWJUAIIGOWJNQDVQUEHFXLXOHKUCTLUMVUKPZFQHBZSMOKMRRHHSKYCYZUMPNFMDCWSVTGRPNZEYTKAXYCLMEBBWSLPFSBTVMPJRRQYKQR"
    }

url = "https://victoriassecretbeautype.myvtex.com/api/catalog/pvt/stockkeepingunit/202/file"

response = requests.request("GET", url, headers=headers)

print(response.text)