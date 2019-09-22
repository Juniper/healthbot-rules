import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl hw.ore.present")
    obj1 = re.search('\d+', op1.text)
    op2 = dev.rpc.request_shell_execute(command="sysctl hw.re.failover")
    obj2 = re.search('\d+', op2.text)
    return ({'fields': {"ore_present": int(obj1.group()), "failover": int(obj2.group())}})
