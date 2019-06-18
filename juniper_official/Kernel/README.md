# Synopsis
All rules under Kernel.ifstate topic.

# Description
This section comprises of all the rules which monitor the sensors related to Ifstate
(FIB metadata) in Junos.

# Rules Index

## Rule 1:  check-client-limit-reached.rule
**Synopsis**            
This rule checks if any application has opened more than the allowed number of Ifstate
based routing sockets.

**Sensor type**         
open-config

**Input variables**     
_client-limit-reached_ : open-config path /junos/kernel-ifstate/client-limit-reached

**Platforms supported**       
MX series, PTX series, EX92XXX

**Junos release supported**         
19.1 Junos release onwards

**Threshold**           
It checks if the count has incremented by at least one, in the last 10 mins

**Suggested action**    
Contact Juniper and provide below information.     
1) All log files in /var/log/, from both routing engines.      
2) Collect and share 'gcore' of the application reporting this error in logs.
   Search for "rts_ifstate_chk_multi_registration" in the /var/log/messages\* to
    to look for the application complaining.

## Rule 2:  check-too-many-dead-ifstates.rule
		
**Synopsis**            
This rule checks for the number of dead ifstates at any given time in the
system. It monitors the number of dead Ifstates and raises an alarm if there
are too many of these (> 50% of alive ifstates) detected for significant
duration of time (1 hour).

**Sensor type**         
open-config

**Dependent files**     
deadalive.yml, get-dead-alive-ratio.py
 
**Input variables**    
_alive-ifstates-cnt_ :openconfig path  `/junos/kernel-ifstate/alive-ifstates-cnt`     
_dead-ifstates-cnt_  :openconfig path  `/junos/kernel-ifstate/dead-ifstates-cnt`    

**Platforms supported**     
MX series, PTX series, EX92XXX

**Junos release supported**    
19.1 Junos release onwards

**Threshold**           
50 percent of alive ifstates

**Suggested action**    
Collect below information and contact Juniper:
1) Take a kernel live vmcore by issuing "sysctl kern.live_core_dump" and share vmcore generated in
   /var/crash
2) All log files in /var/log/, from both routing engines
3) Output of `ifsmon -p, ifsmon -c, ifsmon -Id, ifsmon -g`     

## Rule 3:  check-too-many-dead-ifstates-iagent.rule

**Synopsis**            
This rule checks for the number of dead ifstates at any given time in the
system. It monitors the number of dead Ifstates and raises an alarm if there
are too many of these (> 50% of alive ifstates) detected for significant
duration of time (1 hour).
Note: This is the iAgent version of Rule 2 above, for targets < 19.1 Junos
      release or for non MX/PTX/EX platforms.

**Sensor type**         
iAgent

**Dependent files**     
deadalive.yml, get-dead-alive-ratio.py
 
**Input variables**    
_dead-cnt_  : iAgent sensor `ifsmon -I`     
_live-cnt_  : iAgent sensor `ifsmon -I`    

**Platforms supported**     
All platforms

**Junos release supported**      
All Junos releases

**Threshold**           
50 percent of alive ifstates

**Suggested action**    
Collect below information and contact Juniper:
1) Take a kernel live vmcore by issuing "sysctl kern.live\_core\_dump" and share vmcore generated in
   /var/crash
2) All log files in /var/log/, from both routing engines
3) Output of below commands from shell, run as a root user:
   a> ifsmon -Id
   b> ifsmon -c
   c> ifsmon -p
   d> ifsmon -g

## Rule 4:  check-stuck-ifstate-clients.rule

**Synopsis**            
This rule checks if there are any stuck ifstate clients present in the system.
Though rare, but when any Ifstate client (application/FPC peer) gets stuck,
it can result in resource accumulation and eventually can lead to traffic loss.

**Sensor Type**         
open-config

**Dependent files**     
fetch_stuck_client.py, fetch_stuck_client.yml 

**Input variables**    
_stuck-clients_  : openconfig path `/junos/kernel-ifstate/stuck-clients-cnt` 

**Platforms supported**    
MX series, PTX series, EX92XXX

**Junos release supported**    
19.1 Junos release onwards

**Threshold**           
It checks if the count has incremented for stuck clients in the last one minute. 

**Suggested action**    
Check Following CLI for the further details on which client/peer is slow.
  \> show system alarms

Once a stuck Ifstate client is detected, it should ideally be restarted or
a GRES switchover (if configured) should be tried. It is recommended to
take these actions during a maintainence window.

Contact Juniper and provide below information.     
1) Any kernel live vmcore files in /var/crash/, on both routing engines.      
2) All log files in /var/log/, from both routing engines.      
3) If daemon is stuck, take gcore using `gcore -c <core_file_name> <pid>`         
4) Daemon log file located at /var/log/<daemon_name>       

## Rule 5:  check-stuck-ifstate-clients-iagent.rule

**Synopsis**            
This rule checks if there are any stuck ifstate clients present in the system.
Though rare, but when any Ifstate client (application/FPC peer) gets stuck,
it can result in resource accumulation and eventually can lead to traffic loss.

**Sensor Type**         
iAgent

**Dependent files**     
fetch_stuck_client.py, fetch_stuck_client.yml 

**Input variables**    
_stuck-client-info_ : iAgent sensor `show system alarms`

**Platforms supported**    
All platforms

**Junos release supported**    
All Junos releases

**Threshold**
This rule checks if "slow peers" alarm has been raised on the device or not.

**Suggested action**    
Check Following CLI for the further details on which client/peer is slow.
  \> show system alarms

Once a stuck Ifstate client is detected, it should ideally be restarted or
a GRES switchover (if configured) should be tried. It is recommended to
take these actions during a maintainence window.

Contact Juniper and provide below information.     
1) Any kernel live vmcore files in /var/crash/, on both routing engines.     
2) All log files in /var/log/, from both routing engines.     
3) Take gcore using `gcore -c <core_file_name> <pid>`     
4) Daemon log file located at /var/log/<daemon_name>    

## Rule 6:  check-delayed-unrefs-anomaly.rule

**Synopsis**            
This rule checks if there are any delayed unrefs and if they are greater than a
particular threshold. Transient spikes in delayed unref count is expected in
certain catastrophic or major events and is not a cause for worry. But, if this
situation persists for significant amount of time (say in minutes), then it can
result in traffic loss.

**Sensor Type**         
open-config

**Input variables**     
_delayed-unrefs-cnt_  : openconfig path `/junos/kernel-ifstate/delayed-unrefs-cnt`
_delayed-unrefs-max_  : openconfig path `/junos/kernel-ifstate/delayed-unrefs-max`

**Dependent files**     
delayed_unref.yml, delayed_unref.py

**Platforms supported**    
MX series, PTX series, EX92XXX

**Junos release supported**    
19.1 Junos release onwards

**Threshold**           
The threshold for this rule is detected via `sysctl net.rt_nh_max_delayed_unrefs`. 

**Suggested action**    
Contact Juniper and provide below information.    
1) Collect the live core by enabling sysctl `kern.live_core_dump=1`    
2) Kernel live vmcore files in /var/crash/, on both routing engines.    
2) All log files in /var/log/, from both routing engines.    
3) Output of `ifsmon -p, ifsmon -c, ifsmon -Id, ifsmon -kd, ifsmon -Pd`     
4) Collect marker debugs by enabling `sysctl -w net.ifs_marker_debug=1`    

## Rule 7:  check-delayed-unrefs-anomaly-iagent.rule

**Synopsis**            
This rule checks if there are any delayed unrefs and if they are greater than a
particular threshold. Transient spikes in delayed unref count is expected in
certain catastrophic or major events and is not a cause for worry. But, if this
situation persists for significant amount of time (say in minutes), then it can
result in traffic loss.

**Sensor Type**         
iAgent

**Dependent files**     
delayed_unref.yml, delayed_unref.py

**Input variables**     
_delayedcnt_    : iAgent sensor `ifsmon -I`    
_delayedmax_  : iAgent sensor `sysctl net.rt_nh_max_delayed_unrefs`

**Platforms supported**    
All platforms

**Junos release supported**    
All Junos releases

**Threshold**           
The threshold for this rule is detected via `sysctl net.rt_nh_max_delayed_unrefs`. 

**Suggested action**       
Contact Juniper and provide below information.           
1) Any kernel live vmcore files in /var/crash/, on both routing engines.           
2) All log files in /var/log/, from both routing engines.          
3) Output of `ifsmon -p, ifsmon -c, ifsmon -Id, ifsmon -kd, ifsmon -Pd`     
4) Collect marker debugs by enabling `sysctl -w net.ifs_marker_debug=1`     
5) Collect the live core by enabling sysctl `kern.live_core_dump=1`     

## Rule 8:  check-dead-ifstate-client.rule

**Synopsis**            
This rule checks if there are any dead ifstate clients not cleaned up in the
system for the last 20 minutes.

**Sensor Type**         
open-config

**Input variables**     
_dead-clients-cnt_  : openconfig path `/junos/kernel-ifstate/dead-clients-cnt`

**Platforms supported**    
MX series, PTX series, EX92XXX

**Junos release supported**    
19.1 Junos release onwards

**Threshold**           
It checks if all the samples collected every 1 minute are non-zero for contiguous
20 minutes.

**Suggested action**    
Contact Juniper and provide below information.       
1) Any kernel live vmcore files in /var/crash/, on both routing engines.    
2) All log files in /var/log/, from both routing engines.    
3) Check for any symptoms of ENOBUFS/Veto messages from kernel in /var/log/messages\*    

# Synopsis              
All rules under kernel.peer-infra topic. 

# Description           
This section comprises of all the rules which monitors all the parameters related
to peer-infra module in Junos Kernel. This module is responsible for replicating
FIB states to the line cards and also to process incoming IPCs from them.

#Rules Index

## Rule 1 - check-pfeman-conn-drops.rule
**Synopsis**            
This rule checks if there are any pfeman connection drops.

**Sensor type**         
open-config

**Input variables**     
_peer-pfeman-conn-drops_ : openconfig path `/junos/kernel/peer-infra/pfeman-conn-drops`

**Threshold**           
It checks if the count is incremented by atleast 5 in the last 5 minutes.

**Platforms supported**   
MX series, PTX series, EX92XXX

**Junos release supported**     
19.1 Junos release onwards

**Suggested action      
If there is an impact seen along with this (say, FPC restart or traffic loss),
then collect /var/log/\* and report to Juniper.

## Rule 2 - check-spurious-ppt-wkups.rule
**Synopsis**            
This rule checks for any spurious peer proxy threads (ppt) wakeups.
These spurious wakeups can result in performance issues, hence it is
important to detect any such issues.

**Sensor type**         
open-config

**Input variables**     
_spurious-ppt-wkups_  : open-config path `/junos/kernel/peer-infra/spurious-ppt-wkups`

**Threshold**           
This rule checks if the count is incremented for the last 't' mins and doesn't comapre this with any threshold.

**Platforms supported**
MX series, PTX series, EX92XXX

**Junos release supported**
19.1 Junos release onwards

**Suggested action**
If this reported consistently, it should be reported to Juniper along with
the /var/log/\* files.
# Synopsis
Rules under kernel.tcpip topic.

# Description
This section comprises of the rules that monitor health of TCP/IP stack in the Junos RE kernel. 

# Rules Index

## Rule 1: check-iri-conn-keepalive-dropped.rule
**Description**   
This rule detects any intra-chassis connection (part of Internal Routing
Instance) drops because of keep alive expiry.

**Sensor type**  
iAgent

**Dependent files**
tcpconn.yml, tcp_conn.py

**Input variables**
_keepalive_ : iAgent sensor 'sysctl net.inet.tcp.irs_kto'

**Threshold**  
The rule displays yellow color if any of the two contiguous samples 20 seconds
apart, report increase in counter that captures IRI connection drops.

**Platforms supported**
All Junos platforms

**Junos release supported**
19.1 Junos release onwards

**Suggested action**  
If there are repeated keepalive drops reported by this rule, search for
"Dropping socket connection due to keepalive timer expiration" in
/var/log/messages\* on the affected routing engine. Also, check if any
jlock hogs or TCP connection drop messages get reported in these log files
around the same time. Report to Juniper if this is happening consistently
or if there is a noticeable side effect seen (such as protocol flaps / traffic
loss) around the same time.
