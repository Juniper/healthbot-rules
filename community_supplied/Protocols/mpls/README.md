# HealthBot mpls KPI rules and playbooks

## mpls playbooks
### Playbook name: mpls-kpi-community 
		> Description: "To check if VRF interfaces and notifies when anomaly."
		> Synopsis: "VRF interface performance indicators"
		> Playbook file name: mpls-kpi-community.playbook
		> Detals:
		 Playbook contains multiple rules which checks for vrf interfaces
		 and count and notifies when anomalies are found.
		 1) Rule "check-vrf-interfaces-netconf" Check count of Interfaces per VRF
		    and notifies when anomalies are found.

## mpls rules

### Rule name: check-vrf-interfaces-netconf 
		> Description: "Check count of Iface per VRF"
		> Synopsis: "VRF Name:Iface membership KPI"
		> Rule file name: check-vrf-interfaces-netconf.rule

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
