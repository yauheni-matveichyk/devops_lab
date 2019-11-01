#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import requests
import argparse
import json
import datetime

github_login = input('Enter your GitHub login:')
github_password = getpass.getpass()

parser = argparse.ArgumentParser()
parser.add_argument('--version', help='Application version.',
                    action='store_true')
parser.add_argument('--state', help='Time, Show PR, state, login',
                    action='store_true')
parser.add_argument('--week', help='Week number.', action='store_true')
parser.add_argument('--day', help='On which day of the week',
                    action='store_true')
parser.add_argument('--count', help='How many', action='store_true')
parser.add_argument('--all', help='How many', action='store_true')
args = parser.parse_args()

if args.version:
    print '0.2_UNSTABLE'
    quit()

session = requests.Session()
session.auth = (github_login, github_password)

r = session.get('https://api.github.com/repos/alenaPy/devops_lab/pulls')

data = json.loads(r.text)

ss = r.content
r.json()

# tt = json.loads(ss)

tt = r.json()

# r.status_code

if args.count:
    count = args.count
else:
    count = 25

for i in range(count):
    user = '-'
    week = '-'
    day = '-'
    state = '-'
    hours = '-'
    name = tt[i]['title']
    creation = (tt[i]['created_at'])[:10]

for item in tt:
    if args.state:
        a = item['title']
        x = item['state']
        o = item['created_at']
        y = item['user']['login']
        print ':Created at:' + o + ':Title:' + a + ':State:' + x \
            + ':Login:' + y

    if args.week:
        a = item['title']
        x = item['state']
        o = item['created_at']
        y = item['user']['login']
        week = datetime.datetime.strptime(creation, '%Y-%m-%d'
                ).isocalendar()[1]
        print 'Number of week: {0}'.format(week) + ':Created at:' + o \
            + ':Title:' + a + ':State:' + x + ':Login:' + y

    if args.day:
        a = item['title']
        x = item['state']
        o = item['created_at']
        y = item['user']['login']
        day = datetime.datetime.strptime(creation, '%Y-%m-%d'
                ).strftime('%A')
        print 'On which day of the week: {0}'.format(day) \
            + ':Created at:' + o + ':Title:' + a + ':State:' + x \
            + ':Login:' + y

    if args.all:
        a = item['title']
        x = item['state']
        o = item['created_at']
        y = item['user']['login']
        week = datetime.datetime.strptime(creation, '%Y-%m-%d'
                ).isocalendar()[1]
        day = datetime.datetime.strptime(creation, '%Y-%m-%d'
                ).strftime('%A')

        # print("On which day of the week: {0}".format(day))

        print 'Week number: {0}'.format(week) \
            + ':On which day of the week: {0}'.format(day) \
            + ':Created at:' + o + ':Title:' + a + ':State:' + x \
            + ':Login:' + y

session.close()
