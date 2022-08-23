'''
which_pfe.py - This library contains methods maps the PICS & PORTS to the PFE :

    which_pfe()  - This function maps the PICS & PORTS to the PFE
    
'''
'''-----------------------------------------------------------------------------
    which_pfe()  - This function maps the PICS & PORTS to the PFE
    
    Input: 
         fpc_type   - fpc type
         fpc_no     - fpc number
         pic_no     - pic number
         port_no    - port number
    Output:
         PFE name
-----------------------------------------------------------------------------'''


import re

global port_str

def which_pfe(fpc_type,fpc_no, pic_no, port_no, **kwargs):
    
    global port_str
 
    # code will match any FPC as long as its the suffix of string returned from sensor or its within brackets
    match = re.search(r'((LC|MPC|Virtual)+[^]]*)', str(fpc_type))
    try:
        fpc = match.group(1)
    except:
        return 0

    #create a string of FPC/PIC/PORT  
    port_str = str(fpc_no)+str(pic_no)+str(port_no)

    # create a switch case statement to run different methods based on FPC type
    # port mapping defined within each method
    cases = {
    "Virtual FPC": fpc_type_0,
    "MPCE Type 2 3D" : fpc_type_1,                      # MPC2E, 
    "MPCE Type 2 3D Q" : fpc_type_1,                    # MPC2E-Q, 
    "MPCE Type 2 3D EQ": fpc_type_1,                    # MPC2E-EQ
    "MPCE Type 3 3D" : fpc_type_2,                      # MPC3E
    "MPC2E NG PQ & Flex Q" : fpc_type_2,                # NG-MPC2E        
    "MPC2E NG HQoS" : fpc_type_2,                       # NG-MPC2EQ    
    "MPC3E NG PQ & Flex Q" : fpc_type_2,                # NG-MPC3E  
    "MPC3E NG HQoS" : fpc_type_2,                       # NG-MPC3E-Q
    "MPC5E 3D 24XGE+6XLGE" : fpc_type_3,                # MPC5E
    "MPC5E 3D 2CGE+4XGE" : fpc_type_4,                  # MPC5E type 2
    "MPC7E-MRATE" : fpc_type_5,                         # MPC7E       
    "MPC7E-10G" : fpc_type_5,                           # MPC7E
    "MPC7E 3D 40XGE" : fpc_type_5,                      # MPC7E
    "MPC7E 3D MRATE-12xQSFPP-XGE-XLGE-CGE" : fpc_type_5,# MPC7E  
    "MPC7E 40x10GE Mezz" : fpc_type_5,                  # MPC7E            
    "MPC7E-10G LQ" : fpc_type_5,                        # MPC7E            
    "MPC7E-MRATE LQ" : fpc_type_5,                      # MPC7E
    "MPC7E-10G HMC-2G" : fpc_type_5,                    # MPC7E          
    "MPC7E-MRATE HMC-2G" : fpc_type_5,                  # MPC7E         
    "MPC7E-10G HMC-2G LQ" : fpc_type_5,                 # MPC7E          
    "MPC7E-MRATE HMC-2G LQ" : fpc_type_5,               # MPC7E
    "LC2103" : fpc_type_6                               # summit
    }
  
    pfe_map = cases.get(fpc, not_supported)

    pfe=pfe_map()

    return pfe
# Virtual FPC -- modeling after MPC2E 
# includes 40x1GE(0), 20x1GE(1), 2x10GE(2), 4x10GE(3)
def fpc_type_0(): 
    global port_str
    
    port_group1 = ['0', '1'] #based on pics for this fpc
    port_group2 = ['2', '3']

    #access the 2nd part of Port_str which is the pic number and match 
    if (port_str[1] in port_group1):
        return 'PFE0'
    elif (port_str[1] in port_group2):
        return 'PFE1'

# MPC2E, MPC2E-Q, MPC2E-EQ
def fpc_type_1():
    global port_str
    
    port_group1 = ['0', '1'] #based on pics for this fpc
    port_group2 = ['2', '3']

    if (port_str[1] in port_group1):
        return 'PFE0'
    elif (port_str[1] in port_group2):
        return 'PFE1'

# MPC3E, NG-MPC2E, NG-MPC2EQ, NG-MPC3E, NG-MPC3E-Q 
# 1 PFE
def fpc_type_2():
    return 'PFE0'
    

#MPC5E type 1
def fpc_type_3():
    global port_str
    
    port_group1 = ['0', '2'] #based on pics for this fpc
    port_group2 = ['1', '3']

    if (port_str[1] in port_group1):
        return 'PFE0'
    elif (port_str[1] in port_group2):
        return 'PFE1'

#MPC5E type 2
def fpc_type_4():
    global port_str
    
    port_group1 = ['0', '1'] #based on pics for this fpc
    port_group2 = ['2', '3']

    if (port_str[1] in port_group1):
        return 'PFE0'
    elif (port_str[1] in port_group2):
        return 'PFE1'

#MPC7E
def fpc_type_5():
    global port_str
    
    port_group1 = ['0'] #based on pics for this fpc
    port_group2 = ['1']

    if (port_str[1] in port_group1):
        return 'PFE0'
    elif (port_str[1] in port_group2):
        return 'PFE1'

#LC2103 architecture   
def fpc_type_6():
    global port_str

    port_group1 = ['00', '01', '10', '11', '12', '13'] #based on ports
    port_group2 = ['02', '03', '14', '15', '16', '17']
    port_group3 = ['04', '05', '18', '19', '110', '111']

    #set portstr to be only pic and port numbers 
    portStr = port_str[1:]  
    if (portStr in port_group1):
        return 'PFE0'
    if (portStr in port_group2):
        return 'PFE1'
    if (portStr in port_group3):
        return 'PFE2'

def port_str(fpc, pic, port, **kwargs):
    return str(fpc)+str(pic)+str(port)

def not_supported():
    return 404
