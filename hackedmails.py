import requests
import json

class HackedMails():
    """Class for hacked-mails.com database API"""
    def __init__(self):
        self.site = "https://hacked-emails.com/api?q="

    def _get_account(self, account=""):
        """Makes the GET request to the database and returns the response
        object"""
        self.name = account
        self.url = self.site + self.name
        return requests.get(self.url)

    def check(self, account="", verbose=False):
        """Receives de account, call the get function and print results"""
        self.name = account
        self.response = self._get_account(self.name)
        self.jresponse = json.loads(self.response.text)
        if self.jresponse['status'] == 'found':
            print(self.name +  ' - PWNED\n')
            #FIX: Make it pythonic print
            if verbose == True:
                print('\n')
                print(self.jresponse)
                print('\n')
        else:
            print(self.name + ' - CLEAN')

