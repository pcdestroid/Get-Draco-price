import requests
headers = {}
response = requests.post('https://api.mir4global.com/wallet/prices/draco/daily', headers=headers)
x = response.json()
print(x.get('Data')[len(x.get('Data')) - 1].get('USDDracoRate'))