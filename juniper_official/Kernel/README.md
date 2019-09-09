# Synopsis
All rules under kernel.rtsock topic.

# Description
This section comprises of all the rules which monitor the sensors related to rtsock in Junos.

# Rules Index

## Rule 1: detect-routing-socket-errors.rule
**Synopsis**            
This rule checks for the total number of routing socket errors at any given time in the system. It monitors the total number of errors and raises an alarm if there are too many of these detected for significant duration of time. routing socket errors includes errors returned from veto, mproc and rtsock layers.

**Sensor type**           
open-config

**Input variables**           
rtsock-error-count-threshold : theshold value.          
rtsock-total-error-count: open-config path /junos/kernel/rtsock/total-error-cnt          
rtsock-total-veto-count: open-config path /junos/kernel/rtsock/total-veto-cnt         

**Platforms supported**                    
MX series, PTX series, EX series

**Junos release supported**              
19.3R1 Junos release onwards

**Threshold**                 
Check if routing socket errors has been increased by 100 from its previous value in ALL the samples for the last 70 or 130 seconds. 

**Suggested action**          
Collect below information and contact Juniper:       
1)Take a kernel live vmcore by issuing "sysctl kern.live_core_dump" and share vmcore generated in /var/crash          
2)All log files in /var/log/, from both routing engines          
3)Output of ifsmon -p, ifsmon -c, ifsmon -Id, ifsmon -g               

## Rule 2: detect-routing-socket-errors-iagent.rule

**Synopsis**                   
This rule checks for the total number of routing socket errors at any given time in the system. It monitors the total number of errors and raises an alarm if there are too many of these detected for significant duration of time. routing socket errors includes errors returned from veto, mproc and rtsock layers.

**Sensor type**           
iAgent

**Input variables**             
rtsock-error-count-threshold : theshold value.          
rtsock-total-error-count: sysctl net.rtsock_total_error_count         
rtsock-total-veto-count: sysctl net.rtsock_total_veto_count               

**Platforms supported**               
MX series, PTX series, EX series

**Junos release supported**             
18.3R3 Junos release onwards

**Threshold**                 
Check if routing socket errors has been increased by 100 from its previous value in ALL the samples for the last 70 or 130 seconds.

**Suggested action**                  
Collect below information and contact Juniper:              
1)Take a kernel live vmcore by issuing "sysctl kern.live_core_dump" and share vmcore generated in /var/crash        
2)All log files in /var/log/, from both routing engines        
3)Output of ifsmon -p, ifsmon -c, ifsmon -Id, ifsmon -g          
