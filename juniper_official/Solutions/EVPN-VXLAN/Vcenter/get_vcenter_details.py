import requests
import traceback
from tand_udf import MultiRows

to_avoid_tand = {}

'''
res = {
   "vm_name": ["VM1", "VM2"],
   "vm_mac": ["00:50:56:9b:77:01", "00:50:56:9b:77:02"],
   "vm_ip": ["1.1.1.1", "1.1.1.2"],
   "dc_name": ["dc1", "dc1"],
   "cluster_name": ["cl1", "cl1"],
   "host_name": ["esxi1", "esxi1"],
   "if_name": ["ge-0/0/1", "ge-0/0/2"],
}
'''

# Queries influxdb and returns vm_name vm_ip vm_mac, datacenter name, cluster name of vecnter
def get_vm_name(remote_host_name, if_name, vcenter_device_group, vcenter_device, **kwargs):
                global to_avoid_tand
    database_name = "{0}:{1}".format(vcenter_device_group, vcenter_device)
    url = "http://tsdb:8086/query?db={0}&rp={0}".format(database_name)
    params = {
        'q': 'select "datacenter", "cluster", "host-name", "name" , "mac", "ip" from "vcenter.evpn/get-vcenter-details" where "host-name" = \'{0}\' and time > now()- 5m order by desc'.format(
            remote_host_name)
    }
    response = requests.get(url=url, params=params)
    res = response.json()
    try:
        result_dict = {"vm_name": [], "vm_mac": [], "vm_ip": [], "dc_name": [],
                       "cluster_name": [], "host_name": [], "if_name": []};
        for value in res["results"][0]["series"]:
            index = 0
            for item in value["columns"]:
                if item == "name":
                    vindex = 0
                    for item in value["values"]:
                        vm_name = value["values"][vindex][index]
                        vindex += 1
                        result_dict["vm_name"].append(vm_name)
                if item == "mac":
                    vindex = 0
                    for item in value["values"]:
                        vm_mac = value["values"][vindex][index]
                        vindex += 1
                        result_dict["vm_mac"].append(vm_mac)
                if item == "ip":
                    vindex = 0
                    for item in value["values"]:
                        vm_ip = value["values"][vindex][index]
                        vindex += 1
                        result_dict["vm_ip"].append(vm_ip)
                if item == "datacenter":
                    vindex = 0
                    for item in value["values"]:
                        dc_name = value["values"][vindex][index]
                        vindex += 1
                        result_dict["dc_name"].append(dc_name)
                if item == "cluster":
                    vindex = 0
                    for item in value["values"]:
                        cluster_name = value["values"][vindex][index]
                        vindex += 1
                        result_dict["cluster_name"].append(cluster_name)
                if item == "host-name":
                    vindex = 0
                    for item in value["values"]:
                        host_name = value["values"][vindex][index]
                        vindex += 1
                        result_dict["host_name"].append(host_name)
                        result_dict["if_name"].append(if_name)
                index += 1
        rows = MultiRows()
        index = 0
        for item in range(len(result_dict["vm_name"])):
            rows.add_row()
            rows.add_tag("vm_name", result_dict["vm_name"][index])
            for f in ['vm_mac', 'vm_ip', 'dc_name', 'host_name', 'cluster_name', 'if_name']:
                if result_dict[f][index] is None:
                    f1 = "NA"
                    rows.add_field(f, f1)
                else:
                	rows.add_field(f, result_dict[f][index])
            index += 1
        return rows
    except KeyError:
    	pass