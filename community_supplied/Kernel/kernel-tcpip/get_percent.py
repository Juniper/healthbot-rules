from jnpr.junos import Device
from jnpr.junos.utils.config import Config

"""
This function returns the output checking id the parameter has reached specified limit
0 : Output is normal
1 : Output is not normal
"""



def get_percent_output (actual_val, max_val, percent_val, **kwargs):
        output = 0
        a = (int(max_val) * int(percent_val))/100
        if (int(actual_val) > a):
          output = 1

        return output

