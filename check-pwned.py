import requests
import json
import argparse
from time import sleep

parser = argparse.ArgumentParser(
        description='Check for pwned accounts.')
group = parser.add_mutually_exclusive_group()
group.add_argument(
        '-a',
        '--account',
        help='An email account or a login name.')
group.add_argument(
        '-f',
        '--file',
        help='Read accounts from file (one account per line)')
parser.add_argument(
        '-d',
        '--database',
        help='Choose between the suported databases',
        choices=['haveibeenpwned', 'hibp'],
        default='hibp')
args = parser.parse_args()


def haveibeenpwned(account=None, file=None):
    site = "https://haveibeenpwned.com/api/v2/breachedaccount/"

    if account:
        email = account.rstrip()
        url = site + email
        resp = requests.get(url)
        if resp.text:
            t = json.loads(resp.text)
            print(email + ' - PWNED\n')
            print(t)
            print('\n')
        else:
            print(email + ' - CLEAN\n')

    if file:
        f = open(file, 'rb')

        for a in f:
            email = a.decode("utf-8").rstrip()
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
        f.close()

if args.database == 'hibp' or 'haveibeenpwned':
    if args.account:
        haveibeenpwned(account=args.account)

    if args.file:
        haveibeenpwned(file=args.file)
