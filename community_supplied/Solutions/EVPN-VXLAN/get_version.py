from __future__ import print_function
import sys
import ast
from jnpr.junos import Device
from jnpr.junos.facts import get_software_information
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree

def get_version(**kwargs):
    response = requests.get('http://config-server:9000/api/v2/config/device/%s' % kwargs['device_id'], verify=False)
    if response.status_code != 200:
        response = requests.get('http://config-server:9000/api/v2/config/device/%s?update=true' % kwargs['device_id'], verify=False)
    device_info = response.json()

    junos_host = device_info['host']
    junos_user = device_info['authentication']['password']['username']
    junos_password = device_info['authentication']['password']['password']
    print (device_info)
    
    device=Device(host=junos_host, user=junos_user, password=junos_password)
    device.open()
    device.timeout = 300
    v=get_software_information.get_facts(device)
    err_msg=''
    #check all fpc have the same junos version
    number_of_fpcs=len(device.facts["model_info"])
    print (number_of_fpcs)
    for i in range(0,number_of_fpcs):
        fpcn=list(device.facts["junos_info"].keys())[i]
        #verify all fpcs have same version
        if i >= 1:
            if prev_fpc_ver != device.facts['junos_info'][fpcn]['text']:
                err_msg="%s version is different to other fpcs/re/nodes, verify and rectify this immediately." % fpcn
                break
        prev_fpc_ver=device.facts['junos_info'][fpcn]['text']
    device.close()
    if err_msg == '':
        print (device.facts["version"])
        return device.facts["version"]
    else:
        return err_msg