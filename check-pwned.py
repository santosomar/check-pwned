#!/usr/bin/python
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
        nargs=1,
        help='Read accounts from file (one account per line)')
parser.add_argument(
        '-d',
        #'--database',
        help='Choose the database(s) default:haveibeenpwned. (available\
: %(choices)s).',
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

#Throws error if no account or no account file is specified
#This is required to fix behavior when running without any args
if (args.database) and not (args.account or args.file):
    parser.error('You must specify at least one account or one account file.')

#Start check for haveibeenpwned database
if 'haveibeenpwned' in args.database:
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

#Start check for hackedmails database
if 'hackedmails' in args.database:
    checker = hackedmails.HackedMails()
    print('[+]Checking in hacked-emails.com database.')
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
