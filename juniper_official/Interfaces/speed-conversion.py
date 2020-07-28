from __future__ import division
import sys

#This function converts speedory speed string to float
def speed_conv(speed, **kwargs):
    if speed.endswith('Gbps'):
        speed = speed[:-4]
        speed = int(speed) * 1000
    elif speed.endswith('mbps'):
        speed = speed[:-4]
        speed = int(speed)
    else:
        speed = int(speed)
    return speed