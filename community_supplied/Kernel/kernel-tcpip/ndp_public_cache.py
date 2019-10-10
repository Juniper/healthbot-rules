import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="cli show system statistics icmp6 | grep -e \"Current Public ND\"")
    re1 = re.search('\d+', op1.text)
    obj1 = int(re1.group())
    op2 = dev.rpc.request_shell_execute(command="cli show system statistics icmp6 | grep -e \"public limit reached\"")
    re2 = re.search('\d+', op2.text)
    obj2 = int(re2.group())
    op3 = dev.rpc.request_shell_execute(command="cli show system statistics icmp6 | grep -e \"Max Public ND\"")
    re3 = re.search('\d+', op3.text)
    obj3 = int(re3.group())
    return ({'fields': {"ndpcache_public_cnt": obj1, "ndpcache_public_drop_cnt": obj2, "ndpcache_public_max_cnt": obj3}})
