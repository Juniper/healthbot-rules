# HealthBot Isis KPI rules and playbooks

## Isis playbooks
### Playbook name: isis-stats-playbook 
		> Description: "Playbook checks the ISIS adjacencies health and notify anomaly when statistics are unusual"
		> Synopsis: "ISIS adjacency key performance indicators"
		> Playbook file name: isis-statistics.playbook
		> Detals:
		 Playbook contains multiple rules which checks the ISIS adjacency statistics
		 and notifies when anomalies are found.
		 1) Rule "check-isis-adjacencies" detects the ISIS adjacency session state
		    changes and notify anomalies when session state is down.
		 2) Rule "check-isis-statistics" detects the ISIS session statistics (lsp,
		    csnp, esh, iih, ish, psnp and unknown drops) and notify anomalies when
		    drop count exceeds threshold.

## Isis rules

### Rule name: check-isis-adjacencies 
		> Description: "Collects ISIS adjacency state periodically and notify anomaly when state is down"
		> Synopsis: "ISIS session state analyzer"
		> Rule file name: isis-adjacency.rule

		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];

		> Supported healthbot version: 1.0.1
		> Detals:
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

		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];

		> Supported healthbot version: 1.0.1
		> Detals:
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
