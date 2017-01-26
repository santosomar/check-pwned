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
        nargs='+')
parser.add_argument(
        '-f',
        #'--file',
        metavar='<FILE>',
        help='Read accounts from file (one account per line)')
parser.add_argument(
        '-d',
        #'--database',
        help='Choose the database(s) (available \
        databases: %(choices)s).',
        nargs='+',
        choices=['haveibeenpwned', 'hackedmails'],
        metavar='<DBNAME>',
        default='haveibeenpwned')
parser.add_argument(
        '-v',
        #'--verbose',
        help='Show more information from the respose (json format)',
        action='store_true',
        default=False)
args = parser.parse_args()


if args.database.count('haveibeenpwned') > 0:
    checker = haveibeenpwned.HaveIBeenPwned()
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

if args.database.count('hackedmails') > 0:
    checker = hackedmails.HackedMails()
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
