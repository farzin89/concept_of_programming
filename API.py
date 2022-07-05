
import requests
import time

def inform_farzin():
    print("hi there,price is good")

def inform_farzin2():
    print('price is not good')

my_good_price = 19559

response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")
price = float(response.json()['data']['amount'])
print('at this moment, bitcoin is %i dollars' %price)
while True :
    if (price < my_good_price):
        inform_farzin()
    else :
        inform_farzin2()
    time.sleep(4)

