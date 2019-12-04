import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="cli show system statistics arp | grep -e \"Current Public ARP\"")
    re1 = re.search('\d+', op1.text)
    obj1 = int(re1.group())
    op2 = dev.rpc.request_shell_execute(command="cli show system statistics arp | grep -e \"public limit reached\"")
    re2 = re.search('\d+', op2.text)
    obj2 = int(re2.group())
    op3 = dev.rpc.request_shell_execute(command="cli show system statistics arp | grep -e \"Max Public ARP\"")
    re3 = re.search('\d+', op3.text)
    obj3 = int(re3.group())
    return ({'fields': {"arpcache_public_cnt": obj1, "arpcache_public_drop_cnt": obj2, "arpcache_public_max_cnt": obj3}})
