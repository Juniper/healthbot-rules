import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.tunnel.looped_cnt")
    re1 = re.search('\d+', op1.text)
    obj1 = int(re1.group())
    return ({'fields': {"looped_tun_cnt": obj1}})
