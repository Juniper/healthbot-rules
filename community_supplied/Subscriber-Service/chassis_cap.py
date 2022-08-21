'''
chassis_cap.py - This library contains methods to return chaasis capacity based on chassis name and dictionary of data passed:

    chassis_capacity()  - This function produces a chaasis capacity based on chassis name and dictionary of data passed
    
'''

'''-----------------------------------------------------------------------------
    chassis_capacity()  - This function produces a chaasis capacity based on chassis name and dictionary of data passed
    
    Input: 
         cases - Dictionary of key value pairs as a string (Key: Chassis name, Value: Chassis capacity)
         chassis - Chassis name
    Output:
         Chaasis capacity for the respective Chassis name.
-----------------------------------------------------------------------------'''
import re
import json


def chassis_capacity(cases, chassis, **kwargs):

    cases = cases.replace('\"','"')
    cases = cases.replace("'","")
    cases_map = json.loads(cases)

    # code will match any MX chassis as long as its the suffix of string returned from sensor or its within brackets
    match = re.search(r'((MX|VMX)+[^]]*)', str(chassis))
    try:
        chassis_name = match.group(1)

    except:
        return 0

    capacity = int(cases_map.get(chassis_name, 0))
    return capacity
   