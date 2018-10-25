# Healthbot System KPIs
#
 
Contains readily consumable healthbot playbooks and rules which are specific to system key performance indicators(KPIs).
System KPI rules collects the statistics from network devices then analyzes the data and act. System KPI playbook is set of
rules, each rule is defined with set of KPIs. Playbook contains routing engine cpu, routing engine memory, junos processes
cpu, memory leak detection and system storage rules. Rules are defined with default variable values which can be changed
while deploying playbook.


## Usage

Apply the playbook to device-group under playbooks section using healthbot GUI.
