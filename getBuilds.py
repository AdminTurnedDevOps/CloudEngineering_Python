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

buildAPI(uri='https://vsrm.dev.azure.com/adminturneddevops/AzureDevOpsRecipes/_apis/release/definitions/?api-version=5.1', username='mlevan1992@outlook.com')