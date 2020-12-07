from __future__ import print_function
import re, sys, requests
from jnpr.junos.device import Device
from jnpr.junos.utils.config import Config


def get_vlan(message, **kwargs):
    # Get previous values
    temp = re.search(r'set vlans v(\d+) vxlan vni (\d+)', message)
    vlan_num = int(temp.group(1))
    return vlan_num

def get_vni(message, **kwargs):
    # Get previous values
    temp = re.search(r'set vlans v(\d+) vxlan vni (\d+)', message)
    vni_num = int(temp.group(2))
    return vni_num

def get_vlan_vni(message, **kwargs):
    # Get previous values
    temp = re.search(r'set vlans v(\d+) vxlan vni (\d+)', message)
    vni_num = int(temp.group(2))
    vlan_num = int(temp.group(1))
    print(kwargs, file=sys.stderr)
    r = requests.get('http://config-server:9000/api/v1/device-group/%s/'% kwargs['device_group'], verify=False)
    #print(r.status_code, file=sys.stderr)
    if r.status_code != 200:
        return False
    device_group_info = r.json()
    devices_list = device_group_info['devices']
    d = requests.get('http://config-server:9000/api/v1/device/%s/' % kwargs['device_id'], verify=False)
    if d.status_code != 200:
        return False
    device_info = d.json()
    device_name = device_info['device-id']
    for dev in devices_list:
        if dev!= device_name:
            rd = requests.get('http://config-server:9000/api/v1/device/%s/' %dev, verify=False)
            if r.status_code != 200:
                return False
            devices_info = rd.json()
            hostname = devices_info['host']
            userid = devices_info['authentication']['password']['username']
            password = devices_info['authentication']['password']['password']
            dev = Device(host=hostname, user=userid, password=password, normalize=True)
            dev.open()
            sw = dev.cli("show vlans v%s" %vlan_num, warning=False)
            try:
                tmp = re.search(r'default-switch\s+v(\d*)\s+', sw)
                vlan = int(tmp.group(1))
            except:
                vlan = None
            print(vlan)
            if (vlan is vlan_num):
                print("VNI configuration exists")
            else:
                cu = Config(dev)
                config = """
                set vlans v{0} vlan-id {0}               
                set vlans v{0} vxlan vni {1}
                set vlans v{0} l3-interface irb.{0}
                set vlans v{0} description "Tenant_1 - brdige domain id {0}"
                set protocols evpn extended-vni-list {1}
                set policy-options policy-statement OVERLAY-IMPORT term vni-Tenant_1-v{0} from community com-vni-Tenant_1-v{0}
                set policy-options policy-statement OVERLAY-IMPORT term vni-Tenant_1-v{0} then accept
                set policy-options community com-vni-Tenant_1-v{0} members target:1:{0}
                set policy-options policy-statement TENANT_1-EXPORT term vni-Tenant_1-v{0} then community add com-vni-Tenant_1-v{0}
                set policy-options policy-statement TENANT_1-EXPORT term vni-Tenant_1-v{0} then accept
                set policy-options policy-statement TENANT_1-EXPORT term vni-Tenant_1-v{0} from interface irb.{0}
                set policy-options policy-statement TENANT_1-IMPORT term vni-Tenant_1-v{0} from community com-vni-Tenant_1-v{0}
                set policy-options policy-statement TENANT_1-IMPORT term vni-Tenant_1-v{0} then accept
                """.format(vlan_num, vni_num)
                cu.load(config, format='set')
                if cu.commit_check():
                    res = cu.commit()
                    print("Added config")
                else:
                    print("commit check failed")
                    return False
        else:
            print("Local device")
    return True
