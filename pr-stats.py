import getpass
import requests
import argparse
import json

github_login = 'yauheni_matveichyk@epam.com'
github_password = getpass.getpass()

parser = argparse.ArgumentParser()
parser.add_argument('--version', help='Application version.',
                    action='store_true')
parser.add_argument('--state', help='Time, Show PR, state, login',
                    action='store_true')
args = parser.parse_args()

if args.version:
    print('0.1_UNSTABLE')
    quit()

session = requests.Session()
session.auth = (github_login, github_password)

r = session.get('https://api.github.com/repos/alenaPy/devops_lab/pulls')

data = json.loads(r.text)

ss = r.content
r.json()
tt = json.loads(ss)
r.status_code
for item in tt:
    if args.state:
        a = item['title']
        x = item['state']
        o = item['created_at']
        y = item['user']['login']
        print(o + ':' + a + ':' + x + ':' + y)

session.close()
