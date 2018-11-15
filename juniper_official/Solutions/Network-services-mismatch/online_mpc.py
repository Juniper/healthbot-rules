import re

def run():
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_fpc_information()
    online = op.xpath('./fpc[normalize-space(state) = "Online"]/slot')
    op2 = dev.rpc.get_chassis_inventory()
    ret = []
    for slot in online:
        if slot.text is not None:
            fru = op2.xpath('./chassis/chassis-module[normalize-space(name) = "FPC {}"]/description'.format(slot.text))
            if re.match("^(MPC)", fru[0].text):
                ret.append({'target': 'fpc'+slot.text})
    return ret
