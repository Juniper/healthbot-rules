# HealthBot Rib KPI rules and playbooks

## Rib playbooks
### Playbook name: route-summary-playbook 
		> Description: "Playbook checks each table's and protocol's route count and notifies anomaly when route count is above or below dynamic threshold"
		> Synopsis: "Route table and protocol routes key performance indicators"
		> Playbook file name: route-summary.playbook
		> Details:
		 Playbook contains multiple rules which monitors each route-table's and
		 protocol's router count and notifies when anomalies are found.
		 1) Rule "check-ascertain-routes" sets the dynamic thresholds based on
		    the learned data (route count of each table) using ML(Machine Learning)
		    algorithms and detects threshold breaches and notify anomalies.
		 2) Rule "check-protocol-route-coun" sets the dynamic thresholds based on
		    learned data (route count of each protocol) using ML(Machine Learning)
		    algorithms and detects threshold breaches and notify anomalies.

## Rib rules

### Rule name: check-protocol-route-count 
		> Description: "Collects total-route-count of each protocol and sets dynamic thresholds and notify anomaly when route count is abnormal"
		> Synopsis: "Protocols routes statistics analyzer"
		> Rule file name: route-table-protocol-summary.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: route-protocol-summary.yml;
		> More details:
		 Dynamically sets the route count threshold for each protocol of each route
		 table and notify anomaly when route count is aberrant.
### Rule name: check-ascertain-routes 
		> Description: "Collects total-route-count of each routing table and sets dynamic thresholds and notify anomaly when route count is abnormal"
		> Synopsis: "Routing table statistics analyzer"
		> Rule file name: route-tables-summary.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: route-summary.yml;
		> More details:
		 Dynamically sets the route count threshold for each route table and notify
		 anomaly when route count is aberrant.
