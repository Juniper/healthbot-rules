# HealthBot Isis KPI rules and playbooks

## Isis playbooks
### Playbook name: isis-stats-playbook 
		> Description: "Playbook checks the ISIS adjacencies health and notify anomaly when statistics are unusual"
		> Synopsis: "ISIS adjacency key performance indicators"
		> Playbook file name: isis-statistics.playbook
		> Details:
		 Playbook contains multiple rules which checks the ISIS adjacency statistics
		 and notifies when anomalies are found.
		 1) Rule "check-isis-adjacencies" detects the ISIS adjacency session state
		    changes and notify anomalies when session state is down.
		 2) Rule "check-isis-statistics" detects the ISIS session statistics (lsp,
		    csnp, esh, iih, ish, psnp and unknown drops) and notify anomalies when
		    drop count exceeds threshold.
		 3) Rule "check-spf-isis-netconf" Check SPF run time and count  for ISIS and
		    notifies when anomalies are found.

## Isis rules

### Rule name: check-spf-isis-netconf 
		> Description: "Check SPF run time and count  for isis"
		> Synopsis: "SPF KPI"
		> Rule file name: check-spf-isis-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
### Rule name: check-isis-adjacencies 
		> Description: "Collects ISIS adjacency state periodically and notify anomaly when state is down"
		> Synopsis: "ISIS session state analyzer"
		> Rule file name: isis-adjacency.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:MX240, Junos:17.4R1
		> Supported product:MX, Platforms:MX480, Junos:17.4R1
		> Supported product:MX, Platforms:MX960, Junos:17.4R1
		> Supported product:MX, Platforms:MX2010, Junos:17.4R1
		> Supported product:MX, Platforms:MX2020, Junos:17.4R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.4R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.4R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.4R1



		> More details:
		 Detects ISIS adjacency state changes and notifies when anomalies are found.
		 Three input control detection
		
		   1) instance-name, is a regular expression that matches the routing
		      instance that you would like to monitor.  By default it's '.*', which
		      matches all routing instances. Use something like 'master|RI1' to match
		      only ISIS adjacencies belong to master and RI1 routing instances.
		   2) system-name, is a regular expression that matches the ISIS syste-id
		      that you would like to monitor.  By default it's '.*', ISIS which matches
		      all system ids. Use something like 'router1|router2' to match only
		      ISIS adjacencies contains system-id names router1 and router2.
		   3) interface-name, is a regular expression that matches the interfaces
		      that you would like to monitor.  By default it's '.*', which matches
		      all interfaces. Use something like 'ge.*' to match only ISIS
		      adjacencies contains gigabit ethernet interfaces.
### Rule name: check-isis-statistics 
		> Description: "Collects ISIS session statistics(lsp, csnp, esh, iih, ish, psnp and unknown drops) periodically and notify anomaly when breaches threshold"
		> Synopsis: "ISIS adjacency statistics analyzer"
		> Rule file name: isis-statistics.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:MX240, Junos:17.4R1
		> Supported product:MX, Platforms:MX480, Junos:17.4R1
		> Supported product:MX, Platforms:MX960, Junos:17.4R1
		> Supported product:MX, Platforms:MX2010, Junos:17.4R1
		> Supported product:MX, Platforms:MX2020, Junos:17.4R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.4R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.4R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.4R1



		> More details:
		 Detects ISIS packet drops and notifies when anomalies are found.
		 Two input control detection
		
		   1) drops-threshold, is the threshold that causes the rule to report an
		      anomaly. By default it's 1. This rule will set a dashboard color to
		      red when packet drop count is greater than 'drops-threshold' for 3
		      minutes period, otherwise color is set to green.
		   2) interface-name, is a regular expression that matches the interfaces
		      that you would like to monitor.  By default it's '.*', which matches
		      all interfaces. Use something like 'ge.*' to match only ISIS
		      adjacencies contains gigabit ethernet interfaces.
