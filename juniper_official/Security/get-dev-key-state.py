import re
import jnpr.junos

"""
This function will run /usr/sbin/check-secureboot-status.sh
on the host and check if the development keys have been revoked.
This is achieved by calling efi-updatevar on the host.

This function will return the following values and a msg
0 : Green, "Juniper Dev keys are not revoked. Doing nothing"
           "Dev key revocation status: Success"
1 : Yellow, "State of Development keys unknown" (Fallthrough case)
2 : Red, "Dev key revocation status: Failure"

Note: "Dev key revocation status: ?" would appear very rarely. Success would
only appear once when command is issues. "Failure" could appear continuously,
so the user would likely want to know if the revocation command was issued but
there are still keys that need to be revoked.
"""

def run():
    dev_key_color_result = 1
    dev = __proxy__['junos.conn']()

    """ This rule needs to be run as root """
    root = False
    try:
        op_cli = dev.rpc.request_shell_execute(command="/usr/bin/whoami")
    except jnpr.junos.exception.RpcError:
        dev_key_msg = "feature unsupported"
        return ({'fields':{"sb_color_result": sb_color_result, "dev_key_msg": dev_key_msg}})

    if hasattr(op_cli, 'xpath'):
        user = op_cli.xpath('.')
        root = bool(user[0].text.strip('\n') == 'root')

    if not root:
        dev_key_msg = "Rule must be run as root."
        return ({'fields':{"sb_color_result": sb_color_result, "dev_key_msg": dev_key_msg}})

    op1 = dev.rpc.request_shell_execute(command="/bin/sh /usr/sbin/check-secureboot-status.sh | grep \"Dev Key Revocation Status:\"")
    obj1 = re.search('(?<=: ).*',op1.text)
    dev_key_msg = obj1.group(0)

    if (obj1.group(0) == "Juniper Dev keys are not revoked. Doing nothing"): #Green
        dev_key_color_result = 0
    elif (obj1.group(0) == "Dev key revocation status: Success"): #Green
        dev_key_color_result = 0
    elif (obj1.group(0) == "Dev key revocation status: Failure"): #Red
        dev_key_color_result = 2
    else: #Yellow, fallthrough case
        dev_key_color_result = 1
        dev_key_msg = "State of Development keys unknown"

    return ({'fields':{"dev_key_color_result": dev_key_color_result, "dev_key_msg": dev_key_msg}})
