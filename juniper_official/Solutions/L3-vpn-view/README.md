# HealthBot L3-vpn-view KPI rules and playbooks

## L3-vpn-view playbooks
### Playbook name: vpn-view 
		> Description: "Playbook checks health of L3VPN session, PE and CE interface status and notify anomaly when statistics are unusual"
		> Synopsis: "L3VPN network health analyzer"
		> Playbook file name: l3vpn-network.playbook
		> Detals:
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

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
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
			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5110;
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;
			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
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
		 Collects L3VPN protocol status and PE & CE interface statistics and notifies
		 anomalies when any of the BGP session, CE or PE interface is down.
