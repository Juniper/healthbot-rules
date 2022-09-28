"""
Updates the arguments for rule jflow.config/counterNH jflow.config/flowNH
fetches the argument target fpc, pfe instance and counterNH/flowNH respectively
"""

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import json
from jnpr.junos.factory import loadyaml
from pprint import pprint


SIBYaml = """
---
SIBTable:
    command: show jnh {{instance}} sample
    target: NULL
    args:
        instance: NULL
    view: samplerInstanceView

samplerInstanceView:
    fields:
        v4Table: _v4Table
        v6Table: _v6Table
        mplsTable: _mplsTable

_v4Table:
    item: '*'
    title: '1    0    1 Sampler'
    view: _v4SIBTableview

_v4SIBTableview:
    regex:
        index: '(\d+)\s+\d+\s+\d+\s?Sampler'
        proto: '((\d+))\s+\d+\s?Sampler'
        class: '(\d+)\s?Sampler'
        freq: 'Frequency:(\w+)'
        clen: 'Clip Length:(\w+)'
        CounterNH: '0 : (\w+)'
        FlowNH: '1 : (\w+)'

_v6Table:
    item: '*'
    title: '9    1    1 Sampler'
    view: _v4SIBTableview

_v6SIBTableview:
    regex:
        index: '(\d+)\s+\d+\s+\d+\s?Sampler'
        proto: '((\d+))\s+\d+\s?Sampler'
        class: '(\d+)\s?Sampler'
        freq: 'Frequency:(\w+)'
        clen: 'Clip Length:(\w+)'
        CounterNH: '0 : (\w+)'
        FlowNH: '1 : (\w+)'

_mplsTable:
    item: '*'
    title: '25    3    1 Sampler'
    view: _mplsSIBTableView

_mplsSIBTableView:
    regex:
        index: '(\d+)\s+\d+\s+\d+\s?Sampler'
        proto: '((\d+))\s+\d+\s?Sampler'
        class: '(\d+)\s?Sampler'
        freq: 'Frequency:(\w+)'
        clen: 'Clip Length:(\w+)'
        CounterNH: '0 : (\w+)'
        FlowNH: '1 : (\w+)'

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
PROTO_IPV4 = 0
PROTO_IPV6 = 1
PROTO_MPLS = 3
PROTO_MAX  = 4

def func(fpc, dev, ret):
    table = {}
    class_flag = 0
    nh_flag = 0
    proto = PROTO_MAX
    
    inst = pfeInst(dev)
    pfe_inst=inst.get(target = fpc)
    for inst_key in list(pfe_inst.keys()):
        pfe_inst_table = {}
        a_dict = {}
        pfe_inst_table = pfe_inst[inst_key]
        pinst = pfe_inst_table['pfe_id']
        a_dict['instance']= str(pinst) 
        sample= SIBTable(dev)
        s1=sample.get(target=fpc, args=a_dict)
        for key in list(s1.keys()):
            ret1 = {}
            if (key == 'v4Table' or key == 'mplsTable' or key == 'v6Table'):
                table = s1[key]
            for key1 in table:
                if(key1 == 'CounterNH'):
                    nh_flag=1
    
    #flag will be set if class is Sampler
                if(key1 == 'class' and table[key1] == 1):
                    class_flag=1
    
                if(key1 == 'proto'):
                    proto = table[key1]
    
    #if the nexthop feild exist and class is Sample then update the argumnt list
            if((nh_flag==1) and (class_flag==1)):    
                arg_dict = {}
                arg_dict['instance'] = pinst
                if(proto == PROTO_IPV4 and table['proto'] == 0 and table['index'] == 1 and key == 'v4Table'):
                    arg_dict['NH'] =  table['CounterNH']
                    arg_dict['proto'] = table['proto']
                    ret1['target'] = fpc
                    ret1['args'] = arg_dict
                    ret.append(ret1)
                elif(proto == PROTO_IPV6 and table['proto'] == 1 and table['index'] == 9 and key == 'v6Table'):
                    arg_dict['NH'] = table['CounterNH']
                    arg_dict['proto'] = table['proto']
                    ret1['target'] = fpc
                    ret1['args'] = arg_dict
                    ret.append(ret1)
                elif(proto == PROTO_MPLS and table['proto'] == 3 and table['index'] == 25 and key == 'mplsTable'):
                    arg_dict['NH'] = table['CounterNH']
                    arg_dict['proto'] = table['proto']
                    ret1['target'] = fpc
                    ret1['args'] = arg_dict
                    ret.append(ret1)
    
    
        for key in list(s1.keys()):
            ret1 = {}
            if (key == 'v4Table' or key == 'mplsTable' or key == 'v6Table'):
                table = s1[key]
    
            for key1 in table:
                if(key1 == 'CounterNH'):
                    nh_flag=1
    
    #flag will be set if class is Sampler
                if(key1 == 'class' and table[key1] == 1):
                    class_flag=1
    
                if(key1 == 'proto'):
                    proto = table[key1]
    
    #if the nexthop feild exist and class is Sample then update the argumnt list
            if((nh_flag==1) and (class_flag==1)):    
                arg_dict = {}
                arg_dict['instance'] = pinst
                if(proto == PROTO_IPV4 and table['proto'] == 0 and table['index'] == 1 and key == 'v4Table'):
                    arg_dict['flowNH'] =  table['FlowNH']
                    arg_dict['proto'] = table['proto']
                    ret1['target'] = fpc
                    ret1['args'] = arg_dict
                    ret.append(ret1)
                elif(proto == PROTO_IPV6 and table['proto'] == 1 and table['index'] == 9 and key == 'v6Table'):
                    arg_dict['flowNH'] = table['FlowNH']
                    arg_dict['proto'] = table['proto']
                    ret1['target'] = fpc
                    ret1['args'] = arg_dict
                    ret.append(ret1)
                elif(proto == PROTO_MPLS and table['proto'] == 3 and table['index'] == 25 and key == 'mplsTable'):
                    arg_dict['flowNH'] = table['FlowNH']
                    arg_dict['proto'] = table['proto']
                    ret1['target'] = fpc
                    ret1['args'] = arg_dict
                    ret.append(ret1)
    return ret


def run():
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_fpc_information()
    online = op.xpath('./fpc[normalize-space(state) = "Online"]/slot')
    ret = []
    ret1= {}
    for i in online:
        if i.text is not None:
            globals().update(FactoryLoader().load(yaml.load(SIBYaml, Loader=yaml.FullLoader)))
            ret = func('fpc'+i.text, dev, ret)
    return ret



