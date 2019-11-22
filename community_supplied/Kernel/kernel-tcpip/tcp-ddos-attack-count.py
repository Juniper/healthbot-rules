import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.inet.tcp.system_attack_count")
    obj = re.search('\d+', op1.text)
    obj1 = int(obj.group())
    return ({'fields': {"tcp-ddos-attack": obj1}})
