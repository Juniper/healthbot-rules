# HealthBot Bgp-route-hijack KPI rules and playbooks

## Bgp-route-hijack playbooks
### Playbook name: bgp-route-hijack-detection 
		> Description: "Playbook detects bgp ipv4 and ipv6 route hijack"
		> Synopsis: "Playbook detects route hijack"
		> Playbook file name: bgp-route-hijack.playbook
		> Details:
		 Playbook contains multiple rules which detect BGP IPv4 and IPv4 route
		 hijacks and notifies when anomalies are found.
		
		 1) Rule bgp-route-hijack-v4.rule, detects the v4 route hijacks and notifies
		     anomalies when error count increases.
		 2) Rule bgp-route-hijack-v6.rule, detects the v4 route hijacks and notifies
		     anomalies when error count increases.

## Bgp-route-hijack rules

### Rule name: check-route-hijacking-v4 
		> Description: "Checks bgp ipv4 route hijack"
		> Synopsis: "IPv4 bgp route hijack detector"
		> Rule file name: bgp-route-hijack-v4.rule
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
		 Collects bgp session statistics and notifies when bgp v4 route hijack.
### Rule name: check-route-hijacking-v6 
		> Description: "Checks bgp ipv6 route hijacks"
		> Synopsis: "IPv4 bgp route hijack detector"
		> Rule file name: bgp-route-hijack-v6.rule
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
		 Collects bgp session statistics and notifies when bgp v4 route hijacks.
