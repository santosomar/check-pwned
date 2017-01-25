import requests
import json

class hm():
    """Class for hacked-mails.com database API"""
    def __init__(self):
        self.site="https://hacked-emails.com/api?q="

    def get_account(self, account=""):
        """Makes the GET request to the database"""
        self.name=account
        self.url = self.site + self.name
        return requests.get(self.url)

    def check(self, account=""):
        """Receives de account, call the get function and print results"""
        self.name=account
        self.response = self.get_account(self.name)
        self.jresponse = json.loads(self.response.text)
        if self.jresponse['status'] == 'found':
            print(self.name +  ' - PWNED\n')
            print(self.jresponse)
        else:
            print(self.name + ' - CLEAN')

