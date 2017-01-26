import argparse
import haveibeenpwned
import hackedmails
from time import sleep

parser = argparse.ArgumentParser(
        description='Check for pwned accounts.')
#group = parser.add_mutually_exclusive_group()
parser.add_argument(
        '-a',
        #'--account',
        metavar='<ACCOUNT>',
        help='One or more email accounts (separated by spaces).',
        dest='account',
        nargs='+')
parser.add_argument(
        '-f',
        #'--file',
        metavar='<FILE>',
        dest='file',
        help='Read accounts from file (one account per line)')
parser.add_argument(
        '-d',
        #'--database',
        help='Choose the database(s) (available \
        databases: %(choices)s).',
        nargs='+',
        choices=['haveibeenpwned', 'hackedmails'],
        metavar='<DBNAME>',
        dest='database',
        default='haveibeenpwned')
parser.add_argument(
        '-p',
        #'--paste',
        help='Get the pasted leaks sources if avaible.',
        action='store_true',
        dest='paste',
        default=False)
parser.add_argument(
        '-v',
        #'--verbose',
        help='Show more information from the respose (json format)',
        action='store_true',
        dest='verbose',
        default=False)
args = parser.parse_args()


if args.database.count('haveibeenpwned') > 0:
    checker = haveibeenpwned.HaveIBeenPwned()
    print('[+]Checking in haveibeenpwned.com database.')
    if args.account:
        for a in args.account:
            checker.check(a.strip(), args.verbose, args.paste)
            sleep(1.5)

    if args.file:
        f = open(args.file, 'r')
        for a in f:
            checker.check(a.strip(), args.verbose)
            sleep(1.5)
        f.close()
    del checker

if args.database.count('hackedmails') > 0:
    checker = hackedmails.HackedMails()
    print('[+]Checking in hacked-mails.com database.')
    if args.account:
        for a in args.account:
            checker.check(a.strip(), args.verbose)
            sleep(1.5)

    if args.file:
        f = open(args.file, 'r')
        for a in f:
            checker.check(a.strip(), args.verbose)
            sleep(1.5)
        f.close()
    del checker
