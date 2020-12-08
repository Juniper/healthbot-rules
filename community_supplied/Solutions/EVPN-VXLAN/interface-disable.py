#! /usr/bin/env python3
import requests
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

def interface_deactivate(iface,**kwargs):
  r = requests.get('http://config-server:9000/api/v2/device/%s/' % kwargs['device_id'], verify=False)
  device_info = r.json()
  hostname = device_info['host']
  userid = device_info['authentication']['password']['username']
  password = device_info['authentication']['password']['password']
  with Device(host=hostname, user=userid, passwd=password) as dev:
    conf = """
interfaces {
  /* Disabled automatically by Healthbot server after aggressive flap */
  %s {
      disable;
  }
}
"""%iface
    cu = Config(dev)
    cu.load(conf)
    cu.pdiff()
    cu.commit()
