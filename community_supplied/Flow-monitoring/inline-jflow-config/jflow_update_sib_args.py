from jnpr.junos import Device
from getpass import getpass
import sys
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
from pprint import pprint
import json
from lxml import etree

myYaml4 = """
---
fpcConfig:
    rpc: get_config
    args:
        filter_xml: chassis/fpc
        options:
            inherit: inherit
            groups: groups
    item: chassis/fpc
    view: chassisView
chassisView:
    fields:
        fpc_number: name
        sample_inst_name: sampling-instance/name

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

def func (fpc, dev, ret):
    value = ""
    inst = pfeInst(dev)
    pfe_inst=inst.get(target = fpc)
    for inst_key in list(pfe_inst.keys()):
        pfe_inst_table = {}
        a_dict = {}
        pfe_inst_table = pfe_inst[inst_key]
        pinst = pfe_inst_table['pfe_id']
        a_dict['instance']= str(pinst) 
        sample1 = fpcConfig(dev)
        s1= sample1.get(target=fpc)
        for key in list(s1.keys()):
            ret1 = {}
            table = s1[key]
            if ('fpc'+table['name'] == fpc):
                arg_dict = {}
                arg_dict['instance'] = pinst
                arg_dict['s_inst_name'] = table['sample_inst_name']
                ret1['target'] = fpc
                ret1['args'] = arg_dict
                ret.append(ret1)
    return ret


def run():
    globals().update(FactoryLoader().load(yaml.load(myYaml4, Loader=yaml.FullLoader)))
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_fpc_information()
    online = op.xpath('./fpc[normalize-space(state) = "Online"]/slot')
    ret = []
    ret1= {}
    for i in online:
        if i.text is not None:
            ret = func('fpc'+i.text, dev, ret)
    return ret
