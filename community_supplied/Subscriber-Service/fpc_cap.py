'''
fpc_cap.py - This library contains methods return capacity per fpc based on fpc type:

    fpc_capacity()  - This function produces a fpc capacity based on fpc_type and dictionary of data passed
    
'''

'''-----------------------------------------------------------------------------
    fpc_capacity()  - This function produces a fpc capacity based on fpc type and dictionary of data passed
    
    Input: 
         cases - Dictionary of key value pairs as a string (Key: fpc type, Value: FPC capacity)
         fpc_type - fpc type
    Output:
         FPC capacity for the respective fpc type.
-----------------------------------------------------------------------------'''
import re
import json

def fpc_capacity(cases, fpc_type, **kwargs):
    
    cases = cases.replace('\"','"')
    cases = cases.replace("'","")
    cases_map = json.loads(cases)
    
    
    # code will match any FPC as long as its the suffix of string returned from sensor or its within brackets
    match = re.search(r'((LC|MPC|Virtual)+[^]]*)', str(fpc_type))
    try:
        fpc = match.group(1)
    except:
        return 0


    capacity = cases_map.get(fpc, "not a supported FPC/MPC type")
    return capacity
