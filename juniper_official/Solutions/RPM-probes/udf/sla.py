from __future__ import division
'''
This function calculates the sla percentage over a period of 1 year
'''
def sla_1y(total_online_time, **kwargs):
        return float(100 * float(total_online_time/31536000))

