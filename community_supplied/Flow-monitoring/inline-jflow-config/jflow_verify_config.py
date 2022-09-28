from socket import inet_aton
import re

def verify_template_version(index, vty_temp_type, vty_version, config_temp_type, **kwargs):
    index = int(index)
    if (vty_version == "(Jflow-V9)" or vty_version == "(IP-FIX)"):
       if (index == 0):
           if(vty_temp_type == "(IPv4)" and config_temp_type == "ipv4-template"):
               return True
           else:
               return False

       elif (index == 1):
           if (vty_temp_type == "(IPv6)" and config_temp_type == "ipv6-template"):
               return True
           else:
               return False

       elif (index == 3):
           if (vty_temp_type == "(MPLS)" and config_temp_type == "mpls-template"):
               return True
           else:
               return False

       elif (index == 4):
           if (vty_temp_type == "(MPLS-IPv4)" and config_temp_type == "mpls-template"):
               return True
           else:
               return False

       elif (index == 5):
           if (vty_temp_type == "(MPLS-IPv6)" and config_temp_type == "mpls-template"):
               return True
           else:
               return False

    else:
        return False


def verify_tbl_size (target, fpc_num, vty_flow_tbl_size, config_flow_tbl_size, **kwargs):
    fpc_target = "fpc"+fpc_num
    if (target == fpc_target):
        if (config_flow_tbl_size == "0"):
            if (vty_flow_tbl_size == "1024"):
                return True
            else:
                return False
                
        flow_table_size = int(config_flow_tbl_size) * 256 *1024
        if (int(vty_flow_tbl_size) >= flow_table_size):
            return True
        else:
            return False
    

def verify_collector_ip(vty_coll1, vty_coll2, vty_coll3, vty_coll4, cfg_coll, vty_no_of_coll, **kwargs):
    invalid_ip = "0.0.0.0"
    if (int(vty_no_of_coll) == 0 or int(vty_no_of_coll) >4):
        return False;

    if (int(vty_no_of_coll) == 1):
        if (vty_coll1 != invalid_ip and (vty_coll1 == cfg_coll)):
            return True
        else:
            return False

    elif (int(vty_no_of_coll) == 2):
        if (((vty_coll1 != invalid_ip) and (vty_coll2 != invalid_ip))):
            list1 = []
            list1.append(vty_coll1)
            list1.append(vty_coll2)
            list1 = sorted(list1, key=lambda x:tuple(map(int, x.split('.'))))
            coll_ip_str = "[\'"+list1[0]+ "\', \'"+list1[1]+ "\']"

            if (coll_ip_str == cfg_coll):
                return True
            else:
                return False

    elif (int(vty_no_of_coll) == 3):
        if (((vty_coll1 != invalid_ip) and (vty_coll2 != invalid_ip) and (vty_coll3 != invalid_ip))):
            list1 = []
            list1.append(vty_coll1)
            list1.append(vty_coll2)
            list1.append(vty_coll3)
            list1 = sorted(list1, key=lambda x:tuple(map(int, x.split('.'))))
            coll_ip_str = "[\'"+list1[0]+"\', \'"+list1[1]+ "\', \'"+ list1[2]+ "\']"
            if (coll_ip_str == cfg_coll):
                return True
            else:
                return False

    elif (int(vty_no_of_coll) == 4):
        if (((vty_coll1 != invalid_ip) and (vty_coll2 != invalid_ip) and (vty_coll3 != invalid_ip) and (vty_coll4 != invalid_ip))):
            list1 = []
            list1.append(vty_coll1)
            list1.append(vty_coll2)
            list1.append(vty_coll3)
            list1.append(vty_coll4)
            list1 = sorted(list1, key=lambda x:tuple(map(int, x.split('.'))))
            list1.sort()
            coll_ip_str = "[\'"+list1[0]+ "\', \'"+list1[1]+ "\', \'"+ list1[2]+ "\', \'"+ list1[3]+ "\']"
            if (coll_ip_str == cfg_coll):
                return True
            else:
                return False

    else:
        return False

def verify_collector_port(vty_cport1, vty_cport2, vty_cport3, vty_cport4, cfg_port, vty_no_of_coll, **kwargs):
    invalid_port = 0
    if (int(vty_no_of_coll) == 0 or int(vty_no_of_coll) >4):
        return False

    if (int(vty_no_of_coll) == 1):
        if (vty_cport1 == cfg_port):
            return True
        else:
            return False

    elif (int(vty_no_of_coll) == 2):
        list1 = []
        list1.append(vty_cport1)
        list1.append(vty_cport2)
        list1.sort(key=int)
        list2 = re.findall(r"'(.*?)'", cfg_port, re.DOTALL)
        list2.sort(key=int)
        if (list1 == list2):
            return True
        else:
            return False
    
    elif (int(vty_no_of_coll) == 3):
        list1 = []
        list1.append(vty_cport1)
        list1.append(vty_cport2)
        list1.append(vty_cport3)
        list1.sort(key=int)
        list2 = re.findall(r"'(.*?)'", cfg_port, re.DOTALL)
        list2.sort(key=int)
        if (list1 == list2):
            return True
        else:
            return False

    elif (int(vty_no_of_coll) == 4):
        list1 = []
        list1.append(vty_cport1)
        list1.append(vty_cport2)
        list1.append(vty_cport3)
        list1.append(vty_cport4)
        list1.sort(key=int)
        list2 = re.findall(r"'(.*?)'", cfg_port, re.DOTALL)
        list2.sort(key=int)
        if (list1 == list2):
            return True
        else:
            return False

def verify_no_of_collector(cfg_collector, vty_no_of_collector, **kwargs):
    if (int(vty_no_of_collector) == 0 or int(vty_no_of_collector) > 4):
        return False
    list1 = []
    list1 = re.findall(r"'(.*?)'", cfg_collector, re.DOTALL)
    if ((int(vty_no_of_collector) == 1) and (not list1) and (cfg_collector != None)):
        return True
    size = len(list1)
    if (size == int(vty_no_of_collector)):
        return True
    else:
        return False

def verify_jflow_src_addr(vty_src1, vty_src2,vty_src3, vty_src4, cfg_src_ip, vty_no_of_coll, **kwargs):
    invalid_ip = "0.0.0.0"
    num_coll = int(vty_no_of_coll)
    if (num_coll ==0 or num_coll >4):
        return False

    if (num_coll == 1):
        if (vty_src1 != invalid_ip and vty_src1 == cfg_src_ip):
            return True
        else:
            return False

    elif (num_coll ==2):
        if (vty_src1 != invalid_ip and vty_src2 != invalid_ip and (vty_src1 == vty_src2 == cfg_src_ip)):
            return True
        else:
            return False

    elif (num_coll == 3):
        if (vty_src1 != invalid_ip and vty_src2 != invalid_ip and vty_src3 != invalid_ip and (vty_src1 == vty_src2 == vty_src3 == cfg_src_ip)):
            return True
        else:
            return False

    elif (num_coll == 4):
        if (vty_src1 != invalid_ip and vty_src2 != invalid_ip and vty_src3 != invalid_ip and vty_src4 != invalid_ip and (vty_src1 == vty_src2 == vty_src3 == vty_src4 == cfg_src_ip)):
            return True
        else:
            return False



def verify_active_timeout (vty_version, vty_timeout, cfg_active_timeout, **kwargs):
    vty_active_timeout = vty_timeout
    if (vty_version == "(Jflow-V9)" or vty_version == "(IP-FIX)"):
        if (vty_version == "(Jflow-V9)"):
            if (cfg_active_timeout == 0):
                if (vty_active_timeout == 60):
                    return True;
                else:
                    return False;
            else:
                if (int(cfg_active_timeout) == int(vty_active_timeout)):
                    return True;
                else:
                    return False;
        elif (vty_version == "(IP-FIX)"):
            if (cfg_active_timeout == 0):
                if (vty_active_timeout == 60):
                    return True;
                else:
                    return False;
            else:
                if (int(cfg_active_timeout) == int(vty_active_timeout)):
                    return True;
                else:
                    return False;
    else:
        return False;

def verify_inactive_timeout (vty_version, vty_timeout, cfg_inactive_timeout, **kwargs):
    vty_inactive_timeout = vty_timeout
    if (vty_version == "(Jflow-V9)" or vty_version == "(IP-FIX)"):
        if (vty_version == "(Jflow-V9)"):
            if (cfg_inactive_timeout == 0):
                if (vty_inactive_timeout == 60):
                    return True;
                else:
                    return False;
            else:
                if (int(cfg_inactive_timeout) == int(vty_inactive_timeout)):
                    return True;
                else:
                    return False;
        elif (vty_version == "(IP-FIX)"):
            if (cfg_inactive_timeout == 0):
                if (vty_inactive_timeout == 60):
                    return True;
                else:
                    return False;
            else:
                if (int(cfg_inactive_timeout) == int(vty_inactive_timeout)):
                    return True;
                else:
                    return False;
    else:
        return False;

