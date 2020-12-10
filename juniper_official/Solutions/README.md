# Healthbot solutions to network problems

 
Contains readily consumable healthbot solutions playbooks and rules. Solution rules collect the statistics from network devices, then analyze the data and act.
Solutions playbooks are a set of rules, where each rule is defined with a set of KPIs. 

Solution Playbooks contains root cause analysis of OSPF and its subsystems problems, MPLS blackhole detection, microbursts detection, l3 VPN view and BGP IPv4 & IPv6 route hijacks detection.
Rules are defined with default variable values, which can be changed while deploying the playbook.


## Usage

Apply the device specific playbooks to device-group under the playbooks section using healthbot GUI.
Apply the network specific playbooks to network-group under the playbooks section using healthbot GUI.

