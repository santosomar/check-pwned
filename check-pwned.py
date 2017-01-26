import argparse
import haveibeenpwned
import hackedmails
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
        nargs='+',
        choices=['haveibeenpwned', 'hackedmails'],
        default='haveibeenpwned')
args = parser.parse_args()


if args.database.count('haveibeenpwned') > 0:
    checker = haveibeenpwned.HaveIBeenPwned()
    if args.account:
        checker.check(args.account.rstrip())

    if args.file:
        f = open(args.file, 'r')
        for a in f:
            checker.check(a.rstrip())
            sleep(2)
        f.close()
    del checker

if args.database.count('hackedmails') > 0:
    checker = hackedmails.HackedMails()
    if args.account:
        checker.check(args.account.rstrip())

    if args.file:
        f = open(args.file, 'r')
        for a in f:
            checker.check(a.rstrip())
            sleep(2)
        f.close()
    del checker
