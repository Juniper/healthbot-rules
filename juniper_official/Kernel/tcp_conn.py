import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.inet.tcp.irs_kto")
    obj1 = re.search('\d+', op1.text)
    return ({'fields': {"keepalive": int(obj1.group())}})
