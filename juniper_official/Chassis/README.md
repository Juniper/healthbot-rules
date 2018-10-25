# Chassis Management Healthbot KPIs
#
 
Contains readly consumable healthbot playbooks and rules which are specific to chassis key performance indicators(KPIs).
Chassis KPI rules collects the statistics from network devices then analyzes the data and act. Chassis KPI playbook is set of
rules, each rule is defined with set of KPIs. Playbook contains chassis temperature, routing engine temperature, routing engine
CPU temperature, FPC temperature, FAN health, PEM power usage, Zone power usage and overall system power usage rules. Rules are
defined with default variable values which can be changed while deploying playbook.


## Usage

Apply the playbook to device-group under playbooks section using healthbot GUI.
