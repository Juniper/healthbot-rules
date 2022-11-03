"""
Function to verify if the sampling instance is binded to the respective fpc
@param target fpc target as specied in vty command
@param fpc_num fpc number as obtained from RE config
@param cfg_inst_name instance name in RE CLI
@param vty_inst_name instance name as cfg in vty output

@return true if valid false otherwise
"""

from __future__ import division

def check_fpc(target, fpc_num, cfg_inst_name, vty_inst_name, **kwargs):
    vty_fpc_target = 'fpc'+str(fpc_num)
    if (target == vty_fpc_target):
        if(cfg_inst_name == vty_inst_name):
            return True
        else:
            return False
    return False
