#!/usr/bin/env python3
from __future__ import print_function, division
import requests, sys
from pprint import pprint as pp
from tand_udf import MultiRows

def get_ifl_stats(**kwargs):
    print(kwargs, file=sys.stderr)
    # Define and query influxdb
    dg = (kwargs['device_group'])
    did = (kwargs['device_id'])
    print("DG", dg)
    url = "http://influxdb:8086/query?db={0}:{1}&rp={0}:{1}".format(dg, did)
    params = {
        'q': 'select * from "service.cgnat/check-cgnat" where time > now() - 1800s group by * limit 1'
    }
    response = requests.get(url=url, params=params)
    res = response.json()
    #print("response :",res)
    res_tags = []
    res_fields = []
    for i, value in enumerate(res['results'][0]['series']):
        tags = ['', '', '', '']
        # interface-name, internal-ip, pool-name, service-set-name
        if "interface-name" in value['tags']:
            tags[0] = value['tags']['interface-name']
        if 'internal-ip' in value['tags']:
            tags[1] = value['tags']['internal-ip']
        if 'pool-name' in value['tags']:
            tags[2] = value['tags']['pool-name']
        if 'service-set-name' in value['tags']:
            tags[3] = value['tags']['service-set-name']
        res_tags.append(tags)
        # session-count, ports-used, external-ip
        fields = [0, 0, '']
        for ind, field in enumerate(("session-count",
                                     "ports-used", "external-ip")):
            try:
                field_index = value['columns'].index(field)
                fields[ind] = value['values'][0][field_index]
            except ValueError as exp:
                print(exp)
        res_fields.append(fields)
    session_list = [row[0] for row in res_fields]
    external_ip_list = [row[2] for row in res_fields]
    internal_ip_list = [x[1] for x in res_tags]
    avg_external_ip1 = avg_external_ip(external_ip_list)
    max_session_count1 = max_session_count(session_list, internal_ip_list)
#    max_session_count1 = max_session_count(session_list)
    total_external_ip1 = total_external_ip(external_ip_list)
    total_internal_ip1 = len(list(set([x[1] for x in res_tags])))
    avg_session_count1 = avg_session_count(session_list, total_internal_ip1)
    max_external_ip1 = max_external_ip(external_ip_list)

    rows = MultiRows()
    rows.add_row()
    rows.add_field("avg_external_ip", avg_external_ip1)
    rows.add_field("max_session_count", max_session_count1)
    rows.add_field("total_external_ip", total_external_ip1)
    rows.add_field("avg_session_count", avg_session_count1)
    rows.add_field("total_internal_ip", total_internal_ip1)
    rows.add_field("max_external_ip", max_external_ip1)
    return rows


'''
This function returns average external ip address
'''
def avg_external_ip(list_external_ip):
    ori_len = len(list_external_ip)
    list_external_ip = set(list_external_ip)
    final_len = len(list_external_ip)
    utilization = 0
    if ori_len > 0:
         utilization = ori_len/final_len
    return utilization

'''
This function returns average external ip address
'''
def avg_session_count(list_session_count, external_ip_count):
    total_value = sum(list_session_count)
    if external_ip_count > 0:
        avg_value = total_value/external_ip_count
        return round(avg_value,2)
    return 0

'''
This function returns average external ip address
'''
def max_external_ip(list_external_ip):
    a = [[x,list_external_ip.count(x)] for x in set(list_external_ip)]
    max_value = 0
    for i in a:
        if i[1] > max_value:
            max_value = i[1]
    return max_value

'''
This function returns average external ip address
'''
#def max_session_count(list_session_count):
#    max_value = 0
#    if list_session_count:
#        max_value = max(list_session_count)
#    return max_value

def max_session_count(list_session_count, list_internal_ip):
    max_value = 0
    unique_session_count = dict()
    for val1, val2 in zip(list_internal_ip, list_session_count):
        if val1 in unique_session_count:
            unique_session_count[val1] = unique_session_count[val1] + val2
        else:
            unique_session_count[val1] = val2
    max_value = unique_session_count.get(max(unique_session_count, key=unique_session_count.get))
    return max_value
#    sum_session_list=[]
#    already=[]
#    if list_session_count:
#        for x in list_internal_ip:
#            c=0
#            temp=[]
#            for y in list_internal_ip:
#                if((x==y) and (x not in already)):
#                    temp.append(list_session_count[c])
#                c+=1
#            sum_session_list.append(sum(temp))
#            already.append(x)
#        max_value = max(sum_session_list)
#    return max_value


'''
This function returns average external ip address
'''
def total_external_ip(list_external_ip):
    list_external_ip = set(list_external_ip)
    final_len = len(list_external_ip)
    return final_len

