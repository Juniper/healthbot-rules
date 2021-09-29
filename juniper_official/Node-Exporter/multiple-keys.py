# generic function to find the difference between current and previous values
# usage: key_name is mandatory to store the previous value
#        sub_key_name is optional can be used in case of multiple keys
def value_diff(key_name, value, sub_key_name = None, sub_key_name2 = None, **kwargs):
    key_sub_key_name = ""
    if sub_key_name is None:
        key_sub_key_name = key_name
    else:
        key_sub_key_name = key_name + "." + sub_key_name
		
    key_sub_key_name2 = ""		
    if sub_key_name2 is None:
        key_sub_key_name2 = key_sub_key_name
    else:
        key_sub_key_name2 = key_sub_key_name + "." + sub_key_name2		
 
    if 'hb_store' not in kwargs:
        kwargs['hb_store'] = {
            'prev_value': dict()
        }
    else:
        if 'prev_value' not in kwargs['hb_store']:
            kwargs['hb_store']['prev_value'] = dict()
    prev_value = kwargs['hb_store']['prev_value']
 
    curr_value = int(value)
    val_diff = curr_value - prev_value.get(key_sub_key_name2, 0)
 
    # update global values
    prev_value[key_sub_key_name2] = curr_value
    return val_diff