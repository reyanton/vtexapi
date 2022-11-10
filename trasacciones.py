import requests

url = "https://victoriassecretbeautype.myvtex.com/api/pvt/transactions/558634"

headers = {
    "Accept": "application/json; charset=utf-8",
    "X-VTEX-API-AppKey": "vtexappkey-victoriassecretbeautype-GUBDMD",
    "X-VTEX-API-AppToken": "UVLIZQPJFGJXXCVNYBXSEZKWJUAIIGOWJNQDVQUEHFXLXOHKUCTLUMVUKPZFQHBZSMOKMRRHHSKYCYZUMPNFMDCWSVTGRPNZEYTKAXYCLMEBBWSLPFSBTVMPJRRQYKQR"
}

response = requests.request("GET", url, headers=headers)

print(response.text)