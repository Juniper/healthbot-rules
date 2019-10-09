from jnpr.junos import Device
from jnpr.junos.utils.config import Config

"""
This function compares the current vpls flood token count in the system with the low threshold and high threshold and returns the result
"""

def compare_vpls_flood_token_cnt(vpls_flood_token_cnt, vpls_flood_token_max, **kwargs):
        val = 0
        low_thresh = float(0.8)*vpls_flood_token_max
        high_thresh = float(0.9)*vpls_flood_token_max
        if vpls_flood_token_cnt < low_thresh:
            val = 0
        elif vpls_flood_token_cnt >= low_thresh and vpls_flood_token_cnt <= high_thresh:
            val = 1
        elif vpls_flood_token_cnt > high_thresh:
            val = 2
        return val

