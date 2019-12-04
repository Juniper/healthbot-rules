from jnpr.junos import Device
from jnpr.junos.utils.config import Config

"""
This function compares the current nonrpf tunnel id count in the system with the low threshold and high threshold and returns the result
"""

def compare_nonrpf_tunnel_id_cnt(nonrpf_tunnel_id_cnt, nonrpf_tunnel_id_max, **kwargs):
        val = 0
        low_thresh = float(0.85)*nonrpf_tunnel_id_max
        high_thresh = float(0.99)*nonrpf_tunnel_id_max
        if nonrpf_tunnel_id_cnt < low_thresh:
            val = 0
        elif nonrpf_tunnel_id_cnt >= low_thresh  and  nonrpf_tunnel_id_cnt <= high_thresh:
            val = 1
        elif nonrpf_tunnel_id_cnt > high_thresh:
            val = 2
        return val
