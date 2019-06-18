# Synopsis
Rules under routing-options.nsr topic.

# Description
All rules that are related to nonstop-routing Junos feature.

# Rules Index

## Rule 1: check-jsr-kkcm-conn.rule
**Description**
Report KKCM connection issues, if nonstop-routing feature is configured. 

**Sensor type**
iAgent

**Dependent files**
jsr_kkcm.yml, jsr_kkcm.py

**Input variables**
_jsr   : iAgent sensor 'sysctl net.jsr.enable'
_kkcm_ : iAgent sensor 'netstat -na | grep 15001 | grep -c ESTABLISHED'

**Threshold**
The rule displays red color if number of KKCM (Kernel to Kernel Connection
Manager) connections are less than 2, when nonstop-routing (NSR) is configured.
If NSR is not configured or if the number of connections between the two
routing engines are as expected, it displays green color.

**Platforms supported**
All dual RE Junos platforms supporting nonstop-routing

**Junos release supported**
All Junos releases supporting nonstop-routing

**Suggested action**
If this rule reports an issue, make sure that nonstop-routing is indeed
configured. Try removing this configuration and then reconfiguring the same.
If the problem still persists, nonstop-routing is compromised and issue should
be reported to Juniper.
