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
        """Receives the account, call the get function and print results"""
        self.name = account
        self.response = self._get_account(self.name)
        self.jresponse = json.loads(self.response.text)
        if self.jresponse['status'] == 'found':
            print(self.name +  ' - PWNED')
            if verbose == True:
                print('\n{}\n'.format(self.jresponse))
            else:
               for i in range(len(self.jresponse['data'])):
                   print('\t{}'.format(self.jresponse['data'][i]['title']))
        else:
            print(self.name + ' - CLEAN')

