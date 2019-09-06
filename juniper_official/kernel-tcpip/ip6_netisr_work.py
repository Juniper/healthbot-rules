def run():
    dev = __proxy__['junos.conn']()
    netisr_work =dev.rpc.request_shell_execute(command="sysctl net.isr.work | grep -e \"proto 3]\"")
    netisr_work = netisr_work.text.replace(',' , '').split(' ')
    nw_drop = int(netisr_work[16])
    nw_queued = int(netisr_work[18])
    nw_handled = int(netisr_work[20])
    return ({'fields': {"ip6_pkt_drop": nw_drop , "ip6_pkt_queued": nw_queued ,"ip6_pkt_handled": nw_handled }})
