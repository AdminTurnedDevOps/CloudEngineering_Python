##
# For this script to work properly, you will need to authenticate with AZ CLI.
# I have found this to be the smoothest way to interact with the Python SDK. If
# you're using Azure, you're most likely already using the AZ CLI. If not, check
# it out. https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest
##

import azure.mgmt.compute as Compute
from azure.common.client_factory import get_client_from_cli_profile

import retry
import sys
import logging

@retry.retry(RuntimeError, tries=2)
def listVMs(resourceGroup):

    VM = get_client_from_cli_profile(Compute.ComputeManagementClient)

    try:
        VMs = VM.virtual_machines.list(resourceGroup)
        for vm in VMs:
            print(vm)
    
    except Exception as e:
        logging.error(e)

resourceGroup = sys.argv[1]

listVMs(resourceGroup)