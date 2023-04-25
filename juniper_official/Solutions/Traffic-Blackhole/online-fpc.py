# this function collects online fpc and updates dependent sensor tables
# rpc command: get-fpc-information
def run():
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_fpc_information()
    online = op.xpath('./fpc[normalize-space(state) = "Online"]/slot')
    ret = []
    for i in online:
        if i.text is not None:
            ret.append({'target': 'fpc'+i.text})
    return
