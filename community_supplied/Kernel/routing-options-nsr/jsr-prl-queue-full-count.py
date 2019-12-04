import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="netstat -p jsr | grep 'failed to enqueue'")
    obj = re.search('\d+', op1.text)
    obj1 = int(obj.group())
    return ({'fields': {"jsr-prl-queue-full": obj1}})
