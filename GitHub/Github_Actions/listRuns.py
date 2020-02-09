import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
import getpass
import sys
import json

password = getpass.getpass("Enter your password: ")

def listRuns(username):
    try:
        listRuns = requests.get('https://api.github.com/repos/AdminTurnedDevOps/TerraformWorkflow/actions/runs', auth=HTTPBasicAuth(username,password))
        
        if listRuns.status_code == 200:
            print('Authorization successful')
        
        if listRuns.status_code == 404:
            print('Page not found')

        if listRuns.status_code == 403:
            print('Unauthorized... please try a different password')

    except HTTPError as error:
        print(f'HTTP error {error} has occurred')
    
    j = listRuns.content
    js = json.loads(j)
    print(js['workflow_runs'])

username = sys.argv[1]

if __name__ == '__main__':
    listRuns(username)

else:
    print('Running as imported module...')
    listRuns(username)