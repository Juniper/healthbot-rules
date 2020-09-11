# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN playbooks
### Playbook name: netconf-chassis-playbook 


		> Playbook file name: netconf-chassis.playbook
		> Detals:

## EVPN VXLAN rules

### Rule name: check-netconf-chassis-component-temperature 
		> Description: "Collects temperature details from chassis components and notify anomalies based on threshold values "

		> Rule file name: netconf-system-cpu-temperatures.rule

		> Supported products: MX 

			> Supported platforms: ALL;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects Chassis components temperatures and notifies when anomalies are found.
		 One input control detection
		
		   1) "threshold" is the threshold that causes the rule to report
		      an anomaly.  By default it's 80. This rule will set a dashboard
		      color to red when *all* the CPU/Buffer memory/ Heap memory utilization greater than
		      'threshold'.
