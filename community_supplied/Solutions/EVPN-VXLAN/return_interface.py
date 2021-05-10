import re
'''
This function returns 'xe-' interface matching to 'em' interface provided as input for vqfx device.
'''
def get_intf(ifname, **kwargs):
    intf = ''
    if 'em' in ifname and '.' not in ifname:
        slot=re.findall(r"[3-9]|1[0-4]",ifname)
        if int(slot[0]) >= 3:
            intf='xe-0/0/' + str(int(slot[0]) - 3)
    return intf
