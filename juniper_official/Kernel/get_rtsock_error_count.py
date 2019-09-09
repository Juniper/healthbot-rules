import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.rtsock_total_error_count")
    obj = re.search('\d+', op1.text)
    obj1 = int(obj.group())
    op2 = dev.rpc.request_shell_execute(command="sysctl net.rtsock_total_veto_count")
    obj = re.search('\d+', op2.text)
    obj2 = int(obj.group())
    return ({'fields': {"total_error_count": obj1, "total_veto_count": obj2}})
