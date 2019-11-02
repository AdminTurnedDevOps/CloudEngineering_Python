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