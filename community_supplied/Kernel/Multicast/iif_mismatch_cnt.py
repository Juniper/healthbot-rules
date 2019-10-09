import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.mcast.iifmismatch_err_cnt")
    re1 = re.search('\d+', op1.text)
    obj1 = int(re1.group())
    return ({'fields': {"iif_mismatch_err_cnt": obj1}})
