# HealthBot Bgp KPI rules and playbooks

## Bgp playbooks
### Playbook name: snmp-bgp-playbook 


		> Playbook file name: snmp-bgp.playbook
		> Detals:
### Playbook name: bgp-additional-kpis 
		> Description: "To check vrf peer ip usage and notifies when anomaly."
		> Synopsis: "VRF peer ip and forwarding table performance indicators"
		> Playbook file name: bgp-additional-kpis.playbook
		> Detals:
		 Playbook contains multiple rules which checks for vrf peer ip in
		 forwarding table and notifies when anomalies are found.
		 1) Rule "collect-peerip-in-vrf-table-oc" Collects peer addrresses in the vrf tables
		     and provides vector data to check-peer rule.
		 2) Rule "check-peer" check vrf  peer address is present in the forwarding table
		    and notifies when anomalies are found.
		 3) Rule "check-forwarding-table-netconf" Check if peer ip is present in forwarding table
		    aand provides vector data to check-peer rule.
		 4) Rule "check-bgp-config-netconf" monitors the BGP neighbor configurations.
		 5) Rule "check-bgp-summary-netconf.rule" monitors the BGP neighbor summary and notifies
		 6) Rule "check-ecmp-active-paths-netconf.rule" monitors the health of ECMP active path
		    count in control plane and notifies when anomalies are found.

## Bgp rules

### Rule name: check-forwarding-table-netconf 
		> Description: "Check if peer ip is present in forwarding table."
		> Synopsis: "Have fwd table entry for neighbour's IP KPI"
		> Rule file name: check-forwarding-table-netconf.rule

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
### Rule name: check-ecmp-active-paths-netconf 
		> Description: "Collects the ECMP active path count periodically and notifies in case of anomalies"
		> Synopsis: "ECMP active path analyzer"
		> Rule file name: check-ecmp-active-paths-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-bgp-summary-netconf 
		> Description: "Monitors the BGP neighbor summary"
		> Synopsis: "BGP neighbor analyzer"
		> Rule file name: check-bgp-summary-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-nlri-rd-rt-netconf 
		> Description: "To check if NLRI RD:RT are present "
		> Synopsis: "BGP Neighbor  NLRI RD:RT"
		> Rule file name: check-nlri-rd-rt-netconf.rule

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
### Rule name: collect-peerip-in-vrf-table-oc 
		> Description: "Collects peer addrresses in the vrf tables"
		> Synopsis: "Neighbor ip in vrf table."
		> Rule file name: collect-peerip-in-vrf-table-oc.rule

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
### Rule name: check-peer 
		> Description: "To check vrf  peer address is present in the forwarding tble"
		> Synopsis: "Have fwd table entry for neighbour's IP KPI"
		> Rule file name: check-peer.rule

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
### Rule name: check-snmp-bgp-neighbor-flaps 
		> Description: "Collects BGP session details and notify anomalies based on threshold values "
		> Synopsis: "BGP neighbor flaps, neighbor state change detector"
		> Rule file name: snmp-bgp-neighbors.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX46000;
			> Supported platforms: EX4650;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: PTX5000;
			> Supported platforms: [ PTX1000 PTX10000 ];
			> Supported platforms: QFX5100;
			> Supported platforms: [ QFX10000 QFX5110 QFX5200 ];
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects BGP neighbor state changes and notifies when anomalies are found.
		 One input control detection
		
		   1) "neighbors" is a regular expression that matches the BGP neighbors
		      that you would like to monitor.  By default it's '.*', which matches
		      all bgp neighbors. Use something like '172.16.*' to match all neighbor
		      addresses which are in 172.16.0.0/16 network range.
		   2) flap-count-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default value is 80
### Rule name: check-bgp-config-netconf 
		> Description: "Monitors the BGP neighbor configurations"
		> Synopsis: "BGP neighbor analyzer"
		> Rule file name: check-bgp-config-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.1.0
		> Detals:
