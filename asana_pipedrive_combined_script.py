# Asana API
import asana
from asana.rest import ApiException

#Pipedrive API
from pipedrive.client import Client

# other utilities
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

# finding a task in Pipedrive 


# locate it's counterpart in Asana


# update the latter to match the former
