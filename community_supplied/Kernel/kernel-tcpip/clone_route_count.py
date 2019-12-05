import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.inet.rtclone_system_cnt")
    re1 = re.search('\d+', op1.text)
    obj1 = int(re1.group())
    op2 = dev.rpc.request_shell_execute(command="sysctl net.inet.rtclone_max_limit")
    re2 = re.search('\d+', op2.text)
    obj2 = int(re2.group())
    return ({'fields': {"route_clone_max": obj2, "route_clone_cnt": obj1}})
