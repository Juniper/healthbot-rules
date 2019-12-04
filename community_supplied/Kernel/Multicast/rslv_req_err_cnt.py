import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.mcast.rslv_req_err_cnt")
    re1 = re.search('\d+', op1.text)
    obj1 = int(re1.group())
    return ({'fields': {"rslv_req_err_cnt": obj1}})
