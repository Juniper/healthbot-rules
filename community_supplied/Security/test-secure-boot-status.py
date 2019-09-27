import re
import jnpr.junos

"""
This function will run /usr/sbin/check-secureboot-status.sh
on the host and pull the relevant secure boot information.

This function will return the following values and a msg
0 : Green, Secure boot status is good, or SB is not available
    on this platform and the rule should be removed.
1 : Yellow, Secure boot status is unknown
2 : Red, Secure boot status is not enabled or not enforced
"""

def run():
    sb_color_result = 1
    dev = __proxy__['junos.conn']()

    """ This rule needs to be run as root """
    root = False
    try:
        op_cli = dev.rpc.request_shell_execute(command="/usr/bin/whoami")
    except jnpr.junos.exception.RpcError:
        sb_msg = "feature unsupported"
        return ({'fields':{"sb_color_result": sb_color_result, "sb_msg": sb_msg}})

    if hasattr(op_cli, 'xpath'):
        user = op_cli.xpath('.')
        root = bool(user[0].text.strip('\n') == 'root')
    
    if not root:
        sb_msg = "Rule must be run as root."
        return ({'fields':{"sb_color_result": sb_color_result, "sb_msg": sb_msg}})

    op1 = dev.rpc.request_shell_execute(command="/bin/sh /usr/sbin/check-secureboot-status.sh | grep \"Secure Boot Status:\"")

    obj1 = re.search('(?<=: ).*',op1.text)
    sb_msg = obj1.group(0)

    if (obj1.group(0) == "Secure Boot is enforced."): #Green
        sb_color_result = 0
    elif (obj1.group(0) == "Secure Boot is either not enabled or not enforced."): #Red
        sb_color_result = 2
    elif (obj1.group(0) == "Secure Boot status is unknown"): #Yellow
        sb_color_result = 1
    else: #Green, fallthrough case
        sb_color_result = 0
        sb_msg = "Secure Boot is not availble on this platform"

    return ({'fields':{"sb_color_result": sb_color_result, "sb_msg": sb_msg}})
