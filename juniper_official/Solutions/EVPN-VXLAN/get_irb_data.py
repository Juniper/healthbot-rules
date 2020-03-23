import yamlordereddictloader
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import json
 
yaml_data = """
---
IrbRiIntefacesTable:
  rpc: get-interface-information
  args:
    interface_name: 'irb'
    routing-instance: 'all'
  item: physical-interface/logical-interface
  key: name
  view: IrbRiIntefacesView
 
IrbRiIntefacesView:
  fields:
    ip_address: (address-family/interface-address/ifa-local)[1]
    vrfname: vrfname
"""
modules = FactoryLoader().load(yaml.load(yaml_data, Loader=yamlordereddictloader.Loader))
 
def run():
    return __salt__['mine.send']('get_irb_data.get_irbs')
 
 
def get_irbs():
  stats = modules['IrbRiIntefacesTable'](dev = __proxy__['junos.conn']())
  stats.get()
  return json.loads(stats.to_json())