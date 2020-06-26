import sys
import requests
from jnpr.junos.device import Device
from pprint import pprint
from __future__ import division

#megabytes per second conversion
def mbps(bps, **kwargs):
        mbps = bps/1000000
        return mbps

#This function converts speedory speed string to float
def bw_util_percent(mbps, speed, **kwargs):
    if speed.endswith('Gbps'):
        speed = speed[:-4]
        speed = float(speed) * 1000
        bw_utilization=(mbps/speed)*100
    elif speed.endswith('mbps'):
        speed = speed[:-4]
        speed = float(speed)
        bw_utilization=(mbps/speed)*100
    else:
        speed = float(speed)
        bw_utilization = (mbps/speed)*100
    return "%.2f" % bw_utilization
