import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
import getpass
import sys
import json

password = getpass.getpass("Enter your password: ")

def listRuns(project, repo, username):
    try:
        listRuns = requests.get(f'https://api.github.com/repos/{project}/{repo}/actions/runs', auth=HTTPBasicAuth(username,password))
        
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

project = sys.argv[1]
repo = sys.argv[2]
username = sys.argv[3]

if __name__ == '__main__':
    listRuns(project, repo, username)

else:
    print('Running as imported module...')
    listRuns(project, repo, username)