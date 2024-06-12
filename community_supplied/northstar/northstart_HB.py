from __future__ import print_function
import requests
import datetime
import time
import os
#from jinja2 import Environment, FileSystemLoader
from jinja2 import Template
# Supress CLI InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

#
# user_functions
#
def generate_maitenance_json(index_number, use, maintenance_type):
    maintenance_type = maintenance_type
    current_time=datetime.datetime.utcnow().strftime("%Y%m%d%H%M")
    if use == 'for_simulation':
        name = 'created_for_simulation'
        start = 3600
        end = 6000
    else:
        name = 'Healthbot-' + maintenance_type + '-health-alert' + current_time
        start = 1
        end = 720
    maintain=Template("""
    {
        "topoObjectType": "maintenance",
        "topologyIndex": 1,
        "user": "admin",
        "name": "{{ name }}",
        "startTime": "{{ start_time }}",
        "endTime": "{{ end_time }}",
        "elements": [
            {
                "topoObjectType": "{{ maintenance_type }}",
                "index": {{ index_number }}
            }
        ]
    }
    """)

    payload = maintain.render(
        maintenance_type=maintenance_type,
        index_number=index_number,
        current_time=current_time,
        name=name,
        start_time=getTimeSeqUTC(start),
        end_time=getTimeSeqUTC(end)
    )
    return (payload)

def getTimeSeqUTC(num):
    a = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    b_start = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S')) + int(num) * 60
    dateA = str(time.strftime("%Y%m%d", time.localtime(b_start)))
    timeA = str(time.strftime("%H%M", time.localtime(b_start)))
    juniorTime = 'T'.join([dateA, timeA])
    endstr = "00"
    finalTime = ''.join([juniorTime, endstr])
    return finalTime + 'Z'


def northstar(interface_ip,**kwargs):
    print("--"*50)
    print("Northstar Probe Action Started")
    # Gloabl Variables
    username = "USERNAME"
    password = "PASSWORD"
    nsHost = "Northstar_SERVER_IP"

    base_url = "https://{server}:8443".format(server=nsHost)
    url = "https://{server}:8443/NorthStar/API/v2/tenant/1/topology/1".format(server=nsHost)

    # Request for Authorization Token
    print("--"*50)
    print("Requesting Token")
    response = requests.post(base_url+"/oauth2/token",headers={'content-type':'application/json'},json={'grant_type':'password','username':username,'password':password},auth=(username,password),verify=False)
    authData = response.json()
    authHeaders={'Authorization':"{token_type} {access_token}".format(**authData) ,'content-type':'application/json'}

    # interface_ip = "10.136.248.188"

    # Get Index Number for Link experincing delay and jitter
    print("--"*50)
    print("Getting Interface index_number")
    link_status = requests.get(url+"/links",headers=authHeaders,verify=False)
    for i in link_status.json():
      if (i['endA']['ipv4Address']['address'] == interface_ip) or (i['endZ']['ipv4Address']['address'] == interface_ip):
        rest_index_number = i['linkIndex']
        print(rest_index_number)

    # Generate MAINTENANCE JSON Payload
    print("--"*50)
    print("Genertating Payload")
    payload = generate_maitenance_json(rest_index_number, 'for_maint', 'link')
    print(payload)

    # Put Link in MAINTENANCE
    print("--"*50)
    print("Puting Link in MAINTENANCE")
    maintenances_req = requests.post(url+"/maintenances", data=payload, headers=authHeaders, verify=False)
    print(maintenances_req.json())
    print("--"*50)
    print("Northstar Probe Action Ended")
