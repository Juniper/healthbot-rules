# HealthBot Bgp KPI rules and playbooks

## Bgp playbooks
### Playbook name: bgp-session-stats-playbook 
		> Description: "Playbook checks the BGP neighbor sessions health and notify anomaly when statistics are unusual"
		> Synopsis: "BGP neighbor sessions key performance indicators"
		> Playbook file name: bgp-neighbor-stats-kpi.playbook
		> Details:
		 Playbook contains multiple rules which checks the statistics of BGP neighbor
		 sessions and notifies when anomalies are found.
		 1) Rule "check-bgp-session-state" detects the BGP neighbor session state
		    changes and notify anomalies when session state is down.
		 2) Rule "check-bgp-neighbor-flaps" detects the BGP neighbor session flaps
		    and notify anomalies when session state is down.
		 3) Rule "check-bgp-received-routes" detects the received route count
		    threshold breaches and notify anomalies.
		 4) Rule "check-bgp-advertised-routes" detects the advertised route count
		    threshold breaches and notify anomalies.

## Bgp rules

### Rule name: check-bgp-advertised-routes 
		> Description: "Collects BGP session advertised routes count periodically and notifies anomaly when advertised route count exceed threshold"
		> Synopsis: "BGP advertised routes analyzer"
		> Rule file name: bgp-advertised-routes-kpi.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:MX240, Junos:17.2R1
		> Supported product:MX, Platforms:MX480, Junos:17.2R1
		> Supported product:MX, Platforms:MX960, Junos:17.2R1
		> Supported product:MX, Platforms:MX2010, Junos:17.2R1
		> Supported product:MX, Platforms:MX2020, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5110, Junos:17.3R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Detects BGP neighbor advertised route count threshold breaches and notifies
		 when anomalies are found.
		 Four inputs control detection
		
		   1) "neighbors" is a regular expression that matches the BGP neighbors
		      that you would like to monitor.  By default it's '.*', which matches
		      all BGP neighbors. Use something like '172.16.*' to match all neighbor
		      addresses which are in 172.16.0.0/16 network range.
		   2) "routing-instance" is the variable that filters the routing instances.
		      By default it's ".*", which matches neighbors in all routing instances.
		      Use something like "master" to match neighbors belongs to only master
		      routing instance.
		   3) "addr-table" is the variable that filters the routing address table.
		      By default it's ".+", which matches all address tables. Use something
		      like "IPV4_UNICAST" to match only advertised routes belongs to IPV4
		      unicast address table.
		   4) "max-advertised-route-count-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 10000. This rule will set
		      a dashboard color to red when advertised route count exceed threshold
		      (max-advertised-route-count-threshold), otherwise color is set to green.
### Rule name: check-bgp-neighbor-flaps 
		> Description: "Collects BGP session carrier-transitions count periodically and notify anomalies when flap count increases"
		> Synopsis: "BGP neighbor flaps detector"
		> Rule file name: bgp-neighbor-flap-detection.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:MX240, Junos:17.2R1
		> Supported product:MX, Platforms:MX480, Junos:17.2R1
		> Supported product:MX, Platforms:MX960, Junos:17.2R1
		> Supported product:MX, Platforms:MX2010, Junos:17.2R1
		> Supported product:MX, Platforms:MX2020, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5110, Junos:17.3R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Detects BGP neighbor flaps and notifies when anomalies are found.
		 Two inputs control detection
		
		   1) "neighbors" is a regular expression that matches the BGP neighbors
		      that you would like to monitor.  By default it's '.*', which matches
		      all BGP neighbors. Use something like '172.16.*' to match all neighbor
		      addresses which are in 172.16.0.0/16 network range.
		   2) "flaps-threshold" is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when any of the BGP neighbor session flap-increases
		      are greater than 'flaps-threshold' for 60s. If it sees any flaps
		      increase for a period of less than 60s, it'll turn the color to
		      yellow, otherwise color is set to green.
### Rule name: check-bgp-neighbor-flap-iagent 
		> Description: "Collects BGP neighbor flap count periodically and notifies anomaly"
		> Synopsis: "BGP neighbor flap count analyzer"
		> Rule file name: bgp-neighbor-flap-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:A, Junos:15.1R1
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects BGP neighbor flaps and notifies when anomalies are found
		 Two inputs control detection
		   1) "neighbors" is a regular expression that matches the BGP neighbors
		      that you would like to monitor.  By default it's '.*', which matches
		      all BGP neighbors. Use something like '172.16.*' to match all neighbor
		      addresses which are in 172.16.0.0/16 network range.
		   2) "flaps-threshold" is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when any of the BGP neighbor session flap-increases
		      are greater than 'flaps-threshold' for 60s. If it sees any flaps
		      increase for a period of less than 60s, it'll turn the color to
		      yellow, otherwise color is set to green.
### Rule name: check-bgp-neighbor-state-iagent 
		> Description: "Collects BGP neighbor state periodically and notifies anomaly"
		> Synopsis: "BGP neighbor state analyzer"
		> Rule file name: bgp-neighbor-state-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1
		> Supported product:EX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects BGP neighbor state and notifies when anomalies are found
		 Inputs control detection
		   1) "neighbors" is a regular expression that matches the BGP neighbors
		      that you would like to monitor.  By default it's '.*', which matches
		      all BGP neighbors. Use something like '172.16.*' to match all neighbor
		      addresses which are in 172.16.0.0/16 network range.
### Rule name: check-bgp-session-state 
		> Description: "Collects BGP session state periodically and notify anomalies when neighbor session down"
		> Synopsis: "BGP session state analyzer"
		> Rule file name: bgp-neighbor-state.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:MX240, Junos:17.2R1
		> Supported product:MX, Platforms:MX480, Junos:17.2R1
		> Supported product:MX, Platforms:MX960, Junos:17.2R1
		> Supported product:MX, Platforms:MX2010, Junos:17.2R1
		> Supported product:MX, Platforms:MX2020, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5110, Junos:17.3R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Detects BGP neighbor state changes and notifies when anomalies are found.
		 One input control detection
		
		   1) "neighbors" is a regular expression that matches the BGP neighbors
		      that you would like to monitor.  By default it's '.*', which matches
		      all bap neighbors. Use something like '172.16.*' to match all neighbor
		      addresses which are in 172.16.0.0/16 network range.
### Rule name: check-bgp-received-routes 
		> Description: "Collects BGP session received routes count periodically and notifies anomaly when received route count exceed threshold"
		> Synopsis: "BGP received routes analyzer"
		> Rule file name: bgp-received-routes-kpi.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:MX240, Junos:17.2R1
		> Supported product:MX, Platforms:MX480, Junos:17.2R1
		> Supported product:MX, Platforms:MX960, Junos:17.2R1
		> Supported product:MX, Platforms:MX2010, Junos:17.2R1
		> Supported product:MX, Platforms:MX2020, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5110, Junos:17.3R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Detects BGP neighbor received route count threshold breaches and notifies
		 when anomalies are found.
		 Four inputs control detection
		
		   1) "neighbors" is a regular expression that matches the BGP neighbors
		      that you would like to monitor.  By default it's '.*', which matches
		      all BGP neighbors. Use something like '172.16.*' to match all neighbor
		      addresses which are in 172.16.0.0/16 network range.
		   2) "routing-instance" is the variable that filters the routing instances.
		      By default it's ".*", which matches neighbors in all routing instances.
		      Use something like "master" to match neighbors belongs to only master
		      routing instance.
		   3) "addr-table" is the variable that filters the routing address table.
		      By default it's ".+", which matches all address tables. Use something
		      like "IPV4_UNICAST" to match only received routes belongs to IPV4
		      unicast address table.
		   4) "max-received-route-count-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 10000. This rule will set
		      a dashboard color to red when received route count exceed threshold
		      (max-received-route-count-threshold), otherwise color is set to green.
