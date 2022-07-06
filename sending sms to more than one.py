import requests
filename = "Desktop/API/phones"
text = """I am farzin , we sent your book if you did not recive in the next 5 days plese contact me"""

def readphones(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.string() for x in content]
    return content

def send_sms(number,text):
    api_key = '7A4F794F53557935'
    url = 'https://api.kavenegar.com/v1/%s/sms/send/.json'%(api_key)

    data ={'receptor':number,'message':text}
    r =requests.post(url,data= data)
    return r.ok

phones = readphones(filename)
for phone in phones:
    if not send_sms(phone,text):
        print(phone)

