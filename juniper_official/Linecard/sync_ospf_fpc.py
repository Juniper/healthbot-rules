def run():
    dev = __proxy__['junos.conn']()
    op = dev.rpc.get_ospf_interface_information(interface_name="[efgx][et]-*")
    interface_names = [i.text for i in op.xpath('ospf-interface/interface-name')]
    ret = []
    for interface_name in interface_names:
        item = __salt__['fpc.get_mapping_from_interface'](interface_name)
        table_argument = {'target': item['target'], 'args': {'chip_instance': item['center_chip_index']}}
        if table_argument not in ret:
            ret.append(table_argument)
            return ret