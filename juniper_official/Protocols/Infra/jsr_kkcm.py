import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.jsr.enable")
    obj = re.search('\d+', op1.text)
    op2 = dev.rpc.request_shell_execute(command="netstat -na | grep 15001 | grep -c ESTABLISHED")
    return ({'fields': {"jsr": int(obj.group()), "kkcm": int(op2.text)}})
