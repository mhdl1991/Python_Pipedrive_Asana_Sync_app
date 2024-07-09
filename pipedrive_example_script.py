# API wrapper for Pipedrive written in Python
from pipedrive.client import Client
from pprint import pprint
from asana_pipedrive_config import *

# API Token for Pipedrive
pd_client = Client(domain=cfg_pipedrive['domain'])
pd_client.set_api_token( cfg_pipedrive['token'] ) 

'''
#   When you click on a task in your list in PD, you get a URL that looks like this
#   https://r-eco.pipedrive.com/activities/list/user/13344852?selected=30551&tab=activity
#   13344852 in this case is the User ID
#   30551 is the Activity ID
'''
'''
try:
    response = pd_client.activities.get_all_activities()

    for activity in response:
        pprint(activity)
        pprint(response[activity])
        
except ApiException as e:
    print("Exception when calling get_all_activities: %s\n" % e)
''' 
    
# Activity Fields in Pipedrive
# https://developers.pipedrive.com/docs/api/v1/ActivityFields#getActivityFields

# add an activity:
'''
data = {
    'subject': 'Another Test Task made using Pipedrive',
    'type': 'task'
}
response = pd_client.activities.create_activity(data)
'''
# update an activity:
try:
    data = {
        'subject': 'Updating a task using a Python Script',
        'done': 1
    }
    response = pd_client.activities.update_activity('30970', data)

except Exception as e:
    print("Exception: %s\n" % e)
