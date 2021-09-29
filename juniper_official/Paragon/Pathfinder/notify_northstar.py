#!/usr/bin/env python3
import requests
import json
import datetime
import urllib3

#NorthStar URLs
node_get_url = 'http://ns-web.northstar:3301/NorthStar/API/v2/tenant/1/topology/1/nodes?q=$.[?(@.hostName %26%26 (@.hostName == "{hostname}"))]'
link_get_url = 'http://ns-web.northstar:3301/NorthStar/API/v2/tenant/1/topology/1/links/?q=$.[?((@.endA%26%26(@.endA.node.id=="{node_id}")%26%26(@.endA.interfaceName=="{if_name}"))||(@.endZ%26%26(@.endZ.node.id=="{node_id}")%26%26(@.endZ.interfaceName=="{if_name}")))]'
link_mnt_url = 'http://ns-web.northstar:3301/NorthStar/API/v2/tenant/1/topology/1/maintenances?q=$.[?(@.elements%26%26@.elements.filter(x => x.topoObjectType == "link" %26%26 x.index=="{link_index}").length >0 )]'
mnt_url = 'http://ns-web.northstar:3301/NorthStar/API/v2/tenant/1/topology/1/maintenances'
node_mnt_url = 'http://ns-web.northstar:3301/NorthStar/API/v2/tenant/1/topology/1/maintenances?q=$.[?(@.elements%26%26@.elements.filter(x => x.topoObjectType == "node" %26%26 x.index=={node_index}).length >0 )]'
headers = {'Content-Type': 'application/json'}

#Queries the NorthStar Node ID using device hostname.     
def get_node_id(hostname, **kwargs):
    try:
        r = requests.get(node_get_url.format(hostname=hostname), headers=headers, verify=False)
        res = r.json()
        if (r.status_code == 200) and (len(res)>0):
            (node_id) = res[0]['id']
            (node_index) = res[0]['nodeIndex']
            return node_id, node_index
        else:
            raise Exception("Node doesn't exist")
    except Exception as e:
        print(e)


#Queries the NorthStar link ID using device hostname and IFD name and IFL number. 
def get_link_index(hostname, ifd_name, ifl_number, **kwargs):
    node_params = get_node_id(hostname)
    if node_params:
        node_id = node_params[0]
        try:
            r = requests.get(link_get_url.format(node_id=node_id, if_name=ifd_name +"."+ ifl_number), headers=headers, verify=False)
            res = r.json()
            if (r.status_code == 200) and (len(res)>0):
                link_index = res[0]['linkIndex']
                link_id = res[0]['id']
                return link_index, link_id
            else:
                raise Exception("Link doesn't exist")
        except Exception as e:
            print(e)
    else:
        raise Exception("Link doesn't exist")


#Queries the NorthStar link maintenance using Link ID, device hostname and IFD name and IFL number. 
def get_link_maintenances(hostname, ifd_name, ifl_number, **kwargs):
    link_params = get_link_index(hostname, ifd_name, ifl_number)
    if link_params:
        link_index = link_params[0]
        link_id = link_params[1]
        try:
            r = requests.get(link_mnt_url.format(link_index=link_index), headers=headers, verify=False)
            res = r.json()
            link_mnt_state = 0
            link_mnt_status = None
            mnt_index = 0
            if len(res) > 0:
                link_mnt_index = res[0]["elements"][0]['index']
                link_mnt_status = res[0]['status']
                mnt_index = res[0]['maintenanceIndex']
                if (link_mnt_status == "planned") or (link_mnt_status == "in progress") and (link_index == link_mnt_index):
                    link_mnt_state = 1
                else:
                    link_mnt_state = 0
            else:
                link_mnt_state = 0
            return link_index, link_id, link_mnt_state, link_mnt_status, mnt_index
        except Exception as e:
            print(e)
    else:
        raise Exception("Link doesn't exist")


# Puts link under maintenance based on failures or errors
# Inputs required are device hostname, IFD name and IFL number and maintenance time.
def generate_link_maitenance(ifd_name, ifl_number, mnt_time, hb_alert, **kwargs):
    hostname = kwargs['device_id']
    if_name = ifd_name +"."+ ifl_number
    link_params = get_link_maintenances(hostname, ifd_name, ifl_number)
    if link_params:
       link_index = link_params[0]
       link_id = link_params[1]
       link_mnt_state = link_params[2]
       link_mnt_status = link_params[3]
       if link_mnt_state == 0:
           current_time = datetime.datetime.now()
           start_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
           add_time = current_time + datetime.timedelta(days = int(mnt_time.split(":")[0]), hours = int(mnt_time.split(":")[1]), minutes = int(mnt_time.split(":")[2]))
           end_time = add_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
           simulation_payload='{"topoObjectType":"maintenance","topologyIndex":1,"elements":[{"topoObjectType":"link","index":'+str(link_index)+',"id":"'+str(link_id)+'"}],"user":"spadmin","name":"'+str("LinkMaintenanceOfLinkID:"+link_id)+'","comment":"'+str(hb_alert)+'","autocomplete": true,"startTime":"'+str(start_time)+'","endTime":"'+str(end_time)+'"}'
           try:
               r = requests.post(link_mnt_url, data=simulation_payload, headers=headers, verify=False)
               if r.status_code == 201:
                   return True
               else:
                   return False
           except Exception as e:
               print(e)
       else:
           return True
    else:
      raise Exception("Link or node doesn't exists")
    

# Deletes link under maintenances
def remove_link_maitenance(ifd_name, ifl_number, **kwargs): 
    hostname = kwargs['device_id']
    if_name = ifd_name +"."+ ifl_number
    link_params = get_link_maintenances(hostname, ifd_name, ifl_number)
    if link_params:
        mnt_index = link_params[4]
        try:
            r = requests.get(mnt_url+'/'+str(mnt_index), headers=headers, verify=False)
            res = r.json()
            if (r.status_code == 200) and (len(res)>0):
                res['status']='completed'
                c = requests.put(mnt_url+'/'+str(mnt_index), data=json.dumps(res), headers=headers, verify=False)          
                d = requests.delete(mnt_url+'/'+str(mnt_index), headers=headers, verify=False)
                if (d.status_code == 200) or (d.status_code == 204):
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
    else:
      raise Exception("Link or node doesn't exists")



# Puts node under maintenance
def generate_node_maitenance(mnt_time, hb_alert, **kwargs):
    hostname = kwargs['device_id']
    node_params = get_node_id(hostname)
    if node_params:
        node_id = node_params[0]
        node_index = node_params[1]
        current_time = datetime.datetime.now()
        start_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        add_time = current_time + datetime.timedelta(days = int(mnt_time.split(":")[0]), hours = int(mnt_time.split(":")[1]), minutes = int(mnt_time.split(":")[2]))
        end_time = add_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        simulation_payload='{"topoObjectType":"maintenance","topologyIndex":1,"elements":[{"topoObjectType":"node","index":'+str(node_index)+',"id":"'+str(node_id)+'"}],"user":"spadmin","name":"'+str("NodeMaintenanceOf"+hostname)+'","comment":"'+str(hb_alert)+'","autocomplete": true,"startTime":"'+str(start_time)+'","endTime":"'+str(end_time)+'"}'
        try: 
            r = requests.post(mnt_url, data=simulation_payload, headers=headers, verify=False)
            if r.status_code == 201:
                return True
            else:
                return False
        except Exception as e:
            print(e)
    else:
      raise Exception("Node doesn't exists")


# Removes node maintenances
def remove_node_maitenance(**kwargs): 
    hostname = kwargs['device_id']
    node_params = get_node_id(hostname)
    if node_params:
        node_id = node_params[0]
        node_index = node_params[1]
        try:
            r = requests.get(node_mnt_url.format(node_index=node_index), headers=headers, verify=False)
            res = r.json()
            if (r.status_code == 200) and (len(res)>0):
                mnt_index = res[0]['maintenanceIndex']
                res[0]['status']='completed'
                res = json.dumps(res[0])
                c = requests.put(mnt_url+'/'+str(mnt_index), data=res, headers=headers, verify=False)            
                d = requests.delete(mnt_url+'/'+str(mnt_index), headers=headers, verify=False)
                if (d.status_code == 200) or (d.status_code == 204):
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
    else:
      raise Exception("Node doesn't exists")   
