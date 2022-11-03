"""
Updates the arguments required for rule jflow.stats/inline-stats
the python function extracts the target fpc, pfe instance and protocol family 
for which the stats are to be fetched
"""

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import json
from jnpr.junos.factory import loadyaml
from pprint import pprint


InstanceTableYml = """
---
SampleInstanceTable:
    command: show jnh {{ instance }} sample-inline instance-table
    target: NULL
    key: Index
    args:
        instance: NULL
    view: _instanceTableView

_instanceTableView:
    columns:
        index: Index
        tbl_size: 
            - Flow
            - Tbl size
        timeout:
            - Active/Inactive
            - Timeout (sec)
        type:
            - Template
            - Type
        version:
           - Export
           - Version
        num_coll: Collectors#

pfeInst:
    command: show pfe id info
    target: Null
    title: 'PFE instance details:'
    key: 'PFE-ID'
    view: _instView

_instView:
    columns:
        pfe_id: 'PFE-ID'
        down-flag: 'Down-Flags'

"""

def func(fpc, dev, ret):
    table = {}
    inst = pfeInst(dev)
    pfe_inst=inst.get(target = fpc)
    for inst_key in list(pfe_inst.keys()):
        pfe_inst_table = {}
        a_dict = {}
        pfe_inst_table = pfe_inst[inst_key]
        pinst = pfe_inst_table['pfe_id']
        a_dict['instance']= str(pinst) 
        globals().update(FactoryLoader().load(yaml.load(InstanceTableYml, Loader=yaml.FullLoader)))
        sample= SampleInstanceTable(dev)
        s1=sample.get(target=fpc, args=a_dict)
        for key in list(s1.keys()):
            index_dict = {}
            template_dict = {}
            table = s1[key]
            instance = pinst
    
    
    #extract template type for inline stats details
            for j in table:
                arg_dict = {}
                template_dict['target'] = fpc
                arg_dict['instance'] = instance
                
                if (table['index'] == 0):
                    arg_dict['temp_type'] = "ipv4"
                elif (table['index'] == 1):
                    arg_dict['temp_type'] = "ipv6"
                elif (table['index'] == 2):
                    arg_dict['temp_type'] = "bridge"
                elif (table['index'] == 3):
                    arg_dict['temp_type'] = "mpls"
                elif (table['index'] == 4):
                    arg_dict['temp_type'] = "mpls-ipv4"
                elif (table['index'] == 5):
                    arg_dict['temp_type'] = "mpls-ipv6"
                
                template_dict['args'] = arg_dict
            ret.append(template_dict)
    return ret

def run():
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_fpc_information()
    online = op.xpath('./fpc[normalize-space(state) = "Online"]/slot')
    ret = []
    ret1= {}
    for i in online:
        if i.text is not None:
            globals().update(FactoryLoader().load(yaml.load(InstanceTableYml, Loader=yaml.FullLoader)))
            ret = func('fpc'+i.text, dev, ret)
    return ret



