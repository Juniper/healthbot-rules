# Synopsis        
All rules based on open-config under security topic.

# Description
This folder comprises of all the rules which monitors all the sensors related
to security topic under junos.

# Rules Index   

## Rule 1: check-veriexec-status.rule

**Synopsis**   
This rule detects the status of veriexec in the system and detects the anomalies
based on if veriexec is loaded and enforced.

IMPORTANT: If telemetry is being done in plain text, veriexec state will be visible
over the network and can be a security risk. Hence prefer the iagent rule below, unless
the telemetry channel is secured.

**Sensor type**          
open-config

**Input variables**   
_veriexec-state_: open-config path `/junos/security/veriexec-state`

**Threshold**   
It will check the veriexec status and will report the red alarm in case if
veriexec is not loaded, and yellow alarm in case if its loaded but not enforced.

**Platforms supported**    
MX series, PTX series, EX92XXX

**Junos release supported**    
19.1 Junos release onwards

**Suggested action**   
This rule will report if there is any anomalies related to veriexec.
It's recommended to have always veriexec enabled.

## Rule 2: check-veriexec-status-iagent.rule

**Synopsis**   
This rule detects the status of veriexec in the system and detects the anomalies
based on if veriexec is loaded and enforced.

**Sensor type**          
iAgent

**Dependent files**   
veriexec.yml

**Input variables**   
_veriexec-state_: iAgent sensor `sysctl security.mac.veriexec.state`

**Threshold**   
It will check the veriexec status and will report the red alarm in case if
veriexec is not loaded, and yellow alarm in case if its loaded but not enforced.

**Platforms supported**
All platforms

**Junos release supported**
All Junos releases

**Suggested action**   
This rule will report if there is any anomalies related to veriexec.
It's recommended to have always veriexec enabled.

