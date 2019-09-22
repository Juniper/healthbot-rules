import re

def run():
    dev = __proxy__['junos.conn']()
    output = dev.rpc.request_shell_execute(command = "cli show system alarms")
    op = re.search('slow peers are: ((\s?[a-zA-Z]\s?)+)\n$', output.text)
    if op:
        return ({'fields':{"stuck_client_info": op.group()}}) 
    else:
        return ({'fields':{"stuck_client_info": output.text.replace("\n"," ")}})
    
 
