#!/usr/bin/env python3
import requests
import traceback 

# Queries influxdb and returns vm_name
def get_vm_name(remote_host_name, vsphere_device_group, vsphere_device, db_server_ip, db_port, **kwargs):
	database_name = "{0}:{1}".format(vsphere_device_group, vsphere_device)
	url = "http://{0}:{1}/query?db={2}&rp={2}".format(db_server_ip, db_port, database_name)
	params = {
	    'q': 'select "host-name", "name" from "vcenter.evpn/get-vsphere-details" where "host-name" = \'{0}\' and time > now()- 2m order by desc'.format(remote_host_name)
	}
	response = requests.get(url=url, params=params)
	res = response.json()
	vm_name = ""
	try:
		for value in res["results"][0]["series"]:
			index = 0
			for item in value["columns"]:
				if item == "name":
					vindex = 0
					for item in value["values"]:
						vm_name = vm_name + value["values"][vindex][index] + ","
						vindex += 1
				index += 1
		return vm_name.rstrip(",")
	except KeyError:
		#print("vm_name not found")
		vm_name = "None"
		return vm_name

# Queries influxdb and returns mac_id
def get_mac_id(remote_host_name, vsphere_device_group, vsphere_device, db_server_ip, db_port, **kwargs):
	database_name = "{0}:{1}".format(vsphere_device_group, vsphere_device)
	url = "http://{0}:{1}/query?db={2}&rp={2}".format(db_server_ip, db_port, database_name)
	params = {
	    'q': 'select "host-name", "mac" from "vcenter.evpn/get-vsphere-details" where "host-name" = \'{0}\' and time > now()- 2m order by desc'.format(remote_host_name)
	}
	response = requests.get(url=url, params=params)
	res = response.json()
	mac_id = ""
	try:
		for value in res["results"][0]["series"]:
			index = 0
			for item in value["columns"]:
				if item == "mac":
					vindex = 0
					for item in value["values"]:
						mac_id = mac_id + value["values"][vindex][index] + ","
						vindex += 1
				index += 1
		return mac_id.rstrip(",")
	except KeyError:
		#print("mac_id not found")
		mac_id = "None"
		return mac_id

# Queries influxdb and returns data_center_name
def get_datacenter_name(remote_host_name, vsphere_device_group, vsphere_device, db_server_ip, db_port, **kwargs):
	database_name = "{0}:{1}".format(vsphere_device_group, vsphere_device)
	url = "http://{0}:{1}/query?db={2}&rp={2}".format(db_server_ip, db_port, database_name)
	params = {
	    'q': 'select "datacenter", "cluster", "host-name", "name" , "mac", "ip" from "vcenter.evpn/get-vsphere-details" where "host-name" = \'{0}\' order by desc limit 1'.format(remote_host_name)
	}
	response = requests.get(url=url, params=params)
	res = response.json()
	data_center_name = "None"
	try:
		for value in res["results"][0]["series"]:
			index = 0
			for item in value["columns"]:
				if item == "datacenter":
					data_center_name = value["values"][0][index]
					break
				index += 1
		if data_center_name == None:
			data_center_name = "NA"
		return data_center_name
	except KeyError:
		#print("data_center_name not found")
		return data_center_name
		
# Queries influxdb and returns cluster_name
def get_cluster_name(remote_host_name, vsphere_device_group, vsphere_device, db_server_ip, db_port, **kwargs):
	database_name = "{0}:{1}".format(vsphere_device_group, vsphere_device)
	url = "http://{0}:{1}/query?db={2}&rp={2}".format(db_server_ip, db_port, database_name)
	params = {
	    'q': 'select "datacenter", "cluster", "host-name", "name" , "mac", "ip" from "vcenter.evpn/get-vsphere-details" where "host-name" = \'{0}\' order by desc limit 1'.format(remote_host_name)
	}
	response = requests.get(url=url, params=params)
	res = response.json()
	cluster_name = "None"
	try:
		for value in res["results"][0]["series"]:
			index = 0
			for item in value["columns"]:
				if item == "cluster":
					cluster_name = value["values"][0][index]
					break
				index += 1
		if cluster_name == None:
			cluster_name = "NA"
		return cluster_name
	except KeyError:
		#print("cluster_name not found")
		return cluster_name

# Queries influxdb and returns vm_ip
def get_vm_ip(remote_host_name, vsphere_device_group, vsphere_device, db_server_ip, db_port, **kwargs):
	database_name = "{0}:{1}".format(vsphere_device_group, vsphere_device)
	vm_ip = "{0}:{1}".format(vsphere_device_group, vsphere_device)
	url = "http://{0}:{1}/query?db={2}&rp={2}".format(db_server_ip, db_port, database_name)
	params = {
	    'q': 'select "datacenter", "cluster", "host-name", "name" , "mac", "ip" from "vcenter.evpn/get-vsphere-details" where "host-name" = \'{0}\' order by desc limit 1'.format(remote_host_name)
	}
	response = requests.get(url=url, params=params)
	res = response.json()
	vm_ip = "None"
	try:	
		for value in res["results"][0]["series"]:
			index = 0
			for item in value["columns"]:
				if item == "ip":
					vm_ip = value["values"][0][index]
					break
				index += 1
		if vm_ip == None:
			vm_ip = "NA"
		return vm_ip
	except KeyError:
		#print("vm_ip not found")
		return vm_ip