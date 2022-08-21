'''
pfe_count.py - This library contains methods return pfe count based on fpc type:

    pfe_count()  - This function produces pfe count based on fpc type
    
'''
'''-----------------------------------------------------------------------------
    pfe_count()  - This function produces pfe count based on fpc type
    
    Input: 
         fpc_type - fpc type
    Output:
         PFE count based on fpc type
-----------------------------------------------------------------------------'''


import re
import json
        
def pfe_count(fpc_type, **kwargs):

      # code will match any FPC as long as its the suffix of string returned from sensor or its within brackets
    match = re.search(r'((LC|MPC|Virtual)+[^]]*)', str(fpc_type))
    try:
        fpc = match.group(1)
    except:
        return 0

    cases = {
        "Virtual FPC": 2,
        "MPCE Type 2 3D" : 2,                       # MPC2E,         
        "MPCE Type 2 3D Q" : 2,                     # MPC2E-Q, 
        "MPCE Type 2 3D EQ": 2,                     # MPC2E-EQ        
        "MPCE Type 3 3D" : 1,                       # MPC3E            
        "MPC2E NG PQ & Flex Q" : 1,                 # NG-MPC2E          
        "MPC2E NG HQoS" : 1,                        # NG-MPC2EQ        
        "MPC3E NG PQ & Flex Q" : 1,                 # NG-MPC3E         
        "MPC3E NG HQoS" : 1,                        # NG-MPC3E-Q       
        "MPC5E 3D Q 24XGE+6XLGE" : 2,               # MPC5E
        "MPC5E 3D Q 2CGE+4XGE" : 2,                 # MPC5E type 2
        "MPC7E 3D 40XGE" : 2,                       # MPC7E
        "MPC7E 3D MRATE-12xQSFPP-XGE-XLGE-CGE" : 2, # MPC7E    
        "MPC7E 40x10GE Mezz" : 2,                   # MPC7E                       
        "MPC7E-10G LQ" : 2,                         # MPC7E                            
        "MPC7E-MRATE LQ" : 2,                       # MPC7E
        "MPC7E-10G HMC-2G" : 2,                     # MPC7E                        
        "MPC7E-MRATE HMC-2G" : 2,                   # MPC7E                      
        "MPC7E-10G HMC-2G LQ" : 2,                  # MPC7E                     
        "MPC7E-MRATE HMC-2G LQ" : 2,                # MPC7E
        "MPC Type 2 3D" : 2,                        # MPC2E,         # Same variants as above but w/o the E in MPCE
        "MPC Type 2 3D Q" : 2,                      # MPC2E-Q, 
        "MPC Type 2 3D EQ": 2,                      # MPC2E-EQ        
        "MPC Type 3 3D" : 1,                        # MPC3E            
        "MPC2 NG PQ & Flex Q" : 1,                  # NG-MPC2E          
        "MPC2 NG HQoS" : 1,                         # NG-MPC2EQ        
        "MPC3 NG PQ & Flex Q" : 1,                  # NG-MPC3E         
        "MPC3 NG HQoS" : 1,                         # NG-MPC3E-Q       
        "MPC5 3D Q 24XGE+6XLGE" : 2,                # MPC5E
        "MPC5 3D Q 2CGE+4XGE" : 2,                  # MPC5E type 2
        "MPC7 3D 40XGE" : 2,                        # MPC7E
        "MPC7 3D MRATE-12xQSFPP-XGE-XLGE-CGE" : 2,  # MPC7E    
        "MPC7 40x10GE Mezz" : 2,                    # MPC7E                       
        "MPC7-10G LQ" : 2,                          # MPC7E                            
        "MPC7-MRATE LQ" : 2,                        # MPC7E
        "MPC7-10G HMC-2G" : 2,                      # MPC7E                        
        "MPC7-MRATE HMC-2G" : 2,                    # MPC7E                      
        "MPC7-10G HMC-2G LQ" : 2,                   # MPC7E                     
        "MPC7-MRATE HMC-2G LQ" : 2,                 # MPC7E
        "MPC8EQ" : 4,                               # MPC8E
        "LC2103" : 3                                # summit
    }

    capacity = cases.get(fpc, "not a supported FPC/MPC type")
    return capacity

