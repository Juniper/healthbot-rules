# Chassis management healthbot key performance indicators
# 
** Synopsis **

This folder contains healthbot rules and playbooks to check the chassis health and notify when anomaly

** Rule Index **

Rule1 – chassis-fan-health.rule – This rule checks health of fan and notify in case any of the health monitored fields crosses threshold   
Sensor type : iAgent    
Input variables : N/A    
Dependency file(s) : chassis-fan.yml    

Rule2 – chassis-temperature.rule – This rule checks health of whole chassis temperature and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : chassis-temperature-high-threshold(default value 55), chassis-temperature-low-threshold(default value 45)   
Dependency file(s): No   

Rule3 – fpc-temperature.rule – This rule checks health of FPC temperature and notify in case any of the health monitored fields crosses threshold    
sensor type: open-config   
Input variables : FPC-Slot-No(default value 0-9), FPC-Temperature-Higher-Threshold(default value 55), FPC-Temperature-Lower-Threshold(default value 45)   
Dependency file(s) : No   

Rule4 – pem-power-usage.rule –  This rule checks pem status and power usage and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : pem-power-usage-threshold(default value 888888880)   
Dependency file(s) : used-percentage.py   

Rule5 – re-cpu-temperature.rule – This rule checks health of RE CPU temperature and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : RE-CPU-Temperature-Higher-Threshold(default value 55), RE-CPU-Temperature-Lower-Threshold(default value 45), RE-Slot-No(default value 0-1)   
Dependency file(s) : No   

Rule6 – system-power-usage.rule – This rule checks system power usage and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : system-power-usage-threshold(default value 20)   
Dependency file(s) : used-percentage.py   

Rule7 – zone-power-usage.rule – This rule checks health of pem power zones usage and notify in case any of the health monitored fields crosses threshold   
sensor type: iAgent   
Input variables : zone-power-usage-threshold(default value 80)   
Dependency file(s) : used-percentage.py   


Playbook – chassis-kpis.playbook – This playbook checks health of chassis and notify in case any of the health monitored fields crosses threshold   
This playbook contains following rules:-   
chassis.fan/check-fan-health    
chassis.temperatures/check-fpc-temperature    
chassis.power/check-pem-power-usage    
chassis.power/check-system-power-usage    
chassis.power/check-zone-power-usage    
chassis.temperatures/check-chassis-temperature    
chassis.temperatures/check-re-cpu-temperature    
chassis.temperatures/check-re-temperature   


# Synopsis
Rules under chassis.gres topic.

# Description
This section comprises of the rules that monitor health of Graceful Routing Engine Switchover (GRES) Junos high-availability/failover feature. 

# Rules Index

## Rule 1: check-failover-configured.rule
**Description**  
This rule checks if graceful-switchover is configured or not, on a dual Routing Engine chassis.

**Sensor type**  
iAgent

**Dependent files**  
failover-info.yml, get_failover_info.py

**Input variables**  
_gres-state_ : iAgent sensor 'sysctl hw.re.failover'
_ore-present_ : iAgent sensor 'sysctl hw.ore.present'

**Platforms supported**  
All platforms

**Junos release supported**  
All Junos releases

**Threshold**  
The rule checks whether graceful-switchover is configured on dual RE chassis or not.

**Suggested action**  
If the chassis has dual RE and "chassis redundancy graceful-switchover" is not configured, this rule will report yellow color. For high availability, it is recommended to configure GRES on dual RE chassis.

**References**  
[Understanding Graceful Routing Engine Switchover](https://www.juniper.net/documentation/en_US/junos/topics/concept/gres-overview.html)

## Rule 2: check-failover-init-error.rule
**Description**  
This rule checks if Ksyncd (Junos Kernel State Synchronization daemon) has reported an initialization error or not.

**Sensor type**  
open-config

**Dependent files**  
N/A

**Input variables**  
_gres-error-state_ : open-config sensor '/junos/chassis/gres/error-state'

**Platforms supported**  
MX series, PTX series, EX92XXX

**Junos release supported**  
19.1 Junos release onwards

**Threshold**  
The rule checks for Ksyncd initialization error every 15 minutes and displays red color if contiguous 2 samples report the error.

**Suggested action**  
If this rule detects a continuous Ksyncd initialization error, it is recommended to reboot Slave Routing Engine to recover from the situation.

**References**  
[Understanding Graceful Routing Engine Switchover](https://www.juniper.net/documentation/en_US/junos/topics/concept/gres-overview.html)

## Rule 3: check-ksyncd-core.rule
**Description**  
This rule checks if Ksyncd (Junos Kernel State Synchronization daemon) core file is present in /var/tmp or not.

**Sensor type**  
iAgent

**Dependent files**  
find_ksyncd_cores.yml, find_ksyncd_cores.py

**Input variables**  
_ksyncd-cores_ : iAgent sensor 'cli show system core-dumps routing-engine other | grep -c ksyncd'

**Platforms supported**  
All dual RE platforms

**Junos release supported**  
All Junos releases

**Threshold**  
The rule checks for presence of Ksyncd core files every 15 minutes.

**Suggested action**  
Contact Juniper and provide below information.
1) Ksyncd core file(s) located in /var/tmp/ on the device. Check both routing engines.
2) Any kernel live vmcore files in /var/crash/, on both routing engines.
3) Crashinfo file located in /var/tmp/, if available.
4) All log files in /var/log/, from both routing engines.

**References**  
[Understanding Graceful Routing Engine Switchover](https://www.juniper.net/documentation/en_US/junos/topics/concept/gres-overview.html)

## Rule 4: report-gres-readiness.rule
**Description**  
This rule checks if system is ready for graceful-switchover or not.
Needs check-failover-configured.rule delpoyed too.

**Sensor type**  
open-config, also refers to one iAgent field in "check-failover-configured" rule.

**Dependent rules**  
check-failover-configured.rule

**Dependent files**  
N/A

**Input variables**  
_configured-state_ : open-config sensor '/junos/chassis/gres/configured-state'
_slave-connect-time_ : open-config sensor '/junos/chassis/gres/slave-connect-time'
_slave-kernel-ready_ : open-config sensor '/junos/chassis/gres/slave-kernel-ready'
_ore-present_ : Reference to iAgent field in rule "check-failover-configured.rule"

**Platforms supported**  
MX series, PTX series, EX92XXX

**Junos release supported**  
19.1 Junos release onwards

**Threshold**  
The rule checks if the system is not ready for GRES switchover for more than 1 hour, in which case it displays red color. It first checks if the chassis is dual RE or not and whether GRES is configured. Then it checks if Slave has been connected to Master RE for at least 60 minutes and if still system is not ready for failover, this rule complains.

**Suggested action**  
This rule displays red color if system is not ready for GRES switchover. When this occurs, try restaring kernel-replication daemon on Slave RE by issuing "restart kernel-replication" command on CLI. If again the rule displays a problem, try rebooting Slave RE.

**References**  
[Understanding Graceful Routing Engine Switchover](https://www.juniper.net/documentation/en_US/junos/topics/concept/gres-overview.html)

# Synopsis
Rules under chassis.issu topic.

# Description
This section comprises of all the rules that monitor health of In Service Software Upgrade (ISSU) Junos feature. 

# Rules Index

## Rule 1: check-issu-failure.rule
**Description**  
This rule detects ISSU failure and displays the ISSU stage when the failure occurred.

**Sensor type**  
open-config

**Dependent files**
N/A

**Input variables**
_failure-stage_ : open-config sensor '/junos/chassis/issu/failure-stage'
_current-issu-stage_ : open-config sensor '/junos/chassis/issu/current-issu-stage'

**Platforms supported**
All MX series, PTX series & EX92XXX that support ISSU

**Junos release supported**
19.1 Junos release onwards

**Threshold**  
The rule displays red color and the ISSU failure state, when it detects a non-zero ISSU failure stage sensor.

**Suggested action**  
If an ISSU failure is detected, this rule will display the ISSU state when the failure occured, as part of the message. If a failure is reported, please collect below information from the device:
1) All log files under /var/log, from both routing engines
2) From and To Junos releases
3) Output of "show chassis hardware"
4) Output of "request system software validate in-service-upgrade <new Junos s/w image>"

*Note*: The ISSU failure count will be reset when next ISSU is performed. If you manually want to reset it, issue "sysctl hw.re.issu_failure_stage=0" command on the routing engine at the shell prompt.

**References**  
[ISSU overview](https://www.juniper.net/documentation/en_US/junos/topics/concept/issu-oveview.html)
