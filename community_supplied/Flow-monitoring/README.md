# HealthBot Flow-monitoring KPI rules and playbooks

## Flow-monitoring playbooks
### Playbook name: traffic-flow-monitoring-ipv6-ipfix 
		> Description: "Playbook monitors IPv6 ipfix flows and notifies anomalies when flow traffic rate exceeds threshold value"
		> Synopsis: "Netflow ipfix ipv6 flow analyzer"
		> Playbook file name: traffic-flow-monitoring-ipv6-ipfix.playbook
		> Detals:
		 Playbook contains a rule which monitors IPv6 ipfix flows and notifies
		 anomalies when flow traffic rate exceeds threshold value.
		
		 1) Rule monitor-ipfix-ipv6-flows-traffic, Monitors IPV6 nfv10(ipfix) flows
		    and notifies anomaly when each flow's traffic rate is above threshold
### Playbook name: traffic-flow-monitoring-ipv4-nfv9 
		> Description: "Playbook monitors IPv4 netflow version9 flows and notifies anomalies when flow traffic rate exceeds threshold value"
		> Synopsis: "Netflow netflow version9 IPv4 flow analyzer"
		> Playbook file name: traffic-flow-monitoring-ipv4-nfv9.playbook
		> Detals:
		 Playbook contains a rule which monitors IPv4 netflow version 9 flows and
		 notifies anomalies when flow traffic rate exceeds threshold value.
		
		 1) Rule monitor-nfv9-ipv4-flows-traffic, Monitors IPv4 netflow version9 flows
		    and notifies anomaly when each flow's traffic rate is above threshold
### Playbook name: traffic-flow-monitoring-ipv4-ipfix 
		> Description: "Playbook monitors IPv4 ipfix flows and notifies anomalies when flow traffic rate exceeds threshold value"
		> Synopsis: "Netflow ipfix ipv4 flow analyzer"
		> Playbook file name: traffic-flow-monitoring-ipv4-ipfix.playbook
		> Detals:
		 Playbook contains a rule which monitors IPv4 ipfix flows and notifies
		 anomalies when flow traffic rate exceeds threshold value.
		
		 1) Rule monitor-ipfix-ipv4-flows-traffic, Monitors IPV4 nfv10(ipfix) flows
		    and notifies anomaly when each flow's traffic rate is above threshold
### Playbook name: traffic-flow-monitoring-ipv6-nfv9 
		> Description: "Playbook monitors IPv6 netflow version9 flows and notifies anomalies when flow traffic rate exceeds threshold value"
		> Synopsis: "Netflow netflow version9 IPv6 flow analyzer"
		> Playbook file name: traffic-flow-monitoring-ipv6-nfv9.playbook
		> Detals:
		 Playbook contains a rule which monitors IPv6 netflow version 9 flows and
		 notifies anomalies when flow traffic rate exceeds threshold value.
		
		 1) Rule monitor-nfv9-ipv6-flows-traffic, Monitors IPv6 netflow version9 flows
		    and notifies anomaly when each flow's traffic rate is above threshold
### Playbook name: traffic-flow-monitoring-mpls-ipv4-ipfix 
		> Description: "Playbook monitors MPLS IPv4 ipfix flows and notifies anomalies when flow traffic rate exceeds threshold value"
		> Synopsis: "Netflow ipfix mpls ipv4 flow analyzer"
		> Playbook file name: traffic-flow-monitoring-mpls-ipv4-ipfix.playbook
		> Detals:
		 Playbook contains a rule which monitors MPLS IPv4 ipfix flows and notifies
		 anomalies when flow traffic rate exceeds threshold value.
		
		 1) Rule monitor-nfv10-mpls-ipv4-flows-traffic, Monitors MPLS IPV4
		    nfv10(ipfix) flows and notifies anomaly when each flow's traffic rate is
		    above threshold

## Flow-monitoring rules

### Rule name: monitor-nfv9-ipv6-flows-traffic 
		> Description: "Monitors netflow version9 IPv6 flows and notifies anomaly when each flow's traffic rate is above threshold"
		> Synopsis: "Netflow version 9 IPv6 flow analyzer"
		> Rule file name: monitor-ipv6-flows-nfv9-traffic.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors netflow version 9 IPv6 traffic flows and notified anomaly when
		 traffic rate is above threshold.
		 Seven inputs controls detection
		
		   1) input-source-address variable, is a regular expression that matches the
		      source ip address of the flow that you would like to monitor. By
		      default it's '.*', which matches all ip addresses. Use something like
		      '::172:16|::172:32' to match specific source addresses.
		
		   2) input-destination-address variable, is a regular expression that matches
		      the destination ip address of the flow that you would like to monitor.
		      By default it's '.*', which matches all ip addresses. Use something
		      like '::172:16|::172:32' to match specific destination addresses.
		   3) input-source-port variable, is a regular expression that matches
		      the source port of the flow that you would like to monitor. By default
		      it's '.*', which matches all ports. Use something like '22' to match
		      source scp port.
		   4) input-destination-port variable, is a regular expression that matches
		      the destination port of the flow that you would like to monitor. By
		      default it's '.*', which matches all ports. Use something like '22'
		      to match source scp port.
		   5) input-in-interface variable, is a regular expression that matches
		      the ingress interface of the flow that you would like to monitor. By
		      default it's '.*', which matches all interfaces. Use something like
		      'ge.*' to match only gigabit ethernet interfaces.
		   6) input-protocol variable, is a regular expression that matches protocol
		      of the flow that you would like to monitor. By default it's '.*', which
		      matches all protocols. Use something like '179' to match only protocol
		      BGP.
		   7) traffic-rate-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 50MB. This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'traffic-rate-threshold', otherwise color is set to green.
### Rule name: monitor-nfv9-ipv4-flows-traffic 
		> Description: "Monitors netflow version9 IPv4 flows and notifies anomaly when each flow's traffic rate is above threshold"
		> Synopsis: "Netflow version 9 IPv4 flow analyzer"
		> Rule file name: monitor-ipv4-flows-nfv9-traffic.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors netflow version 9 IPv4 traffic flows and notified anomaly when
		 traffic rate is above threshold.
		 Seven inputs controls detection
		
		   1) input-source-address variable, is a regular expression that matches the
		      source ip address of the flow that you would like to monitor. By
		      default it's '.*', which matches all ip addresses. Use something like
		      '192.162.1.1|172.16.1.1' to match specific source addresses.
		
		   2) input-destination-address variable, is a regular expression that matches
		      the destination ip address of the flow that you would like to monitor.
		      By default it's '.*', which matches all ip addresses. Use something
		      like '192.162.1.1|172.16.1.1' to match specific destination addresses.
		   3) input-source-port variable, is a regular expression that matches
		      the source port of the flow that you would like to monitor. By default
		      it's '.*', which matches all ports. Use something like '22' to match
		      source scp port.
		   4) input-destination-port variable, is a regular expression that matches
		      the destination port of the flow that you would like to monitor. By
		      default it's '.*', which matches all ports. Use something like '22'
		      to match source scp port.
		   5) input-in-interface variable, is a regular expression that matches
		      the ingress interface of the flow that you would like to monitor. By
		      default it's '.*', which matches all interfaces. Use something like
		      'ge.*' to match only gigabit ethernet interfaces.
		   6) input-protocol variable, is a regular expression that matches protocol
		      of the flow that you would like to monitor. By default it's '.*', which
		      matches all protocols. Use something like '179' to match only protocol
		      BGP.
		   7) traffic-rate-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 50MB. This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'traffic-rate-threshold', otherwise color is set to green.
### Rule name: monitor-ipfix-ipv4-flows-traffic 
		> Description: "Monitors ipfix IPv4 flows and notifies anomaly when each flow's traffic rate is above threshold"
		> Synopsis: "Netflow version 10 IPv4 flow analyzer"
		> Rule file name: monitor-ipv4-flows-ipfix-traffic.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors netflow version 10(ipfix) IPv4 traffic flows and notified anomaly when
		 traffic rate is above threshold.
		 Seven inputs controls detection
		
		   1) input-source-address variable, is a regular expression that matches the
		      source ip address of the flow that you would like to monitor. By
		      default it's '.*', which matches all ip addresses. Use something like
		      '192.162.1.1|172.16.1.1' to match specific source addresses.
		
		   2) input-destination-address variable, is a regular expression that matches
		      the destination ip address of the flow that you would like to monitor.
		      By default it's '.*', which matches all ip addresses. Use something
		      like '192.162.1.1|172.16.1.1' to match specific destination addresses.
		   3) input-source-port variable, is a regular expression that matches
		      the source port of the flow that you would like to monitor. By default
		      it's '.*', which matches all ports. Use something like '22' to match
		      source scp port.
		   4) input-destination-port variable, is a regular expression that matches
		      the destination port of the flow that you would like to monitor. By
		      default it's '.*', which matches all ports. Use something like '22'
		      to match source scp port.
		   5) input-in-interface variable, is a regular expression that matches
		      the ingress interface of the flow that you would like to monitor. By
		      default it's '.*', which matches all interfaces. Use something like
		      'ge.*' to match only gigabit ethernet interfaces.
		   6) input-protocol variable, is a regular expression that matches protocol
		      of the flow that you would like to monitor. By default it's '.*', which
		      matches all protocols. Use something like '179' to match only protocol
		      BGP.
		   7) traffic-rate-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 50MB. This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'traffic-rate-threshold', otherwise color is set to green.
### Rule name: monitor-ipfix-ipv6-flows-traffic 
		> Description: "Monitors netflow version 10(ipfix) IPv6 flows and notifies anomaly when each flow's traffic rate is above threshold"
		> Synopsis: "Netflow version 10(ipfix) IPv6 flow analyzer"
		> Rule file name: monitor-ipv6-flows-ipfix-traffic.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors netflow version 10(ipfix) IPv6 traffic flows and notified anomaly when
		 traffic rate is above threshold.
		 Seven inputs controls detection
		
		   1) input-source-address variable, is a regular expression that matches the
		      source ip address of the flow that you would like to monitor. By
		      default it's '.*', which matches all ip addresses. Use something like
		      '::172:16|::172:32' to match specific source addresses.
		
		   2) input-destination-address variable, is a regular expression that matches
		      the destination ip address of the flow that you would like to monitor.
		      By default it's '.*', which matches all ip addresses. Use something
		      like '::172:16|::172:32' to match specific destination addresses.
		   3) input-source-port variable, is a regular expression that matches
		      the source port of the flow that you would like to monitor. By default
		      it's '.*', which matches all ports. Use something like '22' to match
		      source scp port.
		   4) input-destination-port variable, is a regular expression that matches
		      the destination port of the flow that you would like to monitor. By
		      default it's '.*', which matches all ports. Use something like '22'
		      to match source scp port.
		   5) input-in-interface variable, is a regular expression that matches
		      the ingress interface of the flow that you would like to monitor. By
		      default it's '.*', which matches all interfaces. Use something like
		      'ge.*' to match only gigabit ethernet interfaces.
		   6) input-protocol variable, is a regular expression that matches protocol
		      of the flow that you would like to monitor. By default it's '.*', which
		      matches all protocols. Use something like '179' to match only protocol
		      BGP.
		   7) traffic-rate-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 50MB. This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'traffic-rate-threshold', otherwise color is set to green.
### Rule name: monitor-ipfix-mpls-ipv4-flows-traffic 
		> Description: "Monitors netflow version 10(ipfix) IPv4 flows of MPLS and notifies anomaly when each flow's traffic rate is above threshold"
		> Synopsis: "Netflow version 10 IPv4 flow analyzer"
		> Rule file name: monitor-mpls-ipv4-flows-ipfix-traffic.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors netflow version 10(ipfix) MPLS IPv4 traffic flows and notified anomaly when
		 traffic rate is above threshold.
		 Seven inputs controls detection
		
		   1) input-source-address variable, is a regular expression that matches the
		      source ip address of the flow that you would like to monitor. By
		      default it's '.*', which matches all ip addresses. Use something like
		      '192.162.1.1|172.16.1.1' to match specific source addresses.
		
		   2) input-destination-address variable, is a regular expression that matches
		      the destination ip address of the flow that you would like to monitor.
		      By default it's '.*', which matches all ip addresses. Use something
		      like '192.162.1.1|172.16.1.1' to match specific destination addresses.
		   3) input-source-port variable, is a regular expression that matches
		      the source port of the flow that you would like to monitor. By default
		      it's '.*', which matches all ports. Use something like '22' to match
		      source scp port.
		   4) input-destination-port variable, is a regular expression that matches
		      the destination port of the flow that you would like to monitor. By
		      default it's '.*', which matches all ports. Use something like '22'
		      to match source scp port.
		   5) input-in-interface variable, is a regular expression that matches
		      the ingress interface of the flow that you would like to monitor. By
		      default it's '.*', which matches all interfaces. Use something like
		      'ge.*' to match only gigabit ethernet interfaces.
		   6) input-protocol variable, is a regular expression that matches protocol
		      of the flow that you would like to monitor. By default it's '.*', which
		      matches all protocols. Use something like '179' to match only protocol
		      BGP.
		   7) traffic-rate-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 50MB. This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'traffic-rate-threshold', otherwise color is set to green.
