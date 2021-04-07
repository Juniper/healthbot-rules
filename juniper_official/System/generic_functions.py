import sys
import requests
from jnpr.junos.device import Device
 
 
####################################
#          UDFs                    #
####################################
# Get the hostname of the device
def get_hostname(**kwargs):
    device_info = get_device_info_healthbot(**kwargs)
    return device_info['facts']['hostname']
 
 
# Get the model of the device
def get_model(**kwargs):
    device_info = get_device_info_healthbot(**kwargs)
    return device_info['facts']['platform']
 
 
# Get the version of device
def get_version(**kwargs):
    device_info = get_device_info_healthbot(**kwargs)
    return  device_info['facts']['release']
 
 
# Get the version of RE0 of the device if present
def get_version_RE0(**kwargs):
    device_details = get_device_info(**kwargs)
    with connect_to_device(**device_details) as dev:
        return dev.facts['version_RE0']
 
 
# Get the version of RE1 of the device if present
def get_version_RE1(**kwargs):
    device_details = get_device_info(**kwargs)
    with connect_to_device(**device_details) as dev:
        return dev.facts['version_RE1']
 
 
# Get the version of RE0 of the device if present
def get_re_master(**kwargs):
    device_details = get_device_info(**kwargs)
    with connect_to_device(**device_details) as dev:
        return dev.facts['re_master']['default']
 
 
# Get the serrial number of the device
def get_serial_no(**kwargs):
    device_info = get_device_info_healthbot(**kwargs)
    return device_info['facts']['serial-number']
 
 
# Get the configuration of the device in string
def get_config(**kwargs):
    device_details = get_device_info(**kwargs)
    with connect_to_device(**device_details) as dev:
        return dev.rpc.get_config(options={'format':'json'})
 
 
# subtract function
def difference(num1,num2, **kwargs):
    try:
        return (int(num1)-int(num2))
    except Exception:
        print("Hit Exception, invalid arg type")
 
 
# Calculate the percentage
def decimal_to_percent(numerator,denominator, **kwargs):
    if denominator == 0:
        round_percent = 0
    else:
        percent = (numerator/denominator)*100
        round_percent = round(percent,3)
    return round_percent
 
 
# Change the percentage to decimal
def percent_to_decimal(percentage, **kwargs):
    return percentage/100
 
 
# convert bytes to kilobytes
def bytes_to_kb(bytes, **kwargs):
    return bytes/(10**3)
 
 
# convert bytes to megabytes
def bytes_to_mb(bytes, **kwargs):
    bytes = int(bytes)
    return bytes/(10**6)
 
 
# convert bytes to gigabytes
def bytes_to_gb(bytes, **kwargs):
    return bytes/(10**9)
 
 
# convert bytes to gigabytes
def mb_to_bytes(mb, **kwargs):
    return mb*(10**6)
 
 
# convert megabytes to gigabytes
def mb_to_gb(mb, **kwargs):
    return mb/(10**3)
 
 
# convert gigabytes to bytes
def gb_to_bytes(gb, **kwargs):
    return gb*(10**9)
 
 
# convert bytes to megabytes
def gb_to_mb(gb, **kwargs):
    return gb*(10**6)
 
 
# Bytes per second conversion
def octets_to_bytes_per_second(intf_name, octets, ifl_id = None, **kwargs):
    intf_name_ifl_id = ""
    if ifl_id is None:
        intf_name_ifl_id = intf_name
    else:
        intf_name_ifl_id = intf_name + ifl_id
 
    # Get previous values
    if 'hb_store' not in kwargs:
       kwargs['hb_store'] = {
            'prev_value': dict(),
            'prev_time': dict(),
            'prev_bps': dict()
        }
    else:
        if 'prev_value' not in kwargs['hb_store']:
            kwargs['hb_store']['prev_value'] = dict()
        if 'prev_time' not in kwargs['hb_store']:
            kwargs['hb_store']['prev_time'] = dict()
        if 'prev_bps' not in kwargs['hb_store']:
            kwargs['hb_store']['prev_bps'] = dict()
    prev_value = kwargs['hb_store']['prev_value']
    prev_time = kwargs['hb_store']['prev_time']
    prev_bps = kwargs['hb_store']['prev_bps']
 
    # get present time
    cur_time = kwargs.get('point_time', 0)
 
    octets = int(octets)
 
    # convert octets to bytes
    cur_value = octets
    # Calculate time difference between previous and present point
    time_difference = (cur_time - prev_time.get(intf_name_ifl_id, 0))
    # Calculate data sent in bps
    try:
        bps = (cur_value - prev_value.get(intf_name_ifl_id, 0)) / time_difference
    except Exception:
        print("Hit Exception", file=sys.stderr)
        bps = prev_bps.get(intf_name_ifl_id, 0)
 
    # update global values
    prev_value[intf_name_ifl_id] = cur_value
    prev_time[intf_name_ifl_id] = cur_time
    prev_bps[intf_name_ifl_id] = bps
    return bps
 
# bps functrion is renamed as octets_to_bytes_per_second
# The following mapping is used for backward compatibility
# This line will be removed after 3 releases
bps = octets_to_bytes_per_second
 
# megabytes per second conversion
def mbps(intf_name, octets, ifl_id = None, **kwargs):
    bbps = bps(intf_name, octets, ifl_id, **kwargs)
    mbps = bbps/1000000
    return mbps
 
 
# kilobytes per second conversion
def kbps(intf_name, octets, ifl_id = None, **kwargs):
    bbps = bps(intf_name, octets, ifl_id, **kwargs)
    kbps = bbps/1000
    return kbps
 
 
# gigabytes per second conversion
def gbps(intf_name, octets, ifl_id = None, **kwargs):
    bbps = bps(intf_name, octets, ifl_id, **kwargs)
    gbps = (bbps/1000000000)
    return gbps
 
 
# Bytes transfered in an interval
def bytes(intf_name, octets, ifl_id = None, **kwargs):
    intf_name_ifl_id = ""
    if ifl_id is None:
        intf_name_ifl_id = intf_name
    else:
        intf_name_ifl_id = intf_name + ifl_id
 
    # Get previous values
    if 'hb_store' not in kwargs:
        kwargs['hb_store'] = {
            'prev_value': dict()
        }
    else:
        if 'prev_value' not in kwargs['hb_store']:
            kwargs['hb_store']['prev_value'] = dict()
    prev_value = kwargs['hb_store']['prev_value']
 
    octets = int(octets)
 
    # convert octets to bytes
    cur_value = octets
    try:
        bytes_send = (cur_value - prev_value.get(intf_name_ifl_id, 0))
    except Exception:
        print("Hit Exception", file=sys.stderr)
        bytes_send = prev_bps.get(intf_name_ifl_id, 0)
 
    # update global values
    prev_value[intf_name_ifl_id] = cur_value
    return bytes_send
 
 
# kilobytes transfered in an interval
def kilo_bytes(intf_name, octets, ifl_id = None, **kwargs):
    bytes_send = bytes(intf_name, octets, ifl_id, **kwargs)
    kilobytes_send = bytes_send/1000
    return kilobytes_send
 
 
# megabytes transfered in an interval
def mega_bytes(intf_name, octets, ifl_id = None, **kwargs):
    bytes_send = bytes(intf_name, octets, ifl_id, **kwargs)
    megabytes_send = bytes_send/1000000
    return megabytes_send
 
 
# gigabytes transfered in an interval
def giga_bytes(intf_name, octets, ifl_id = None, **kwargs):
    bytes_send = bytes(intf_name, octets, ifl_id, **kwargs)
    gigabytes_send = bytes_send/1000000000
    return gigabytes_send
 
 
# generic function to find the difference between current and previous values
# usage: key_name is mandatory to store the previous value
#        sub_key_name is optional can be used in case of multiple keys
def value_diff(key_name, value, sub_key_name = None, **kwargs):
    key_sub_key_name = ""
    if sub_key_name is None:
        key_sub_key_name = key_name
    else:
        key_sub_key_name = key_name + "." + sub_key_name
 
    if 'hb_store' not in kwargs:
        kwargs['hb_store'] = {
            'prev_value': dict()
        }
    else:
        if 'prev_value' not in kwargs['hb_store']:
            kwargs['hb_store']['prev_value'] = dict()
    prev_value = kwargs['hb_store']['prev_value']
 
    curr_value = int(value)
    val_diff = curr_value - prev_value.get(key_sub_key_name, 0)
 
    # update global values
    prev_value[key_sub_key_name] = curr_value
    return val_diff
 
 
####################################
#          UDAs                    #
####################################
# Restart the Fpc of device
# input FPC slot Number
def restart_fpc(fpc_slot, **kwargs):
    device_details = get_device_info(**kwargs)
    dev = connect_to_device(**device_details)
    response = dev.rpc.request_chassis_fpc(restart = True, slot = fpc_slot)
    dev.close()
    return response
 
 
# Bring the Fpc online of device
# input FPC slot Number
def online_fpc(fpc_slot, **kwargs):
    device_details = get_device_info(**kwargs)
    dev=connect_to_device(**device_details)
    response = dev.rpc.request_chassis_fpc(online = True, slot = fpc_slot)
    dev.close()
    return response
 
 
# Bring the Fpc offline of device
# input FPC slot Number
def offline_fpc(fpc_slot, **kwargs):
    device_details = get_device_info(**kwargs)
    dev = connect_to_device(**device_details)
    response = dev.rpc.request_chassis_fpc(offline = True, slot = fpc_slot)
    dev.close()
    return response
 
 
# Bring the pic online of specific fpc of device
# input FPC slot Number and pic slot number
def online_pic(fpc_slot, pic_slot, **kwargs):
    device_details = get_device_info(**kwargs)
    dev = connect_to_device(**device_details)
    response = dev.rpc.request_chassis_pic(online = True,fpc_slot = fpc_slot, pic_slot = pic_slot)
    dev.close()
    return response
 
 
# Bring the pic offline of specific fpc of device
# input FPC slot Number and pic slot number
def offline_pic(fpc_slot, pic_slot, **kwargs):
    device_details = get_device_info(**kwargs)
    dev = connect_to_device(**device_details)
    response = dev.rpc.request_chassis_pic(offline = True, fpc_slot = fpc_slot, pic_slot = pic_slot)
    dev.close()
    return response
 
 
# Restart The device
def reboot_system(**kwargs):
            device_details = get_device_info(**kwargs)
            dev = connect_to_device(**device_details)
            response = dev.rpc.request_reboot()
            dev.close()
            return response
 
 
# Restart both the RE's
def reboot_both_routing_engines(**kwargs):
    device_details = get_device_info(**kwargs)
    dev = connect_to_device(**device_details)
    response = dev.rpc.request_reboot(both_routing_engines = True)
    dev.close()
    return response
 
 
# Restart the other RE's
def reboot_other_routing_engine(**kwargs):
    device_details = get_device_info(**kwargs)
    dev = connect_to_device(**device_details)
    response = dev.rpc.request_reboot(other_routing_engine = True)
    dev.close()
    return response
 
 
# Helper Functions
def get_device_info(**kwargs):
    response = requests.get('http://config-server:9000/api/v2/config/device/%s/' % kwargs['device_id'], verify=False)
    if response.status_code != 200:
        return False
    device_info = response.json()
    device_details = dict()
    device_details['hostname'] = device_info['host']
    device_details['user'] = device_info['authentication']['password']['username']
    device_details['password'] = device_info['authentication']['password']['password']
    return device_details
 
 
def get_device_info_healthbot(**kwargs):
    response = requests.get('http://config-server:9000/api/v2/config/device/%s/facts' % kwargs['device_id'], verify=False)
    if response.status_code != 200:
        response = requests.get('http://config-server:9000/api/v2/config/device/%s/facts?update=true' % kwargs['device_id'], verify=False)
    device_info = response.json()
    if len(device_info['facts']) == 0:
        response = requests.get('http://config-server:9000/api/v2/config/device/%s/facts?update=true' % kwargs['device_id'], verify=False)
        device_info=response.json()
    return device_info
 
 
def connect_to_device(hostname=None, user = None, password = None):
    dev = Device(hostname, user=user, password=password, normalize=True)
    dev.open(timeout=300)
    return dev
