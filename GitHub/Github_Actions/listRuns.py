import requests
from requests.auth import HTTPBasicAuth
import getpass

password = getpass.getpass("Enter your password: ")

listRuns = requests.get('https://api.github.com/repos/AdminTurnedDevOps/TerraformWorkflow/actions/runs', auth=HTTPBasicAuth('mlevan1992@gmail.com',password))
print(listRuns.status_code)
print(listRuns.content)