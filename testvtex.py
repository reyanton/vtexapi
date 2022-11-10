from vtex import Vtex

client = Vtex(account_name, environment, app_key, app_token)
result = client.logistics.get_all_carriers()
js = result.json
status_code = result.status_code