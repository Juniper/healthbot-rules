"""
This function checks for online fpcs and updates dependent sensor tables
with the target fpc number and pfe instance-id for that fpc
(depending on the number of PFE instance running on it).
rpc command: get-fpc-information
"""

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import json
from jnpr.junos.factory import loadyaml
from pprint import pprint
pfeInstTable = """
---
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
    sample3 = pfeInst(dev)
    pfe_inst = sample3.get(target=fpc)
    for inst_key in list(pfe_inst.keys()):
        pfe_inst_table = {}
        a_dict = {}
        pfe_dict = {}
        pfe_inst_table = pfe_inst[inst_key]
        pinst = pfe_inst_table['pfe_id']
        a_dict['instance']= str(pinst)
        pfe_dict['target'] = fpc
        pfe_dict['args'] = a_dict
        ret.append(pfe_dict)
    return ret

def run():
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_fpc_information()
    online = op.xpath('./fpc[normalize-space(state) = "Online"]/slot')
    ret = []
    for i in online:
        if i.text is not None:
            globals().update(FactoryLoader().load(yaml.load(pfeInstTable, Loader=yaml.FullLoader)))
            ret = func('fpc'+i.text, dev, ret)
    return ret
