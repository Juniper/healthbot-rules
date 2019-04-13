""" script to determine whether the network services mode is in sync
    across config/cli/sysctl/fpc
"""
import re
import sys
import logging
import jnpr.junos

# create logger for this script
LOGGER = logging.getLogger('netsvc.py')
LOGGER.setLevel(logging.DEBUG)
CH = logging.StreamHandler()
CH.setLevel(logging.DEBUG)
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              '%Y-%m-%d %H:%M:%S')
CH.setFormatter(FORMATTER)
LOGGER.addHandler(CH)

# create root level logger for debugging pyez/ncclient
# comment out if not troubleshooting
# logging.basicConfig(level=logging.INFO)


def re_conf(dev, model, routing_engine=None, vc=None, member=None, member_bre=None):
    """ gets the config for 'show chassis network-services'
        converts this string to int which maps to the enum in
        chassis_network_services_t
        Args:
            dev(obj): pyez connection to device
            model(str): router model name
            routing_engine(str): denotes which RE to run cmd on (opt)
            vc(bool): True if chassis is part of a VC (opt)
            member(list): which vc member to connect to (opt)
            member_bre(int): backup RE in VC member to connect to (opt)
        Returns:
            ret(str): maps to network-services mode
        Raises:
            exception upon pyez error
    """
    LOGGER.debug('routing-engine=%s, vc=%s, member=%s, member_bre=%s',
                 routing_engine, vc, member, member_bre)
    cmd = "cli -c 'show configuration chassis network-services | display inheritance | except #'"
    config = []
    if routing_engine:
        op_cli = dev.rpc.request_shell_execute(routing_engine=routing_engine,
                                               command=cmd)
        if hasattr(op_cli, 'xpath'):
            config = op_cli.xpath('./multi-routing-engine-item/output')
    elif vc and len(member) == 1 and member_bre is not None:
        bre_cmd = 'rsh -Ji member{}-re{} "{}"'.format(member[0], member_bre, cmd)
        op_cli = dev.rpc.request_shell_execute(command=bre_cmd)
        if hasattr(op_cli, 'xpath'):
            config = op_cli.xpath('.')
    elif vc and len(member) == 1:
        op_cli = dev.rpc.request_shell_execute(member=member[0],
                                               command=cmd)
        if hasattr(op_cli, 'xpath'):
            config = op_cli.xpath('./multi-routing-engine-item/output')
    elif vc and not member:
        config.append(False)
    else:
        op_cli = dev.rpc.request_shell_execute(command=cmd)
        if hasattr(op_cli, 'xpath'):
            config = op_cli.xpath('.')

    if len(config) == 1:
        if config[0] is False:
            ret = False
        if re.search(r'network-services ip', config[0].text):
            ret = '0'
        elif re.search(r'network-services ethernet', config[0].text):
            ret = '1'
        elif re.search(r'network-services enhanced-ip', config[0].text):
            ret = '2'
        elif re.search(r'network-services enhanced-ethernet', config[0].text):
            ret = '3'
        elif re.search(r'network-services enhanced-mode', config[0].text):
            ret = '6'
        elif re.search(r'network-services lan', config[0].text):
            ret = '7'
    else:
        if re.search(r'MX5|MX40|MX80|MX150|MX204', model):
            ret = '2'  # defaults to enhanced-ip
        elif re.search(r'MX', model):
            ret = '0'  # defaults to IP
        elif re.search(r'T4000', model):
            ret = '0'  # non-enhanced mode
        elif re.search(r'PTX1000', model):
            ret = '6'  # defaults to enhanced, regex also matches ptx10k
        elif re.search(r'PTX', model):
            ret = '0'  # Normal-Mode

    return ret


def re_cli(dev, model, routing_engine=None, vc=None, member=None, member_bre=None):
    """ gets the cli cmd output  for 'show chassis network-services'
        converts this string to int which maps to the enum in
        chassis_network_services_t
        only required to collect from master re in chassis/vc
        Args:
            dev(obj): pyez connection to device
            model(str): model name
            routing_engine(str): denotes which RE to run cmd on (opt)
            vc(bool): True if chassis is part of a VC (opt)
            member(list): denotes which vc member to connect to (opt)
            member_bre(int): denotes which vc member RE is backup (opt)
        Returns:
            ret(str): maps to network-services mode
        Raises:
            exception upon pyez error
    """
    cmd = "cli -c 'show chassis network-services'"
    if routing_engine:
        op_cli = dev.rpc.request_shell_execute(routing_engine=routing_engine,
                                               command=cmd)
        cli = op_cli.xpath('./multi-routing-engine-item/output')[0].text
    elif member and member_bre is not None:
        bre_cmd = 'rsh -Ji member{}-re{} "{}"'.format(member[0], member_bre, cmd)
        op_cli = dev.rpc.request_shell_execute(command=bre_cmd)
        if hasattr(op_cli, 'xpath'):
            cli = op_cli.xpath('.')
    elif member:
        op_cli = dev.rpc.request_shell_execute(member=member[0],
                                               command=cmd)
        cli = op_cli.xpath('./multi-routing-engine-item/output')[0].text
    elif not vc:
        op_cli = dev.rpc.request_shell_execute(command=cmd)
        cli = op_cli.xpath('.')[0].text

    if re.search(r'Network Services Mode: Normal-Mode', cli):
        ret = '0'
    elif re.search(r'Network Services Mode: IP', cli):
        ret = '0'
    elif re.search(r'Network Services Mode: Ethernet', cli):
        ret = '1'
    elif re.search(r'Network Services Mode: Enhanced-IP', cli):
        ret = '2'
    elif re.search(r'Network Services Mode: Enhanced-Ethernet', cli):
        ret = '3'
    elif re.search(r'Network Services Mode: Enhanced-Mode', cli):
        ret = '6'
    elif re.search(r'Network Services Mode: Lan', cli):
        ret = '7'
    elif re.search(r'T4000', model):
        ret = None

    return ret


def re_sysctl(dev, sysctl_str, routing_engine=None, vc=None, member=None, member_bre=None):
    """ retrieves a sysctl value
        if net.netsvc, must be collected from all RE's in the chassis/vc
        Args:
            dev(obj): pyez connection to device
            sysctl_str(str): which sysctl to check
            routing_engine(str): denotes which RE to run cmd on (opt)
            vc(bool): True if chassis is part of a VC (opt)
            member(list): denotes which vc member is master (opt)
            member_bre(int): denotes which vc member RE is backup (opt)
        Returns:
            ret(str): maps to network-services mode
        Raises:
            exception upon pyez error
    """
    cmd = 'sysctl {}'.format(sysctl_str)
    if routing_engine:
        op_shell = dev.rpc.request_shell_execute(routing_engine=routing_engine,
                                                 command=cmd)
        sysctl = op_shell.xpath('./multi-routing-engine-item/output')[0].text
    elif member and member_bre is not None:
        bre_cmd = 'rsh -Ji member{}-re{} "{}"'.format(member[0], member_bre, cmd)
        op_shell = dev.rpc.request_shell_execute(command=bre_cmd)
        if hasattr(op_shell, 'xpath'):
            sysctl = op_shell.xpath('.')
    elif member:
        op_shell = dev.rpc.request_shell_execute(member=member[0],
                                                 command=cmd)
        sysctl = op_shell.xpath('./multi-routing-engine-item/output')[0].text
    elif not vc:
        op_shell = dev.rpc.request_shell_execute(command=cmd)
        sysctl = op_shell.xpath('.')[0].text
    ret = re.sub(r'{}: '.format(sysctl_str), '', sysctl).strip('\n')

    return ret


def fpc_list(dev, model, hardware, vcm=None, vcb=None):
    """ gets the list of fpcs online in the chassis
        Args:
            dev(obj): pyez connection to device
            model(str): router model name
            hardware(obj): output from get_chassis_inventory() rpc
            vcm(list): member id of vcm (opt)
            vcb(list): member id of vcb (opt)
        Returns:
            online_fpcs(list): which fpc slots are online
            command(str): model specific fpc cmd
        Raises:
            exception upon pyez error
    """
    online_fpcs = []
    feb = None
    trio = None
    paradise = None

    op_fpc = dev.rpc.get_fpc_information()

    try:
        feb = hardware.xpath('./chassis/chassis-module[(description) '
                             '= "Forwarding Engine Processor"]/name')[0].text
    except IndexError:
        pass

    if vcm:
        vcm_slots = op_fpc.xpath('./multi-routing-engine-item[(re-name) = "member{}"]/'
                                 'fpc-information/fpc[(state) = "Online"]/slot'.format(vcm[0]))
        if not vcm_slots:
            LOGGER.warning('There are no FPCs currently online in VCm')
    if vcb:
        vcb_slots = op_fpc.xpath('./multi-routing-engine-item[(re-name) = "member{}"]/'
                                 'fpc-information/fpc[(state) = "Online"]/slot'.format(vcb[0]))
        if not vcb_slots:
            LOGGER.warning('There are no FPCs currently online in VCb')
    if not (vcm or vcb or feb):
        slots = op_fpc.xpath('./fpc[normalize-space(state) = "Online"]/slot')
        if not slots:
            LOGGER.warning('There are no FPCs currently online')

    if feb:
        fpc_type = re.sub(r' 0', '', feb).lower()
        online_fpcs.append('{}0'.format(fpc_type))
        trio = True
    elif re.search('MX', model):
        fpc_string = 'MPC|JNP.*'
        trio = True
    elif re.search('PTX', model):
        fpc_string = 'FPC|PTX.*|LC.*'
        paradise = True
    elif re.search('T4000', model):
        fpc_string = 'FPC Type 5'
        type5 = True

    if trio:
        command = 'show jnh 0 vc mc state'
    elif paradise:
        command = 'show shim fpc enh-mode'
    elif type5:
        command = 'show luchip 0 ppe 0 ppe_cfg'

    if vcm:
        for slot in vcm_slots:
            fru = hardware.xpath('./multi-routing-engine-item[(re-name) = "member{}"]/'
                                 'chassis-inventory/chassis/chassis-module[(name) = "FPC {}"]/'
                                 'description'.format(vcm[0], slot.text))[0].text
            LOGGER.debug(fru)
            if re.match(r'^({})'.format(fpc_string), fru):
                online_fpcs.append('member{}-fpc{}'.format(vcm[0], slot.text))

    if vcb:
        for slot in vcb_slots:
            fru = hardware.xpath('./multi-routing-engine-item[(re-name) = "member{}"]/'
                                 'chassis-inventory/chassis/chassis-module[(name) = "FPC {}"]/'
                                 'description'.format(vcb[0], slot.text))[0].text
            LOGGER.debug(fru)
            if re.match(r'^({})'.format(fpc_string), fru):
                online_fpcs.append('member{}-fpc{}'.format(vcb[0], slot.text))

    if not (vcm or vcb or feb):
        for slot in slots:
            fru = hardware.xpath('./chassis/chassis-module[normalize-space(name) '
                                 '= "FPC {}"]/description'
                                 .format(slot.text))[0].text
            LOGGER.debug(fru)
            if re.match(r'^({})'.format(fpc_string), fru):
                online_fpcs.append('fpc{}'.format(slot.text))

    return online_fpcs, command


def query_fpc(dev, fpc, command):
    """ determines whether an fpc is running in enhanced mode
        Args:
            dev(obj): pyez connection to device
            fpc(str): fpc identifier
            command(str): command to run on fpc
        Returns:
            ret(bool): whether fpc is in enhanced mode or not
        Raises:
            exception upon pyez error
    """
    op_pfe = dev.rpc.request_pfe_execute(target=fpc, command=command)
    output = op_pfe.text

    if re.search(r'static mcast mode: TRINITY-ONLY', output) or \
        re.search(r'ENH-MODE: paradise mode', output) or \
        re.search(r'ppe_img_name:      _ucode_lu_tseries_enh_top', output):
        ret = True
    elif re.search(r'Syntax error', output):
        ret = None
    else:
        ret = False

    return ret


def is_vc(dev, op_re):
    """ determines whether an fpc is running in enhanced mode
        Args:
            dev(obj): pyez connection to device
            re_info(obj): get_route_engine_information() rpc output
        Returns:
            ret(bool): True if chassis is part of a VC
            vcm(list): which member is the VCm
            vcmm(int): which RE is the VCmM
            vcmb(int): which RE is the VCmB
            vcb(list): which member is the VCb
            vcbm(int): which RE is the VCbM
            vcbb(int): which RE is the VCbB
        Raises:
            None
    """
    rpc_fail = False
    ret = None
    vcm, vcmm, vcmb, vcb, vcbm, vcbb = [], None, None, [], None, None
    #op_vc = dev.rpc.get_virtual_chassis_information()
    try:
        op_vc = dev.rpc.get_virtual_chassis_information()
    except jnpr.junos.exception.RpcError:
        # single RE models like PTX1000 will hit this
        ret = False
        rpc_fail = True

    root = amiroot(dev)

    if not rpc_fail:
        vc_xpath = op_vc.xpath('./member-list/member[starts-with(member-role, "Master")]/member-id')
        if len(vc_xpath) == 1:
            ret = True
            vcm.append(vc_xpath[0].text)
            re_xpath = op_re.xpath('./multi-routing-engine-item[(re-name) = "member{}"]'
                                   '/route-engine-information/route-engine[(mastership-state)'
                                   '= "master"]/slot'.format(vcm[0]))
            if len(re_xpath) == 1:
                vcmm = re_xpath[0].text
            re_xpath = op_re.xpath('./multi-routing-engine-item[(re-name) = "member{}"]'
                                   '/route-engine-information/route-engine[(mastership-state)'
                                   '= "backup"]/slot'.format(vcm[0]))
            if len(re_xpath) == 1 and root:
                vcmb = re_xpath[0].text
        else:
            LOGGER.info('VCm isnt reachable')

        vc_xpath = op_vc.xpath('./member-list/member[starts-with(member-role, "Backup")]/member-id')
        if len(vc_xpath) == 1:
            ret = True
            vcb.append(vc_xpath[0].text)
            re_xpath = op_re.xpath('./multi-routing-engine-item[(re-name) = "member{}"]'
                                   '/route-engine-information/route-engine[(mastership-state)'
                                   '= "master"]/slot'.format(vcb[0]))
            if len(re_xpath) == 1:
                vcbm = re_xpath[0].text
            re_xpath = op_re.xpath('./multi-routing-engine-item[(re-name) = "member{}"]'
                                   '/route-engine-information/route-engine[(mastership-state)'
                                   '= "backup"]/slot'.format(vcb[0]))
            if len(re_xpath) == 1 and root:
                vcbb = re_xpath[0].text
        else:
            LOGGER.info('VCb inst reachable')

    return ret, vcm, vcmm, vcmb, vcb, vcbm, vcbb


def list_res(op_re, vcm, vcb):
    """ gets a list of routing-engines
        Args:
            op_re(obj): get_route_engine_information() rpc output
            vcm(list): which member is the VCm
            vcb(list): which member is the VCb
        Returns:
            ret(list): routing-engines in the chassis/vc
        Raises:
            None
    """
    ret = []
    if vcm:
        vcm_re_list = op_re.xpath('./multi-routing-engine-item[(re-name) = "member{}"]'
                                  '/route-engine-information/route-engine/slot'.format(vcm[0]))
        for routing_engine in vcm_re_list:
            ret.append('member{}-re{}'.format(vcm[0], routing_engine.text))
    if vcb:
        vcb_re_list = op_re.xpath('./multi-routing-engine-item[(re-name) = "member{}"]'
                                  '/route-engine-information/route-engine/slot'.format(vcb[0]))
        for routing_engine in vcb_re_list:
            ret.append('member{}-re{}'.format(vcb[0], routing_engine.text))
    if not vcm and not vcb:
        chassis_re_list = op_re.xpath('./route-engine[(mastership-state) != "Present"]/slot')
        for routing_engine in chassis_re_list:
            ret.append('re{}'.format(routing_engine.text))

        if not chassis_re_list:
            ret.append('re0')
    return ret


def verify_model(op_hw):
    """ Determines whether model string is a supported model
        Args:
            op_hw(obj): output from get_chassis_inventory() rpc
        Returns:
            ret(str): model name if supported, None if not
        Raises:
            None
    """
    model = op_hw.xpath('//chassis/description')[0].text
    LOGGER.debug('model = %s', model)

    if re.search('MX|PTX|T4000', model):
        ret = model
    else:
        ret = None

    return ret

def amiroot(dev):
    """ Checks if we are root user or not
        Args: dev(obj): pyez connection to device
        Returns: True if we are root, False if not
        Raises: None
    """
    result = False
    op_cli = dev.rpc.request_shell_execute(command="/usr/bin/whoami")
    if hasattr(op_cli, 'xpath'):
        user = op_cli.xpath('.')
        result = bool(user[0].text.strip('\n') == 'root')
    return result


def run():
    """ core of program. not called main() because iAgent sensor config uses
        Salt which requires run()
    """
    netsvc_sync = True
    proposed_action = 'no action required'
    action_list = ['request system reboot',  #0
                   'request system reboot both-routing-engines',  #1
                   'request system reboot other-routing-engine',  #2
                   'request system reboot member {} both-routing-engines',  #3
                   'request system reboot member {} other-routing-engine',  #4
                   'request system reboot all-members both-routing-engines',  #5
                   'commit synchronize'] #6
    gres_enabled = None
    dev = __proxy__['junos.conn']()

    # script uses this RPC extensively, supported from 14.1+
    try:
        dev.rpc.request_shell_execute(command='ls')
    except jnpr.junos.exception.RpcError:
        LOGGER.error('junos version does not support "request-shell-execute" rpc, exiting')
        sys.exit(1)

    op_hw = dev.rpc.get_chassis_inventory()
    if re.match(r'Aborted!', op_hw.xpath('.')[0].text):
        LOGGER.error('Please connect to the Master RE')
        sys.exit(1)

    # confirm model is supported by this script
    model = verify_model(op_hw)

    if not model:
        LOGGER.error('product model not supported by this script. Only MX/PTX/T4000')
        sys.exit(1)

    op_re = dev.rpc.get_route_engine_information()

    # determine if vc, and if so which member is master, and which is VCmM, VCbM
    vc, vcm, vcmm, vcmb, vcb, vcbm, vcbb = is_vc(dev, op_re)
    LOGGER.debug('vc = %s, vcm = %s, vcmm = %s, vcmb = %s, vcb = %s, vcbm = %s, vcbb = %s',
                 vc, vcm, vcmm, vcmb, vcb, vcbm, vcbb)

    # determine list of RE's
    re_list = list_res(op_re, vcm, vcb)
    LOGGER.debug('re_list = %s', re_list)

    if vc:
        # check if gres enabled on vcb
        vcb_gres_enabled = re_sysctl(dev, 'hw.re.is_slave_peer_gres_ready',
                                     routing_engine=None,
                                     vc=vc, member=vcm, member_bre=None)
        # check if gres enabled on vcmb
        vcm_local_gres_enabled = re_sysctl(dev, 'hw.re.is_local_slave_peer_gres_ready',
                                           routing_engine=None,
                                           vc=vc, member=vcm, member_bre=None)
        # check if gres enabled on vcbb
        vcb_local_gres_enabled = re_sysctl(dev, 'hw.re.is_local_slave_peer_gres_ready',
                                           routing_engine=None,
                                           vc=vc, member=vcb, member_bre=None)

        if (vcb_gres_enabled == '1' and vcm_local_gres_enabled == '1' and
                vcb_local_gres_enabled == '1'):
            gres_enabled = True

        # check VCmM configuration
        vcm_config = re_conf(dev, model, None, vc, vcm, None)
        LOGGER.debug('vcm_config = %s', vcm_config)
        if not vcm_config:
            LOGGER.info('cant connect to the VCm for config check')
        # check VCbM configuration
        vcb_config = re_conf(dev, model, None, vc, vcb, None)
        LOGGER.debug('vcb_config = %s', vcb_config)
        if not vcb_config:
            LOGGER.info('cant connect to the VCb for config check')
        # check VCmM cli cmd
        vcm_cli = re_cli(dev, model, None, vc, vcm, None)
        LOGGER.debug('vcm_cli = %s', vcm_cli)
        if not vcm_cli:
            LOGGER.info('cant connect to the VCm for cli check')
        # check VCbM cli cmd
        vcb_cli = re_cli(dev, model, None, vc, vcb, None)
        LOGGER.debug('vcb_cli = %s', vcb_cli)
        if not vcb_cli:
            LOGGER.info('cant connect to the VCb for cli check')
        # check VCmM RE sysctl
        vcm_sysctl = re_sysctl(dev, 'net.netsvc', None, vc, vcm, None)
        LOGGER.debug('vcm_sysctl = %s', vcm_sysctl)
        if not vcm_sysctl:
            LOGGER.info('cant connect to the VCm for sysctl check')
        # check VCbM RE sysctl
        vcb_sysctl = re_sysctl(dev, 'net.netsvc', None, vc, vcb, None)
        LOGGER.debug('vcb_sysctl = %s', vcb_sysctl)
        if not vcb_sysctl:
            LOGGER.info('cant connect to the VCb for sysctl check')

        vcmb_config, vcmb_cli, vcmb_sysctl = None, None, None
        # vcmb can only be set if we are root user
        if vcmb is not None:
            #check VCmB configuration
            vcmb_config = re_conf(dev, model, None, vc, vcm, vcmb)
            LOGGER.debug('vcmb_config = %s', vcmb_config)
            if not vcmb_config:
                LOGGER.info('cant connect to the VCmB for config check')
            # check VCmB cli cmd
            vcmb_cli = re_cli(dev, model, None, vc, vcm, vcmb)
            LOGGER.debug('vcmb_cli = %s', vcmb_cli)
            if not vcmb_cli:
                LOGGER.info('cant connect to the VCmB for cli check')
            # check VCmB RE sysctl
            vcmb_sysctl = re_sysctl(dev, 'net.netsvc', None, vc, vcm, vcmb)
            LOGGER.debug('vcmb_sysctl = %s', vcmb_sysctl)
            if not vcmb_sysctl:
                LOGGER.info('cant connect to the VCmB for sysctl check')

        vcbb_config, vcbb_cli, vcbb_sysctl = None, None, None
        # vcbb can only be set if we are root user
        if vcbb is not None:
            #check VCbB configuration
            vcbb_config = re_conf(dev, model, None, vc, vcb, vcbb)
            LOGGER.debug('vcbb_config = %s', vcbb_config)
            if not vcbb_config:
                LOGGER.info('cant connect to the VCbB for config check')
            # check VCbB cli cmd
            vcbb_cli = re_cli(dev, model, None, vc, vcb, vcbb)
            LOGGER.debug('vcbb_cli = %s', vcbb_cli)
            if not vcbb_cli:
                LOGGER.info('cant connect to the VCbB for cli check')
            # check VCbB RE sysctl
            vcbb_sysctl = re_sysctl(dev, 'net.netsvc', None, vc, vcb, vcbb)
            LOGGER.debug('vcbb_sysctl = %s', vcbb_sysctl)
            if not vcbb_sysctl:
                LOGGER.info('cant connect to the VCbB for sysctl check')

        # have to order based on increasing severity of action

        # reboot VCmB RE
        if gres_enabled and vcm_config and vcmb_cli and vcm_config != vcmb_cli:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCmB "show chassis network-services" '
                         'cmd output is not in sync. '
                         'Please reboot VCmB RE now!')
            proposed_action = action_list[4].format(vcm[0])
        if gres_enabled and vcm_config and vcmb_sysctl and vcm_config != vcmb_sysctl:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCmB net.netsvc sysctl is not in sync. '
                         'Please reboot VCmB RE now!')
            proposed_action = action_list[4].format(vcm[0])

        # sync config and reboot VCmB RE
        if gres_enabled and vcm_config and vcmb_config and vcm_config != vcmb_config:
            netsvc_sync = False
            LOGGER.error('VCmM and VCmB network-services configuration is not '
                         'in sync. Please sync configurations and reboot VCmB '
                         'RE now!')
            proposed_action = action_list[6] + ' && ' + action_list[4].format(vcm[0])

        # reboot VCbB RE
        if vcm_config and vcbb_sysctl and vcm_config != vcbb_sysctl:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCbB net.netsvc sysctl is not in sync. '
                         'Please reboot VCbB RE now!')
            proposed_action = action_list[4].format(vcb[0])

        if gres_enabled and vcm_config and vcbb_cli and vcm_config != vcbb_cli:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCbB "show chassis network-services" '
                         'cmd output is not in sync. '
                         'Please reboot VCbB RE now!')
            proposed_action = action_list[4].format(vcb[0])

        # sync config and reboot VCbB RE
        if gres_enabled and vcm_config and vcbb_config and vcm_config != vcbb_config:
            netsvc_sync = False
            LOGGER.error('VCmM and VCbB network-services configuration is not '
                         'in sync. Please sync configurations and reboot VCbB '
                         'RE now!')
            proposed_action = action_list[6] + ' && ' + action_list[4].format(vcb[0])

        # reboot both RE on VCb
        if gres_enabled and vcm_config and vcb_cli and vcm_config != vcb_cli:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCbM "show chassis network-services" '
                         'cmd output is not in sync. '
                         'Please reboot both RE on VCb now!')
            proposed_action = action_list[3].format(vcb[0])

        if gres_enabled and vcm_config and vcb_sysctl and vcm_config != vcb_sysctl:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCbM net.netsvc sysctl is not in sync. '
                         'Please reboot both RE VCb now!')
            proposed_action = action_list[3].format(vcb[0])

        # sync config and reboot both RE on VCb
        if gres_enabled and vcm_config and vcb_config and vcm_config != vcb_config:
            netsvc_sync = False
            LOGGER.error('VCmM and VCbM network-services configuration is not '
                         'in sync. Please sync configurations and reboot both '
                         'RE on VCb now!')
            proposed_action = action_list[6] + ' && ' + action_list[3].format(vcb[0])

        # reboot VC
        if vcm_config and vcm_cli and vcm_config != vcm_cli:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCmM "show chassis network-services" '
                         'cmd output is not in sync. '
                         'Please reboot both RE on all VC members now!')
            proposed_action = action_list[5]
        if vcm_config and vcm_sysctl and vcm_config != vcm_sysctl:
            netsvc_sync = False
            LOGGER.error('VCmM config and VCmM net.netsvc sysctl is not in sync. '
                         'Please reboot both RE on all VC members now!')
            proposed_action = action_list[5]



    elif len(re_list) > 1:
        # check if gres enabled
        gres_enabled = re_sysctl(dev, 'hw.re.is_slave_peer_gres_ready',
                                 routing_engine='master',
                                 vc=None, member=None, member_bre=None)
        LOGGER.debug('gres_enabled = %s', gres_enabled)
        # check master RE configuration
        mre_config = re_conf(dev, model, routing_engine='master',
                             vc=None, member=None, member_bre=None)
        LOGGER.debug('mre_config = %s', mre_config)
        # check backup RE configuration
        bre_config = re_conf(dev, model, routing_engine='backup',
                             vc=None, member=None, member_bre=None)
        LOGGER.debug('bre_config = %s', bre_config)
        # check master RE cli cmd
        mre_cli = re_cli(dev, model, routing_engine='master',
                         vc=None, member=None, member_bre=None)
        LOGGER.debug('mre_cli = %s', mre_cli)
        # check backup RE cli cmd
        bre_cli = re_cli(dev, model, routing_engine='backup',
                         vc=None, member=None, member_bre=None)
        LOGGER.debug('bre_cli = %s', bre_cli)
        # check master RE sysctl
        mre_sysctl = re_sysctl(dev, 'net.netsvc', routing_engine='master',
                               vc=None, member=None, member_bre=None)
        LOGGER.debug('mre_sysctl = %s', mre_sysctl)
        # check backup RE sysctl
        bre_sysctl = re_sysctl(dev, 'net.netsvc', routing_engine='backup',
                               vc=None, member=None, member_bre=None)
        LOGGER.debug('bre_sysctl = %s', bre_sysctl)

        if gres_enabled == '1' and mre_config and bre_config and mre_config != bre_config:
            netsvc_sync = False
            LOGGER.error('master and backup RE network-services '
                         'configuration is not in sync.'
                         'Please sync configuration and reboot backup RE now!')
            proposed_action = "{} && {}".format(action_list[6], action_list[2])
        if gres_enabled == '1' and mre_config != bre_sysctl:
            netsvc_sync = False
            LOGGER.error('master RE config and backup RE net.netsvc sysctl is not in sync')
            proposed_action = action_list[2]
        if gres_enabled == '1' and mre_sysctl != bre_sysctl:
            netsvc_sync = False
            LOGGER.error('master and backup RE net.netsvc sysctl is not in sync')
            proposed_action = action_list[2]
        if gres_enabled == '1' and mre_config != bre_cli:
            netsvc_sync = False
            LOGGER.error('master RE config and backup RE "show chassis '
                         'network-services" cmd output is not in sync')
            proposed_action = action_list[2]
        if mre_config != mre_sysctl:
            netsvc_sync = False
            LOGGER.error('master RE config and master RE net.netsvc sysctl is not in sync')
            proposed_action = action_list[1]
        if mre_config and mre_cli and mre_config != mre_cli:
            netsvc_sync = False
            LOGGER.error('master RE config and master RE "show chassis '
                         'network-services" cmd output is not in sync')
            proposed_action = action_list[1]

    else:
        # check master RE configuration
        mre_config = re_conf(dev, model, routing_engine=None,
                             vc=None, member=None, member_bre=None)
        LOGGER.debug('mre_config = %s', mre_config)
        # check master RE cli cmd
        mre_cli = re_cli(dev, model, routing_engine=None,
                         vc=None, member=None, member_bre=None)
        LOGGER.debug('mre_cli = %s', mre_cli)
        # check master RE sysctl
        mre_sysctl = re_sysctl(dev, 'net.netsvc', routing_engine=None,
                               vc=None, member=None, member_bre=None)
        LOGGER.debug('mre_sysctl = %s', mre_sysctl)

        if mre_config and mre_cli and mre_config != mre_cli:
            netsvc_sync = False
            LOGGER.error('master RE config and master RE "show chassis '
                         'network-services" cmd output is not in sync')
            proposed_action = action_list[0]
        if mre_config and mre_sysctl and mre_config != mre_sysctl:
            netsvc_sync = False
            LOGGER.error('master RE config and master RE net.netsvc sysctl is not in sync')
            proposed_action = action_list[0]

    online_fpcs, command = fpc_list(dev, model, op_hw, vcm, vcb)
    LOGGER.debug('online_fpcs = %s, command = "%s"', online_fpcs, command)

    for fpc in online_fpcs:
        fpc_result = query_fpc(dev, fpc, command)
        if fpc_result != None:
            LOGGER.debug('%s in enhanced mode? %s', fpc, fpc_result)
        if vcb and not vcm:
            if (vcb_sysctl == '2' or vcb_sysctl == '3') and fpc_result is False:
                netsvc_sync = False
                LOGGER.error('%s is not in sync with VCbM network-services setting', fpc)
                proposed_action = action_list[3].format(vcb[0])
                break
        elif vcm:
            if (vcm_sysctl == '2' or vcm_sysctl == '3') and fpc_result is False:
                netsvc_sync = False
                LOGGER.error('%s is not in sync with VCmM network-services setting', fpc)
                proposed_action = action_list[5]
                break
        else:
            if (mre_sysctl == '2' or mre_sysctl == '3' or mre_sysctl == '6') and fpc_result is False:
                netsvc_sync = False
                LOGGER.error('%s is not in sync with master RE network-services setting', fpc)
                proposed_action = action_list[1]
                break

    if netsvc_sync:
        LOGGER.info('Network services is in sync')
    else:
        LOGGER.error('Network services is NOT in sync')
    LOGGER.info('netsvc_sync = %s, proposed_action = %s', netsvc_sync, proposed_action)
    return ({'fields': {"netsvc_sync": netsvc_sync, "proposed_action": proposed_action}})
