# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN playbooks
### Playbook name: snmp-interface-playbook 


		> Playbook file name: snmp-interface.playbook
		> Detals:
### Playbook name: loopback-IP-IPv6-verification 
		> Description: "To check if  ipv4/ipv6 address are present on the lo0 interface,ipv6 link local address is present for each interface."
		> Synopsis: "ipv4/ipv6 loopback and ipv6 link-local address"
		> Playbook file name: loopback-IP-IPv6-verification.playbook
		> Detals:
		 Playbook contains multiple rules which checks if ipv4/ipv6 addresses are
		 present on lo0,checks for ipv6 link local address and notifies
		 when anomalies are found.
		 1) Rule "check-lo0-address-netconf" checks for ipv4 address on lo0 interface
		    and notifies anomalies are found.
		 2) Rule "check-lo0-address-ipv6-netconf" checks for ipv6 address on lo0 interface
		    and notifies anomalies are found.
		 3) Rule "count-lo0-address-netconf" counts number of ipv4 addresses on lo0 and
		    notifies anomalies.
		 4) Rule "count-lo0-address-ipv6-netconf" counts number of ipv6 addresses on lo0 and
		    notifies anomalies.
		 5) Rule "check-ipv6-local-address-netconf" checks for ipv6 link local address on
		    interfaces and notifies anomalies.

## EVPN VXLAN rules

### Rule name: count-lo0-address-netconf 
		> Description: "Check whether IP address is configured under lo0 interface"
		> Synopsis: "lo0 configuration kpi"
		> Rule file name: count-lo0-address-netconf.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-interface-health-snmp 
		> Description: "Using this rule any one of the interface statistics counter (in and out errors, packets, octets, flaps) will be monitored"
		> Synopsis: "Interface KPI monitor based on description"
		> Rule file name: snmp-health-monitor-based-on-interface-description.rule




		> Detals:
### Rule name: check-lo0-address-ipv6-netconf 
		> Description: "Collects the IPV6 address configured under lo0 interface"
		> Synopsis: "lo0 ipv6 address configuration KPI"
		> Rule file name: check-lo0-address-ipv6-netconf.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-interface-throughput-oc 
		> Description: "Monitors interface throughput and generates triggers on customizable threshold crossing"
		> Synopsis: "Interface throughput threshold crossing"
		> Rule file name: oc-interface-throughput.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-interface-health-netconf 
		> Description: "Using this rule any one of the interface statistics counter (in and out errors, packets, octets, flaps) will be monitored"
		> Synopsis: "Interface KPI monitor based on description"
		> Rule file name: netconf-health-monitor-based-on-interface-description.rule




		> Detals:
### Rule name: check-interface-throughput-snmp 
		> Description: "Monitors interface throughput and generates triggers on customizable threshold crossing"
		> Synopsis: "Interface throughput threshold crossing"
		> Rule file name: snmp-interface-throughput.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: snmp-check-interface-flaps 

		> Synopsis: "Interface flaps analyzer"
		> Rule file name: snmp-interface-flaps.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Collectes interface flaps count
		
### Rule name: check-interface-throughput-netconf 
		> Description: "Monitors interface throughput and generates triggers on customizable threshold crossing"
		> Synopsis: "Interface throughput threshold crossing"
		> Rule file name: netconf-interface-throughput.rule




		> Detals:
### Rule name: snmp-check-interface-statistics 
		> Description: "Collects interface link oper state periodically and notifies when neighbor sate is down and also collects interface stats like in-errors,in-octests,out-errors,out-octets and notifies when these counters crosses threshold values"
		> Synopsis: "Tnterface state and stats analyzer"
		> Rule file name: snmp-interface-status.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Monitors interface state, input traffic, output traffic, input errors and output errors and notifies when anomalies are found.
		 Below are the inputs to control detection
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
		      for 600s. Use 8000000000 octets for 10G & 80000000000 for 100G interface.
		   4) out-octets-low-threshold, is the threshold that causes the rule to report
		      an anomaly.  By default it's 500000000 octets . This rule will set a
		      dashboard color to yellow when *all* the output traffic exceed
		      threshold for 600s, otherwise color is set to green. Use 5000000000
		      octets for 10G & 50000000000 for 100G interface.
		   5) stats-name, is a regular expression that matches the interface KPI
		      statistics counter name that you would like to monitor. By default it's
		      in-octets, Use proper counter name something like 'in-pkts' or
		      "in-unicast-pkts" or "in-multicast-pkts" etc.
		   6) in-octets-high-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 800000000 octets. This rule will
		      set a dashboard color to red when *all* the input traffic is above
		      threshold for 600 seconds period. Use 8000000000 octets for 10G &
		      80000000000 for 100G interface.
		   7) in-octets-low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 500000000 octets . This rule will
		      set a dashboard color to yellow when *all* the input traffic is above
		      threshold for 600 seconds period, otherwise color is set to green.
		      Use 5000000000 octets for 10G & 50000000000 for 100G interface.
		   8) in-errors-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the error increases are greater than
		      'in-errors-threshold-variable' for 600s. If it sees any errors increase for a
		      period of less than 600s, it'll turn the color to yellow,
		      otherwise color is set to green.
		   9) in-errors-stats-name, is the error stats counter name in-error which is
		      cumaulative of in-fram-errors, in-resource-errors, in-giants, in-drops,
		      in-discards and mtu-errors. Default value is in-errors.
		   10) out-errors-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the error increases are greater than
		      'out-errors-threshold-variable' for 600s. If it sees any errors increase for a
		      period of less than 600s, it'll turn the color to yellow,
		      otherwise color is set to green.
		   11) flaps-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the flap-increases are greater than
		      'flaps-threshold-variable' for 600s. If it sees any flaps increase for a
		      period of less than 600s, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: count-lo0-address-ipv6-netconf 
		> Description: "Check whether IPV6 address is configured under lo0 interface"
		> Synopsis: "lo0 ipv6 configuration kpi"
		> Rule file name: count-lo0-address-ipv6-netconf.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-lo0-address-netconf 
		> Description: "Collects the IP address configured under lo0 interface"
		> Synopsis: "lo0 ip address configuration KPI"
		> Rule file name: check-lo0-address-netconf.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-ifl-in-traffic-mbps 
		> Description: "Collects input traffic (in-octets) periodically and notifies in case of traffic is above threshold"
		> Synopsis: "Sub Interface input traffic analyzer."
		> Rule file name: check-ifl-in-traffic-mbps.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
		 Monitors interface input traffic in Mbs and notifies when anomalies are found.
		 Six inputs control detection
		   1) ifd-name, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) ifl-no, is a regular expression that matches the
		      interfaces ifl that you would like to monitor.  By default it's
		      '.*', which matches all sub interfaces.
		   3) decimal-places, number of decimal places to keep in the mbps output.
		      By default it's 4.
		   4) stats-name, is a regular expression that matches the interface KPI
		      statistics counter name that you would like to monitor. By default it's
		      in-octets, Use proper counter name something like 'in-pkts' or
		      "in-unicast-pkts" or "in-multicast-pkts" etc.
		   5) in-mbps-high-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 1000 mbps. This rule will
		      set a dashboard color to red when *all* the input traffic is above
		      threshold for 180 seconds period.
		   6) in-mbps-low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 700 mbps. This rule will
		      set a dashboard color to yellow when *all* the input traffic is above
		      threshold for 180 seconds period, otherwise color is set to green.
### Rule name: check-ipv6-local-address-netconf 
		> Description: "Check if ipv6 local address is present."
		> Synopsis: "IPv6 Link Local Present KPI"
		> Rule file name: check-ipv6-local-address-netconf.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-ifl-out-traffic-mbps 
		> Description: "Collects output traffic (out-octets) periodically and notifies in case of traffic is above threshold"
		> Synopsis: "Sub Interface output traffic analyzer."
		> Rule file name: check-ifl-out-traffic-mbps.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
		 Monitors interface output traffic in mbps and notifies when anomalies are found.
		 Six inputs control detection
		   1) ifd-name, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) ifl-no, is a regular expression that matches the
		      interfaces ifl that you would like to monitor.  By default it's
		      '.*', which matches all sub interfaces.
		   3) decimal-places, number of decimal places to keep in the mbps output.
		      By default it's 4.
		   4) stats-name, is a regular expression that matches the interface KPI
		      statistics counter name that you would like to monitor.
		   5) out-mbps-high-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 1000 mbps. This rule will
		      set a dashboard color to red when *all* the output traffic is above
		      threshold for 180 seconds period.
		   6) out-mbps-low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 700 mbps. This rule will
		      set a dashboard color to yellow when *all* the output traffic is above
		      threshold for 180 seconds period, otherwise color is set to green.
### Rule name: check-interface-status-description 
		> Description: "Collects interface link oper state periodically and notifies when neighbor sate is down"
		> Synopsis: "Tnterface state analyzer"
		> Rule file name: interface-status.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
		 Monitors interface link state and notifies when anomalies are found.
		 Two input control detection
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) description, is matches the interface description that you would
		      like to monitor.  By default it's  '.*', which matches all interfaces.
