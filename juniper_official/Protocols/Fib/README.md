# HealthBot Fib KPI rules and playbooks

## Fib playbooks
### Playbook name: forwarding-table-summary 
		> Description: "Playbook monitors forwarding-table's each protocol's route count and notifies anomaly when route count is above static or dynamic threshold"
		> Synopsis: "Forwarding table and protocol routes key performance indicators"
		> Playbook file name: forwarding-table-summary.playbook
		> Details:
		 Playbook contains multiple rules which monitors forwarding-table's each
		 route-table's and protocol's router count and notifies when anomalies are
		 found.
		 1) Rule "check-fib-summary" collects forwarding-table's total-route-count
		 of each protocol and sets atatic and dynamic thresholds and notify anomaly
		 when route count is abnormal

## Fib rules

### Rule name: check-fib-summary 
		> Description: "Collects forwarding-table's total-route-count of each protocol and sets dynamic thresholds and notify anomaly when route count is abnormal"
		> Synopsis: "Forwarding-table protocols routes statistics analyzer"
		> Rule file name: fib-summary.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: fib.yml;
		> More details:
		 Detects forwarding-table of each route table and its protocol's route count
		 threshold breaches and notify anomaly when route count is aberrant.
