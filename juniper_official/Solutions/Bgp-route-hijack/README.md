# HealthBot Bgp-route-hijack KPI rules and playbooks

## Bgp-route-hijack playbooks
### Playbook name: bgp-route-hijack-detection 
		> Description: "Playbook detects bgp ipv4 and ipv6 route hijack"
		> Synopsis: "Playbook detects route hijack"
		> Playbook file name: bgp-route-hijack.playbook
		> Detals:
		 Playbook contains multiple rules which detect BGP IPv4 and IPv4 route
		 hijacks and notifies when anomalies are found.
		
		 1) Rule bgp-route-hijack-v4.rule, detects the v4 route hijacks and notifies
		     anomalies when error count increases.
		 2) Rule bgp-route-hijack-v6.rule, detects the v4 route hijacks and notifies
		     anomalies when error count increases.

## Bgp-route-hijack rules

### Rule name: check-route-hijacking-v6 
		> Description: "Checks bgp ipv6 route hijacks"
		> Synopsis: "IPv4 bgp route hijack detector"
		> Rule file name: bgp-route-hijack-v6.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5110;
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;
			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Collects bgp session statistics and notifies when bgp v4 route hijacks.
### Rule name: check-route-hijacking-v4 
		> Description: "Checks bgp ipv4 route hijack"
		> Synopsis: "IPv4 bgp route hijack detector"
		> Rule file name: bgp-route-hijack-v4.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5110;
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;
			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Collects bgp session statistics and notifies when bgp v4 route hijack.
