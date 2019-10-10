import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="cli show system statistics arp | grep -e \"Current Management ARP\"")
    re1 = re.search('\d+', op1.text)
    obj1 = int(re1.group())
    op2 = dev.rpc.request_shell_execute(command="cli show system statistics arp | grep -e \"mgt limit reached\"")
    re2 = re.search('\d+', op2.text)
    obj2 = int(re2.group())
    op3 = dev.rpc.request_shell_execute(command="cli show system statistics arp | grep -e \"Max Management intf ARP\"")
    re3 = re.search('\d+', op3.text)
    obj3 = int(re3.group())
    return ({'fields': {"arpcache_mgmt_cnt": obj1, "arpcache_mgmt_drop_cnt": obj2, "arpcache_mgmt_max_cnt": obj3}})
