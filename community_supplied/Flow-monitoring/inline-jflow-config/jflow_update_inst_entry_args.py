"""
Updates the arguments for rule jflow.config/verify-inst-entry
Fetches the target fpc, pfe instance, corresponding protocol family index in instance table
and the template configured of the corresponding protocol family.
"""

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import json
from jnpr.junos.factory import loadyaml
from pprint import pprint

InstanceTableYml = """
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


fwdConfig:
    get: forwarding-options/sampling/instance
    view: sampleView
sampleView:
    fields:
        inst_name: name
        rate: input/rate
        family_inet: family/inet
        family_inet6: family/inet6
        family_mpls: family/mpls
        flow_server_v4: family/inet/output/flow-server/name
        flow_server_port_v4: family/inet/output/flow-server/port
        flow_server_v6: family/inet6/output/flow-server/name
        flow_server_port_v6: family/inet6/output/flow-server/port
        flow_server_mpls: family/mpls/output/flow-server/name
        flow_server_port_mpls: family/mpls/output/flow-server/port
        template_name_ipfix_v4: family/inet/output/flow-server/version-ipfix/template/template-name
        template_name_v9_v4: family/inet/output/flow-server/version9/template/template-name
        template_name_ipfix_v6: family/inet6/output/flow-server/version-ipfix/template/template-name
        template_name_v9_v6: family/inet6/output/flow-server/version9/template/template-name
        template_name_ipfix_mpls: family/mpls/output/flow-server/version-ipfix/template/template-name
        template_name_v9_mpls: family/mpls/output/flow-server/version9/template/template-name
flowMonitorv9:
    rpc: get_config
    args:
        filter_xml: services/flow-monitoring/version9/template
        options:
            inherit: inherit
            groups: groups
    item: services/flow-monitoring/version9/template
    view: v9serviceView
v9serviceView:
    fields:
        v9_temp_name: name
        v9_ipv4_template: ipv4-template
        v9_ipv6_template: ipv6-template
        v9_mpls_template: mpls-template
        v9_mpls_v4_template: mpls-ipv4-template
        v9_mpls_v6_template: mpls-ipv6-template
        v9_act_timeout: flow-active-timeout
        v9_inact_timeout: flow-inactive-timeout

flowMonitorIpFix:
    rpc: get_config
    args:
        filter_xml: services/flow-monitoring/version-ipfix/template
        options:
            inherit: inherit
            groups: groups

    item: services/flow-monitoring/version-ipfix/template
    view: serviceView
serviceView:
    fields:
        ipfix_temp_name: name
        ipfix_ipv4_template: ipv4-template
        ipfix_ipv6_template: ipv6-template
        ipfix_mpls_template: mpls-template
        ipfix_mpls_v4_template: mpls-ipv4-template
        ipfix_mpls_v6_template: mpls-ipv6-template
        ipfix_act_timeout: flow-active-timeout
        ipfix_inact_timeout: flow-inactive-timeout

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

decodeFlowNH:
    command: show jnh {{instance}} decode {{flowNH}}
    target: NULL
    args:
        flowNH: Null
        instance: Null
    item: '*'
    view: _decodeView

_decodeView:
    regex:
        invalid: '(\w+) jnh-type'
        flownh: 'FlowNH:(\w+)'


decodeNextHop:
    command: show jnh {{instance}} decode {{NH}}
    target: NULL
    args:
        NH: Null
        instance: Null
    item: '*'
    view: _decodeView

_decodeView:
    regex:
        invalid: '(\w+) jnh-type'
        nxt_hop: 'nextNH = (\w+)'
        caddr: 'Caddr = (\w+)'
        flownh: 'FlowNH:(\w+)'
"""


def decodeNH(fpc, dev, pfe_inst, table, decode_ret):
    a_cnh_dict = {}
    a_fnh_dict = {}
    a_cnh_dict['instance'] = pfe_inst
    a_cnh_dict['NH'] = table['CounterNH']
    a_fnh_dict['instance'] = pfe_inst
    a_fnh_dict['NH'] =  table['FlowNH']
    globals().update(FactoryLoader().load(yaml.load(InstanceTableYml, Loader=yaml.FullLoader)))

    #check if counter Nh is valid for thr SIB entry
    decode_cnh_sample = decodeNextHop(dev)
    decode_cnh = decode_cnh_sample.get(target = fpc, args=a_cnh_dict)
    for key in list(decode_cnh.keys()):
        if (key == "invalid"):
            decode_ret['CounterNH'] = "invalid"
        else:
            if(decode_cnh and decode_cnh['nxt_hop'] != None and decode_cnh['caddr'] != None ):
                decode_ret['CounterNH'] = "Valid"
            else:
                decode_ret['CounterNH'] = "invalid" 
    if (len(decode_cnh) == 0):
        decode_ret['CounterNH'] = "invalid"

    #check if flowNH is JFlow for thr SIB entry
    decode_fnh_sample = decodeNextHop(dev)
    decode_fnh = decode_fnh_sample.get(target=fpc, args=a_fnh_dict)
    for key in list(decode_fnh.keys()):
        if (key == "invalid"):
            decode_ret['flowNH'] = "invalid"
        elif (key == "flownh"):
            if (decode_fnh['flownh'] == 'JFlow'):
                decode_ret['flowNH'] = "Valid"
    if(len(decode_fnh) == 0):
        decode_ret['flowNH'] = "invalid"
    return decode_ret


def func(fpc, dev, ret):
    table = {}
    sample3 = pfeInst(dev)
    pfe_inst = sample3.get(target=fpc)
    for inst_key in list(pfe_inst.keys()):
        pfe_inst_table = {}
        a_dict = {}
        pfe_inst_table = pfe_inst[inst_key]
        pinst = pfe_inst_table['pfe_id']
        a_dict['instance']= str(pinst) 
        sample2 = fpcConfig(dev)
        s2 = sample2.get()
        sample4 = fwdConfig(dev)
        s4 = sample4.get()
        
        #Extract the SIB details for each protocol family configured on the fpc from SIb table
        sample= SIBTable(dev)
        s1=sample.get(target=fpc, args=a_dict)
        for key_sib in list(s1.keys()):
            if (key_sib == 'v4Table'):
                table_sib_v4 = s1[key_sib]
            if(key_sib == 'v6Table'):
                table_sib_v6 = s1[key_sib]
            if(key_sib == 'mplsTable'):
                table_sib_mpls = s1[key_sib]

        #check which protcol families have been configured for sampling instance in RE CLI
        for key1 in list(s2.keys()):
            fwd_table = {}
            table1 = s2[key1]
            if (table1['sample_inst_name'] == None):
                continue
            if ('fpc'+table1['name'] == fpc):
                for key in list(s4.keys()):
                    table = s4[key]
                    if (table1['sample_inst_name'] != table['inst_name']):
                        continue
                    #family IPv4 
                    if (table['flow_server_v4'] != None):
                        index_dict = {}
                        template_dict = {}
                        arg_dict = {}
                        field_dict = {}
                        decode_ret = {}
                        instance=pinst
                        index_dict['target'] = fpc
                        arg_dict['index'] = 0
                        arg_dict['instance'] = instance
                        arg_dict['s_inst_name'] = table1['sample_inst_name']

                        #extracting the template details for IPv4
                        if (table['template_name_ipfix_v4'] != None):
                            a = table['template_name_ipfix_v4']
                            if (type (a) == list):
                                arg_dict['template_name']  = a[0]
                            else:
                                arg_dict['template_name'] = table['template_name_ipfix_v4']


                        elif (table['template_name_v9_v4'] != None):
                            a = table['template_name_v9_v4']
                            if (type (a) == list):
                                arg_dict['template_name']  = a[0]
                            else:
                                arg_dict['template_name'] = table['template_name_v9_v4']
                        
                        #checking if the flowNH and countreNh is valid for IPv4
                        if (table_sib_v4['proto'] == 0 and table_sib_v4['index'] == 1 and table_sib_v4['class'] == 1):
                            decode_ret = decodeNH(fpc, dev, instance, table_sib_v4, decode_ret)
                            if(decode_ret['CounterNH'] != None):
                                if (decode_ret['CounterNH'] == "Valid"): 
                                    arg_dict['counterNH'] = "valid-ipv4"
                                else :
                                    arg_dict['counterNH'] = "invalid-ipv4"
                            else:
                                arg_dict['counterNH'] = "invalid-ipv4"

                            if (decode_ret['flowNH'] != None):
                                if (decode_ret['flowNH'] == "Valid"):
                                    arg_dict['flowNH'] = "valid-ipv4"
                                else:
                                    arg_dict['flowNH'] = "invalid-ipv4"
                            else:
                                arg_dict['flowNH'] = "invalid-ipv4"
                        else:
                            arg_dict['counterNH'] = "invalid-ipv4"
                            arg_dict['flowNH'] = "invalid-ipv4"

                        
                            
                        index_dict['args'] = arg_dict
                        ret.append(index_dict)

                    #protocol family IPv6
                    if (table['flow_server_v6'] != None):
                        index_dict = {}
                        template_dict = {}
                        arg_dict = {}
                        field_dict = {}
                        decode_ret = {}
                        instance=pinst
                        arg_dict['index'] = 1
                        index_dict['target'] = fpc
                        arg_dict['instance'] = instance
                        arg_dict['s_inst_name'] = table1['sample_inst_name']

                        #extracting template details for family IPv6
                        if (table['template_name_ipfix_v6'] != None):
                            a = table['template_name_ipfix_v6']
                            if (type (a) == list):
                                arg_dict['template_name']  = a[0]
                            else:
                                arg_dict['template_name'] = table['template_name_ipfix_v6']

                        elif (table['template_name_v9_v6'] != None):
                            a = table['template_name_v9_v6']
                            if (type (a) == list):
                                arg_dict['template_name']  = a[0]
                            else:
                                arg_dict['template_name'] = table['template_name_v9_v6']
                        
                        #verifying if flowNh and counterNh is valid for the family IPv6
                        if (table_sib_v6['proto'] == 1 and table_sib_v6['index'] == 9 and table_sib_v6['class'] == 1):
                            decode_ret = decodeNH(fpc, dev, instance, table_sib_v6, decode_ret)
                            if(decode_ret['CounterNH'] != None):
                                if (decode_ret['CounterNH'] == "Valid"):
                                    arg_dict['counterNH'] = "valid-ipv6"
                                else:
                                    arg_dict['counterNH'] = "invalid-ipv6"
                            else:
                                arg_dict['counterNH'] = "invalid-ipv6"


                            if (decode_ret['flowNH'] != None):
                                if (decode_ret['flowNH'] == "Valid"):
                                    arg_dict['flowNH'] = "valid-ipv6"
                                else:
                                    arg_dict['flowNH'] = "invalid-ipv6"
                            else:
                                arg_dict['flowNH'] = "invalid-ipv6"
                        
                        else:
                            arg_dict['counterNH'] = "invalid-ipv6"
                            arg_dict['flowNH'] = "invalid-ipv6"


                        index_dict['args'] = arg_dict
                        ret.append(index_dict)

                    #family config for MPLS
                    if (table['flow_server_mpls'] != None):
                        index_dict = {}
                        template_dict = {}
                        arg_dict = {}
                        field_dict = {}
                        decode_ret = {}
                        instance=pinst
                        arg_dict['index'] = 3
                        index_dict['target'] = fpc
                        arg_dict['instance'] = instance
                        arg_dict['s_inst_name'] = table1['sample_inst_name']
                        #extracting template details for family MPLS with template type MPLS/MPLS-ipv4/MPLS-IPv6
                        if (table['template_name_ipfix_mpls'] != None):
                            a = table['template_name_ipfix_mpls']
                            if (type (a) == list):
                                arg_dict['template_name']  = a[0]
                            else:
                                arg_dict['template_name'] = table['template_name_ipfix_mpls']
                            flow_mon_ipfix = flowMonitorIpFix(dev)
                            f1 = flow_mon_ipfix.get()       
                            for keyf in list(f1.keys()):    
                                table_flow = f1[keyf]           
                                if (table_flow['ipfix_temp_name'] == arg_dict['template_name']):
                                    if(table_flow['ipfix_mpls_v4_template'] == "mpls-ipv4-template"):
                                        arg_dict['index'] = 4           
                            
                                    elif(table_flow['ipfix_mpls_v6_template'] == "mpls-ipv6-template"):
                                        arg_dict['index'] = 5           

                        elif (table['template_name_v9_mpls'] != None):
                            a = table['template_name_v9_mpls']
                            if (type (a) == list):
                                arg_dict['template_name']  = a[0]
                            else:
                                arg_dict['template_name'] = table['template_name_v9_mpls']
                            flow_mon_v9 = flowMonitorv9(dev)
                            f1 = flow_mon_v9.get()
                            for keyf in list(f1.keys()):
                                table_flow = f1[keyf]
                                if (table_flow['v9_temp_name'] == arg_dict['template_name']):
                                    if(table_flow['v9_mpls_v4_template'] == "mpls-ipv4-template"):
                                        arg_dict['index'] = 4
                            
                                    elif(table_flow['v9_mpls_v6_template'] == "mpls-ipv6-template"):
                                        arg_dict['index'] = 5
                        
                        #verifying if the flowNh and counterNh is valid for MPLS
                        if (table_sib_mpls['proto'] == 3 and table_sib_mpls['index'] == 25 and table_sib_mpls['class'] == 1):
                            decode_ret = decodeNH(fpc, dev, instance, table_sib_mpls, decode_ret)
                            if(decode_ret['CounterNH'] != None):
                                if (decode_ret['CounterNH'] == "Valid"):
                                    arg_dict['counterNH'] = "valid-mpls"
                                else:
                                    arg_dict['counterNH'] = "invalid-mpls"
                            else:
                                arg_dict['counterNH'] = "invalid-mpls"

                            if (decode_ret['flowNH'] != None):
                                if (decode_ret['flowNH'] == "Valid"):
                                    arg_dict['flowNH'] = "valid-mpls"
                                else:
                                    arg_dict['flowNH'] = "invalid-mpls"
                            else:
                                arg_dict['flowNH'] = "invalid-mpls"

                        else:
                            arg_dict['counterNH'] = "invalid-mpls"
                            arg_dict['flowNH'] = "invalid-mpls"

                        index_dict['args'] = arg_dict
                        ret.append(index_dict)

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



