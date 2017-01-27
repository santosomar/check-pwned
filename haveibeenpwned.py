import requests
import json
from pprint import pprint

class HaveIBeenPwned():
    """Class for the haveibeenpwned.com database API"""
    def __init__(self):
        self.breach_url = "https://haveibeenpwned.com/api/v2/breachedaccount/"
        self.paste_url = "https://haveibeenpwned.com/api/v2/pasteaccount/"

    def _get_breach(self):
        """Makes the GET request to the database and returns the response
        object"""
        self.url = self.breach_url + self.name
        return requests.get(self.url)
    
    def _get_paste(self):
        """Method to get the pasted leaks source form this database"""
        self.url = self.paste_url + self.name
        return requests.get(self.url)

    def _output_response(self):
        """Outputs the response in a nice manner, using the varibles from the
        check() function"""
        if self.response.text:
            self.jresponse = json.loads(self.response.text)
            print('\n' + self.name +  ' - PWNED')
            if self.verbose == True:
                pprint(self.jresponse)
            elif self.jresponse[0].get('Name'):
                for i in range(len(self.jresponse)):
                    print('\t{}'.format(self.jresponse[i]['Name']))
            elif self.jresponse[0].get('Source'):
                for i in range(len(self.jresponse)):
                    print('\t{} - [PASTE SITE URL]/{}'
                            .format(self.jresponse[i]['Source'],
                                    self.jresponse[i]['Id']))
        else:
            print('\n' + self.name + ' - CLEAN')

        
    def check(self, account="", verbose=False, paste=False):
        """Receives the account and makes the GET to the API"""
        self.name = account
        self.verbose = verbose

        #Check for breached account
        if self.name:
            self.response = self._get_breach()
            self._output_response()

        #Check for paste links
        if paste == True and self.response.status_code == 200:
            self.response = self._get_paste()
            if self.response.status_code == 200:
                self._output_response()
            else:
                print('\nNo leaked pastes found.')

