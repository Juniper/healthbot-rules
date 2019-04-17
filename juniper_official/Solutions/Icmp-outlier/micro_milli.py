from __future__ import division
'''
This function converts micro seconds to milli seconds
'''
def rtt_micro_milli(micros, **kwargs):
    return float(int(micros)/1000.0)
