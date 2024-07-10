# Asana API
import asana
from asana.rest import ApiException

#Pipedrive API
from pipedrive.client import Client

# other utilities
import sys
from pprint import pprint
from asana_pipedrive_config import *

# Asana setup
configuration = asana.Configuration()
configuration.access_token = cfg_asana['token']
api_client = asana.ApiClient(configuration)
tasks_api_instance = asana.TasksApi(api_client)

# Pipedrive setup
pd_client = Client(domain=cfg_pipedrive['domain'])
pd_client.set_api_token( cfg_pipedrive['token'] ) 

# get arguments from command line
num_args = len(sys.argv)

# the first argument is the script name
# the second argument is the Pipedrive task gid
if (num_args < 2):
    raise Exception("Not enough arguments")

search_task = sys.argv[1] # the task on Pipedrive that you want to sync with asana
pd_task = client.activities.get_activity(search_task)

# locate it's counterpart in Asana


# update the latter to match the former
