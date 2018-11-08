# Healthbot LLDP KPIs
#
 
Contains readily consumable healthbot playbooks and rules which are specific to LLDP neighbor key performance indicators(KPIs).
LLDP KPI rules collects the statistics from network devices then analyzes the data and act. LLDP KPI playbook is set of rules,
each rule is defined with set of KPIs. Playbook contains lldp session state, lldp statistics i.e. frame discards, frame in errors,
frame out erros, tlv discards and unknown tlv rules. Rules are defined with default variable values which can be changed while
deploying playbook.


## Usage

Apply the playbook to device-group under playbooks section using healthbot GUI.
