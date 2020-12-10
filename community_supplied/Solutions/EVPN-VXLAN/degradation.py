#! /usr/bin/env python3
import requests
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.ethport import EthPortTable
from collections import OrderedDict

good_history_uplink = []

def degradation_percent(total_interfaces, current_lldp_interfaces, **kwargs):
    global good_history_uplink
    good_history_uplink = good_history_uplink + total_interfaces
    good_history_uplink = list(OrderedDict.fromkeys(good_history_uplink))
    total_interfaces_len = len(good_history_uplink)
    uplink_down_list = []
    for intf in good_history_uplink:
        if intf not in current_lldp_interfaces:
            uplink_down_list.append(intf)
    uplink_down_length = len(uplink_down_list)
    if total_interfaces_len == 0:
         return 0
    else:
         return int((uplink_down_length / total_interfaces_len ) * 100 )
