import requests
import json
from time import sleep

site = "https://haveibeenpwned.com/api/v2/breachedaccount/"

f = open('accounts.txt','rb')

for account in f:
    email =  account.decode("utf-8").rstrip()
    url = site + email
    resp = requests.get(url)
    if resp.text:
        t = json.loads(resp.text)
        print(email + ' - PWNED\n')
        print(t)
        print('\n')
    else:
        print(email + ' - CLEAN\n')
    sleep(2)
