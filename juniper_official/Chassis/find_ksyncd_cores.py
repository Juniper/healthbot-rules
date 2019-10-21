import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="cli show system core-dumps routing-engine other | grep -c ksyncd")
    return ({'fields': {"ksyncd_cores": int(op1.text)}})
