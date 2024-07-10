# Asana API
import asana
from asana.rest import ApiException

#Pipedrive API
from pipedrive.client import Client

# other utilities
import sys
from pprint import pprint

# this is a file I've made
from asana_pipedrive_config import *

try: 
    # get arguments from command line
    num_args = len(sys.argv)

    # the first argument is the script name
    # the second argument is the Pipedrive task gid
    if (num_args < 2):
        raise Exception("Not enough arguments")

    # Asana connection setup
    configuration = asana.Configuration()
    configuration.access_token = cfg_asana['token']
    asana_client = asana.ApiClient(configuration)
    asana_tasks_api_instance = asana.TasksApi(api_client)

    # Pipedrive connection setup
    pd_client = Client(domain=cfg_pipedrive['domain'])
    pd_client.set_api_token( cfg_pipedrive['token'] ) 

    # the task on Pipedrive that you want to sync with asana
    search_task = sys.argv[1] 
    pd_task = pd_client.activities.get_activity(search_task)
    
    # Pipedrive task name
    pd_task_name = pd_task['data']['title']

    # locate it's counterpart in Asana
    opts = { 'workspace': cfg_asana['gid'] }
    asana_tasks_list = asana_tasks_api_instance.get_tasks(opts)

    # look for a matching name?
    for task in asana_tasks_list:
        asana_task_name = task['data']['name']
        if asana_task_name == pd_task_name:
            # sync task details
            
            pass
        
    
    
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)

except Exception as e:
    print("Exception: %s\n" % e)