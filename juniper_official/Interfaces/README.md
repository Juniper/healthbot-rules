# HealthBot Interfaces KPI rules and playbooks

## Interfaces playbooks
### Playbook name: interface-kpis-playbook 
		> Description: "Playbook to check interface health w.r.t. links, flaps, neighbor state, input & output traffic, errors and queue depth"
		> Synopsis: "Interface key performance indicators"
		> Playbook file name: interface-kpis.playbook
		> Details:
		 Playbook contains multiple rules which monitor interfaces and notifies when
		 anomalies are found.
		
		 1) Rule check-in-errors, detects the interface in errors and notifies
		 2) Rule check-out-errors, detects the interface out errors and notifies
		 3) Rule check-interface-flaps, detects interface flaps and notifies
		 4) Rule check-in-traffic, monitors the interface in traffic and notifies
		 5) Rule check-out-traffic, monitors the interface out traffic and notifies
		 6) Rule check-interface-status, monitors the interface status and notifies
		 7) Rule check-neighbor-state, monitors the interface in errors and notifies
		 8) Rule check-ifl-in-traffic, monitors the logical interfaces in traffic and
		 9) Rule check-ifl-out-traffic, monitors the logical interface out traffic
		 10) Rule check-queue-depth-netconf, monitors the interface queue depth
### Playbook name: interface-throughput-kpi 
		> Description: "Playbook to check interface bandwidth utilization"
		> Synopsis: "Interface bandwidth key performance indicators"
		> Playbook file name: interface-throughput.playbook
		> Details:
		 Playbook contains a rule which monitor interfaces bandwidth
		 utilization and notifies anomalies when exceeds threshold.
		
		 1) Rule check-interface-bandwidth-netconf, Notifies anomalies when interface
		    throughput exceeds threshold.
### Playbook name: lacp-kpis-playbook 
		> Description: "checks links are sending/receiving lacp packets "
		> Synopsis: "lacp key performance indicators"
		> Playbook file name: lacp-kpis-playbook.playbook
		> Details:
		 Playbook contains multiple rules which checks lacp packets
		 and notifies when anomalies are found.
		 1) Rule "check-lacp-statistics-openconfig" checks Checks if LACP Tx and Rx packets are
		     being sent and received on lacp enabled interfaces and notifies anomalies.
		 2) Rule "check-lacp-state-netconf" checks statistics on lacp enabled interfaces
		    and notifies anomalies.

## Interfaces rules

### Rule name: check-ifl-status 
		> Description: "Collects ifl stats and notifies in case status is down"
		> Synopsis: "Sub-interface status check"
		> Rule file name: check-ifl-status.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
### Rule name: check-interface-bandwidth-netconf 
		> Description: "Monitors the interface input and output bandwidth utilization"
		> Synopsis: "Interface bandwidth utilization analyzer"
		> Rule file name: check-interface-bandwidth-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
### Rule name: check-lacp-state-netconf 
		> Description: "Collects LACP interfaces status  periodically and notifies when distribution status is false"
		> Synopsis: "Lacp state analyzer"
		> Rule file name: check-lacp-state-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.0
		> Supported product:QFX, Platforms:A, Junos:18.1R1


		> Helper files: lacp-statistcs.yml;
		> More details:
		 Collects lacp statistics periodically and notifies anomalies when the lacp
		 distribution status is false.
		 One input controls detection
		
		  1) ae-name variable, is the interface name to monitor. By default monitors all lacp
		     interfaces. For specific interfaces to monitor, use regular expression
		     for e.g. ae1 or ae1|ae1.
### Rule name: check-lacp-statistics-openconfig 
		> Description: "Checks if LACP Tx and Rx packets are being sent"
		> Synopsis: "LACP statistics analyzer"
		> Rule file name: check-lacp-statistics-openconfig.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
### Rule name: check-queue-depth-netconf 
		> Description: "To moitor the interface queue depth"
		> Synopsis: "Queue Depth KPI"
		> Rule file name: check-queue-depth-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
### Rule name: check-queue-red-drop-netconf 
		> Description: "To monitor the interface queue RED dropped packets"
		> Synopsis: "Queue  RED Drop KPI"
		> Rule file name: check-queue-red-drop-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
### Rule name: check-queue-red-drop-oc 
		> Description: "To monitor the interface queue RED dropped packets"
		> Synopsis: "Queue  RED Drop KPI"
		> Rule file name: check-queue-red-drop-oc.rule
		> Sensor type: open-config 
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
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
### Rule name: check-queue-red-drop-total-netconf 
		> Description: "To monitor the interface queue RED dropped packets"
		> Synopsis: "Queue  RED Drop KPI"
		> Rule file name: check-queue-red-drop-total-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
### Rule name: check-interface-health 
		> Description: "Using this rule any one of the interface statistics counter (in and out errors, packets, octets, flaps) will be monitored"
		> Synopsis: "Interface KPI monitor based on description"
		> Rule file name: health-monitor-based-on-interface-description.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Filters interfaces based on keyword of an interface description. Monitors
		 only filtered interfaces based on selective KPI.
		 Using this playbook any one of the interface KPI (in-octets, out-octets,
		 in-pkts, out-pkts, in-unicast-pkts, out-unicast-pkts, in-errors, out-errors,
		 carrier-transitions) will be monitored.
		 ****Separate playbook instances to be created for each interface kpi
		 By default it monitors input traffic and notifies when utilization is above
		 threshold
		 Four inputs control detection
		   1) interface-description, is a regular expression that matches the keyword
		      in interface description and filters interfaces that you would like to
		      monitor. By default it's '.+', which matches all interfaces contains
		      description. Use something like 'core' to match only interfaces which
		      contains keyword 'core' in interface description.
		   2) stats-name-variable, is a regular expression that matches the interface KPI
		      statistics counter name that you would like to monitor. By default it's
		      in-octets, Use proper counter name something like 'out-octets' or
		      "in-errors" or "out-errors" etc.
		   3) high-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 800000000 octets . This rule will set a
		      dashboard color to red when *filtered interfaces* the input traffic
		      is above threshold for 60s. Use 8000000000 octets for 10G & 80000000000
		      for 100G interface.
		   4) medium-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 500000000 octets . This rule will set a
		      dashboard color to yellow when *filtered interfaces* the input traffic
		      is above threshold for 60s, otherwise color is set to green. Use
		      5000000000 octets for 10G & 50000000000 for 100G interface.
### Rule name: check-interface-flaps-iagent 
		> Description: "Collects link flap count periodically and notifies when flap count increases"
		> Synopsis: "Link flaps detector"
		> Rule file name: interface-flaps-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:A, Junos:15.1R1
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects interface flaps and notifies when anomalies are found.
### Rule name: check-interface-flaps 
		> Description: "Collects link flap count periodically and notifies when flap count increases"
		> Synopsis: "Link flaps detector"
		> Rule file name: interface-flaps.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Detects interface flaps and notifies when anomalies are found.
		 Two inputs control detection
		
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		
		   2) flaps-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the flap-increases are greater than
		      'flaps-threshold-variable' for 180s. If it sees any flaps increase for a
		      period of less than 180s, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: check-in-errors-iagent 
		> Description: "Collects the interface input error (errors (all), drops,discards, timeouts and runts) periodically and notifies in case of anomalies"
		> Synopsis: "Interface in-error analyzer"
		> Rule file name: interface-in-errors-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:A, Junos:15.1R1
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects interface in errors and notifies when anomalies are found.
### Rule name: check-in-errors 
		> Description: "Collects the interface input error (errors (all), drops,discards, timeouts and runts) periodically and notifies in case of anomalies"
		> Synopsis: "Interface in-error analyzer"
		> Rule file name: interface-in-errors.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Detects interface in errors and notifies when anomalies are found.
		 Two inputs control detection
		
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		
		   2) in-errors-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the error increases are greater than
		      'in-errors-threshold-variable' for 180s. If it sees any errors increase for a
		      period of less than 180s, it'll turn the color to yellow,
		      otherwise color is set to green.
		   3) in-errors-stats-name, is the error stats counter name in-error which is
		      cumaulative of in-fram-errors, in-resource-errors, in-giants, in-drops,
		      in-discards and mtu-errors. Default value is in-errors.
### Rule name: check-in-traffic-iagent 
		> Description: "Collects the interface input traffic."
		> Synopsis: "Interface input traffic analyzer"
		> Rule file name: interface-in-traffic-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:A, Junos:15.1R1
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects interface input traffic and notifies when anomalies are found.
### Rule name: check-in-traffic 
		> Description: "Collects input traffic (in-octets) periodically and notifies in case of traffic is above threshold"
		> Synopsis: "Interface input traffic analyzer"
		> Rule file name: interface-in-traffic.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Monitors interface input traffic and notifies when anomalies are found.
		 Four inputs control detection
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) stats-name, is a regular expression that matches the interface KPI
		      statistics counter name that you would like to monitor. By default it's
		      in-octets, Use proper counter name something like 'in-pkts' or
		      "in-unicast-pkts" or "in-multicast-pkts" etc.
		   3) in-octets-high-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 800000000 octets. This rule will
		      set a dashboard color to red when *all* the input traffic is above
		      threshold for 180 seconds period. Use 8000000000 octets for 10G &
		      80000000000 for 100G interface.
		   4) in-octets-low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 500000000 octets . This rule will
		      set a dashboard color to yellow when *all* the input traffic is above
		      threshold for 180 seconds period, otherwise color is set to green.
		      Use 5000000000 octets for 10G & 50000000000 for 100G interface.
### Rule name: check-interface-in-out-traffic-snmp 
		> Description: "Collects input and output traffic stats periodically and notifies in case traffic is above threshold"
		> Synopsis: "Interface input  and output traffic analyzer"
		> Rule file name: interface-input-output-traffic-snmp.rule
		> Sensor type: snmp 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1



		> More details:
		 Monitors interface input & output traffic and notifies when anomalies are found.
		 Four inputs control detection
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor. By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) high-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 800000000 octets. This rule will
		      set a dashboard color to red when *all* the input traffic is above
		      threshold for 180 seconds period. Use 8000000000 octets for 10G &
		      80000000000 for 100G interface.
		   3) low-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 500000000 octets . This rule will
		      set a dashboard color to yellow when *all* the input traffic is above
		      threshold for 180 seconds period, otherwise color is set to green.
		      Use 5000000000 octets for 10G & 50000000000 for 100G interface.
### Rule name: check-neighbor-state 
		> Description: "Collects interface neighbor state periodically and notifies when neighbor sate is unreachable"
		> Synopsis: "Interface neighbor state analyzer"
		> Rule file name: interface-neighbor-state.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1



		> More details:
		 Monitors interface ipv4 neighbor state and notifies when anomalies are found.
		 One input control detection
		
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
### Rule name: check-out-errors-netconf 
		> Description: "Collects the interface output error (errors (all), drops,discards, timeouts and runts) periodically and notifies in case of anomalies"
		> Synopsis: "Interface out-error analyzer"
		> Rule file name: interface-out-errors-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:A, Junos:15.1R1
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects interface out errors and notifies anomalies when error count increases.
### Rule name: check-out-errors 
		> Description: "This rule collects interface output error (errors(all), drops, discards, timeouts and runts) periodically and notifies in case of anomalies"
		> Synopsis: "Interface out-errors analyzer"
		> Rule file name: interface-out-errors.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Detects interface in errors and notifies when anomalies are found.
		 Two inputs control detection
		
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		
		   2) out-errors-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the error increases are greater than
		      'out-errors-threshold-variable' for 180s. If it sees any errors increase for a
		      period of less than 180s, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: check-out-traffic-iagent 
		> Description: "Collects the interface output traffic periodically and notifies in case of anomalies"
		> Synopsis: "Interface out-traffic analyzer"
		> Rule file name: interface-out-traffic-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:A, Junos:15.1R1
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects interface output traffic and notifies when anomalies are found.
### Rule name: check-out-traffic 
		> Description: "Collects output traffic(out-octets) periodically and notifies in case of traffic is above threshold"
		> Synopsis: "interface output traffic analyzer"
		> Rule file name: interface-out-traffic.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Monitors interface output traffic and notifies when anomalies are found.
		 Four inputs control detection
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) out-octets-stats-name, is a regular expression that matches the interface KPI
		      statistics counter name that you would like to monitor. By default it's
		      out-octets, Use proper counter name something like 'out-pkts' or
		      "out-unicast-pkts" or "out-multicast-pkts" etc.
		   3) out-octets-high-threshold, is the threshold that causes the rule to report
		      an anomaly.  By default it's 800000000 octets. This rule will set a
		      dashboard color to red when *all* the output traffic exceed threshold
		      for 180s. Use 8000000000 octets for 10G & 80000000000 for 100G interface.
		   4) out-octets-low-threshold, is the threshold that causes the rule to report
		      an anomaly.  By default it's 500000000 octets . This rule will set a
		      dashboard color to yellow when *all* the output traffic exceed
		      threshold for 180s, otherwise color is set to green. Use 5000000000
		      octets for 10G & 50000000000 for 100G interface.
### Rule name: check-interface-status-iagent 
		> Description: "Collects interface link oper state periodically and notifies when neighbor sate is down"
		> Synopsis: "Tnterface state analyzer"
		> Rule file name: interface-status-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:A, Junos:15.1R1
		> Supported product:MX, Platforms:A, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1
		> Supported product:QFX, Platforms:A, Junos:15.1R1



		> More details:
		 Monitors interface link state and notifies when anomalies are found.
### Rule name: check-interface-status 
		> Description: "Collects interface link oper state periodically and notifies when neighbor sate is down"
		> Synopsis: "Tnterface state analyzer"
		> Rule file name: interface-status.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Monitors interface link state and notifies when anomalies are found.
		 One input control detection
		
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
### Rule name: check-ifl-in-traffic 
		> Description: "Collects input traffic (in-octets) periodically and notifies in case of traffic is above threshold"
		> Synopsis: "Sub Interface input traffic analyzer."
		> Rule file name: logical-interface-in-traffic.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Monitors sub interface input traffic and notifies when anomalies are found.
		 Five inputs control detection
		   1) ifd-name, is a regular expression that matches the interfaces
		      that you would like to monitor.  By default it's '.*', which matches
		      all interfaces. Use something like 'ge.*' to match only gigabit
		      ethernet interfaces.
		   2) ifl-no, is a regular expression that matches the IFL index number that
		      you would like to monitor.  By default it's '.*', which matches all
		      interfaces. Use something like '0-10*' to match only 0 to 10 IFLs.
		   3) stats-name, is a regular expression that matches the sub interface KPI
		      statistics counter name that you would like to monitor. By default it's
		      in-octets, Use proper counter name something like 'in-pkts' or
		      "in-unicast-pkts" or "in-multicast-pkts" etc.
		   4) in-octets-high-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 80000000 octets (80 MB). This rule
		      will set a dashboard color to red when *all* the input traffic is above
		      threshold for 60 seconds period.
		   5) in-octets-low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 50000000 (50 MB)octets . This rule
		      will set a dashboard color to yellow when *all* the input traffic is
		      above threshold for 60 seconds period, otherwise color is set to green.
### Rule name: check-ifl-out-traffic 
		> Description: "Collects output traffic (out-octets) periodically and notifies in case of traffic is above threshold"
		> Synopsis: "Sub Interface output traffic analyzer."
		> Rule file name: logical-interface-out-traffic.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Monitors sub interface output traffic and notifies when anomalies are found.
		 Five inputs control detection
		   1) ifd-name, is a regular expression that matches the interfaces
		      that you would like to monitor.  By default it's '.*', which matches
		      all interfaces. Use something like 'ge.*' to match only gigabit
		      ethernet interfaces.
		   2) ifl-no, is a regular expression that matches the IFL index number that
		      you would like to monitor.  By default it's '.*', which matches all
		      interfaces. Use something like '0-10*' to match only 0 to 10 IFLs.
		   3) stats-name, is a regular expression that matches the sub interface KPI
		      statistics counter name that you would like to monitor. By default it's
		      out-octets, Use proper counter name something like 'out-pkts' or
		      "out-unicast-pkts" or "out-multicast-pkts" etc.
		   4) out-octets-high-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 80000000 octets (80 MB). This rule
		      will set a dashboard color to red when *all* the output traffic is above
		      threshold for 60 seconds period.
		   5) out-octets-low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 50000000 (50 MB)octets . This rule
		      will set a dashboard color to yellow when *all* the output traffic is
		      above threshold for 60 seconds period, otherwise color is set to green.
