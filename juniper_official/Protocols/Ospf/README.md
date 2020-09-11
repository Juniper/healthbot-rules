# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN playbooks

## EVPN VXLAN rules

### Rule name: check-ospf-forwarding-table 
		> Description: "Checks if the route destination and next hop are correct"
		> Synopsis: "ospf session state analyzer"
		> Rule file name: ospf-kernel-route.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: ospf-kernel-route.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-spf-ospf-netconf 
		> Description: "Check SPF run time and count  for ospf"
		> Synopsis: "Spf ospf runtime and count KPI"
		> Rule file name: check-spf-ospf-netconf.rule

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
### Rule name: check-ospf-statistics-information 
		> Description: "Monitors the transmission and reception of hello packets"
		> Synopsis: "ospf hello statistics analyzer"
		> Rule file name: ospf-statistics.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: ospf.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: pfe-ddos-policer 
		> Description: "This rule collects ospf ddos policer stats periodically and notifies in case of anomalies"
		> Synopsis: "ospf session ddos analyzer"
		> Rule file name: pfe-ddos-policer.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: pfe-ddos-policer.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: fpc-link-stats 
		> Description: "This topic is to monitors and notify OSPF sessions hello packet statitics"
		> Synopsis: "ospf session hello statistics analyzer"
		> Rule file name: fpc-link-stats.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: fpc_link_stats.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-ospf-neighbor-information 
		> Description: "Monitors the OPSF neighbor states"
		> Synopsis: "OSPF session state analyzer"
		> Rule file name: ospf-neighbor-information.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: ospf.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-ospf-io-statistics-information 
		> Description: "Monitors OSPF's I/O statistics"
		> Synopsis: "OSPF IO statistics analyzer"
		> Rule file name: ospf-io-statistics.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: ospf.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-ospf-neighbor-state 
		> Description: "This rule collects ospf session state periodically and notifies in case of anomalies"
		> Synopsis: "ospf session state analyzer"
		> Rule file name: ospf-neighbor-state.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: ospf-neighbor.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
		   This rule checks health of each ospf neigbor state and notify in case any of the health monitored field crosses threshold
### Rule name: check-ddos-statistics 
		> Description: "Monitors ospf related distributed denial of service statistics"
		> Synopsis: "OSPF distributed denial of service statistics analyzer"
		> Rule file name: ddos-statistics.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: ddos-statistics.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: ospf-spf-count-netconf 
		> Description: "Collects data about ospf spf count"
		> Synopsis: "OSPF SPF count KPI"
		> Rule file name: ospf-spf-count-netconf.rule

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
