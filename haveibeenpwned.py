import requests
import json

class HaveIBeenPwned():
    """Class for the haveibeenpwned.com database API"""
    def __init__(self):
        self.site = "https://haveibeenpwned.com/api/v2/breachedaccount/"

    def _get_account(self, account=""):
        """Makes the GET request to the database and returns the response
        object"""
        self.name = account
        self.url = self.site + self.name
        return requests.get(self.url)

    def check(self, account="", verbose=False):
        """Receives the account and makes the GET to the API"""
        self.name = account
        self.response = self._get_account(self.name)
        if self.response.text:
            self.jresponse = json.loads(self.response.text)
            print(self.name +  ' - PWNED')
            if verbose == True:
                print('\n{}\n'.format(self.jresponse))
            else:
                for i in range(len(self.jresponse)):
                    print('\t{}'.format(self.jresponse[i]['Name']))
        else:
            print(self.name + ' - CLEAN')

