# Healthbot BGP KPIs
#
 
Contains readily consumable healthbot playbooks and rules which are specific to BGP neighbor key performance indicators(KPIs).
BGP KPI rules collects the statistics from network devices then analyzes the data and act. BGP KPI playbook is set of rules,
each rule is defined with set of KPIs. Playbook contains bgp session state, neighbor flap detection, received routes with static
threshold, received routes wiht dynamic threshold rules. Rules are defined with default variable values which can be changed while
deploying playbook.


## Usage

Apply the playbook to device-group under playbooks section using healthbot GUI.
