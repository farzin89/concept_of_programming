import requests
def inform_Farzin(price):
    API_key =("4D599544095B75574")
    url = "https://api.kevenegar.com/v1/%s/sms/send.json" %API_key
    payload ={"receptor" :"09113857244","message":"price is as low as%i" %price}
    response = requests.post(url,data=payload)
    print(response)
my_good_price =6500

response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD",proxies={"https":"socks5://127.0.0.1:1080"})
price = float(response.json()['data']['amount'])

if (price < my_good_price):
    inform_Farzin()

