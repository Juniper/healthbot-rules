# HealthBot L3-vpn-view KPI rules and playbooks

## L3-vpn-view playbooks
### Playbook name: vpn-view 
		> Description: "Playbook checks health of L3VPN session, PE and CE interface status and notify anomaly when statistics are unusual"
		> Synopsis: "L3VPN network health analyzer"
		> Playbook file name: l3vpn-network.playbook
		> Details:
		 Collects L3VPN protocol status and PE & CE interface statistics and notifies
		 anomalies when any of the BGP session, CE or PE interface is down.
		 Rule get-interface-details, collects interface statistics.
		 Rule get-routing-instance-details, collects routing instance details
		 Network rule check-l3vpn-state, Analyzes the routing instance, PE and CE
		 interface status and notifies anomalies when any of the state is down.

## L3-vpn-view rules

### Rule name: get-routing-instance-details 
		> Description: "Collects routing instance bgp peer status periodically"
		> Synopsis: "Routing details collector."
		> Rule file name: l3vpn-network.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
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
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Collects L3VPN protocol status and PE & CE interface statistics and notifies
		 anomalies when any of the BGP session, CE or PE interface is down.
