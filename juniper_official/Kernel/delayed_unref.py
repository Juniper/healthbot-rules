import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.rt_nh_max_delayed_unrefs")
    obj = re.search('\d+', op1.text)
    obj1 = int(obj.group())
    op2 = dev.rpc.request_shell_execute(command="ifsmon -I | grep unique")
    a = op2.text.split(':')[1]
    re1 = re.search('\d+', a)
    obj2 = int(re1.group())
    return ({'fields': {"unref_cnt": obj2, "unref_max": obj1}})
