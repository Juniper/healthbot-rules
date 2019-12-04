import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="netstat -p tcp | grep embryonic")
    obj = re.search('\d+', op1.text)
    obj1 = int(obj.group())
    return ({'fields': {"tcp-connection-drops": obj1}})
