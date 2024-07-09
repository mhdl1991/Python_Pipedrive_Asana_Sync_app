#Python Asana script
import asana
from asana.rest import ApiException
from pprint import pprint
#from miscutil import fetch_line
from asana_pipedrive_config import *

# Configure personal access token
configuration = asana.Configuration()
configuration.access_token = cfg_asana['token']
api_client = asana.ApiClient(configuration)
tasks_api_instance = asana.TasksApi(api_client)

try:    
    # Create a task
    body = {"data": {"workspace": cfg_asana['gid'], "name": "Task made using POST request from Python script Version 3", "assignee": "me"}}
    opts = {}

    task = tasks_api_instance.create_task(body, opts)
    pprint(task)
    
    # Update the task you just created
    # https://developers.asana.com/reference/tasks

    body = {"data": {"name": "Task made using POST request from Python script, updated again using a Python script",}}
    task_gid = task['gid']
    opts = { 
        'opt_fields': "name,assignee,workspace"
    }
    
    task = tasks_api_instance.update_task(body, task_gid, opts)
    pprint(task)
    
    
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
