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

'''
# Create a task
configuration = asana.Configuration()
configuration.access_token = cfg_asana['token']
api_client = asana.ApiClient(configuration)

tasks_api_instance = asana.TasksApi(api_client)
body = {"data": {"workspace": cfg_asana['gid'], "name": "Task made using POST request from Python script", "assignee": "me"}}
opts = {}

try:
    task = tasks_api_instance.create_task(body, opts)
    pprint(task)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
'''

# Update a task
# https://developers.asana.com/reference/tasks
tasks_api_instance = asana.TasksApi(api_client)
body = {"data": {"name": "Task made using POST request from Python script, updated again using a Python script",}}
task_gid = "1207766808680968"
opts = { 
    'opt_fields': "name,assignee,workspace"
}
try:
    task = tasks_api_instance.update_task(body, task_gid, opts)
    pprint(task)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)

# try marking the task as completed?
body = {"data": {"completed": True, "due_on":"2024-07-11"}}
try:
    task = tasks_api_instance.update_task(body, task_gid, opts)
    pprint(task)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)






# # Construct resource API Instance
# users_api_instance = asana.UsersApi(api_client)
# user_gid = cfg_asana['name']
# opts = {'workspace': cfg_asana['gid'] }

# try:
    # # Get your user info
    # me = users_api_instance.get_user(user_gid, opts)

    # # Print out your information
    # print(f'Hi, {me["name"]}. Welcome to your Asana example script! Here are your tasks:')
# except ApiException as e:
    # print("Exception when calling UsersApi->get_user: %s\n" % e)
    
# # get list of tasks
# tasks_api_instance = asana.TasksApi(api_client)

# try:
    # # Get multiple tasks
    # tasks = tasks_api_instance.get_tasks(opts)
    # for task in tasks:
        # pprint(task)
# except ApiException as e:
    # print("Exception when calling TasksApi->get_tasks: %s\n" % e)
    
# # try changing a field of a task?

