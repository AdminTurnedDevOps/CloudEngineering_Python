import requests
from requests.auth import HTTPBasicAuth
import logging
import getpass

def buildAPI(uri, username):

    p = getpass.getpass(prompt='Please enter PAT token: ')

    try:
        resp = requests.get(uri, auth=HTTPBasicAuth(username, p))
        print(resp.text)
    
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    buildAPI(uri='', username='')
