# HealthBot Linecard KPI rules and playbooks

## Linecard playbooks
### Playbook name: netconf-fpc-playbook 


		> Playbook file name: netconf-fpc.playbook
		> Detals:

## Linecard rules

### Rule name: check-netconf-fpc-cpu-memory-stats 
		> Description: "Collects CPU, Memory Heap& Buffer Utilization details from FPC slot and notify anomalies based on threshold values "

		> Rule file name: netconf-fpc-cpu-stats.rule

		> Supported products: MX 

			> Supported platforms: ALL;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects FPC CPU and memory utilization and notifies when anomalies are found.
		 One input control detection
		
		   1) "threshold" is the threshold that causes the rule to report
		      an anomaly.  By default it's 80. This rule will set a dashboard
		      color to red when *all* the CPU/Buffer memory/ Heap memory utilization greater than
		      'threshold'.
		   2) slot-name,  is a regular expression that matches the
		      FPC slot number that you would like to monitor.  By default it's
		      all slots [0-9]*.
