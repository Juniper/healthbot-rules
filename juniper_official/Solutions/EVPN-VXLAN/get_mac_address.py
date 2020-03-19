# this function collects dynamic mac-address from ethernet-switching table and updates dependent sensor tables
# rpc command: get-ethernet-switching-table-information - show ethernet-switching table
def run():
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_ethernet_switching_table_information()
    mac = op.xpath('//l2ng-mac-entry[normalize-space(l2ng-l2-mac-flags) = "D"]/l2ng-l2-mac-address')
    ret = []
    for i in mac:
        if i.text is not None:
            ret.append({'args': {'address': i.text}})
    return ret
