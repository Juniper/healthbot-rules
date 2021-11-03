from __future__ import division
import re
'''
This function returns float value of a percentage string
'''

def get_float_from_percentage_string(percentage_string, **kwargs):
    match_value = re.search(r"(\d+\.\d+)\s+\%", percentage_string)
    return float(match_value.group(1))
