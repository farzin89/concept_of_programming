
import requests

response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")

print('in this moment, bitcoin is %i dollars' %float((response.json()['data']['amount'])))
