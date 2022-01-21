# HealthBot Infra KPI rules and playbooks

## Infra playbooks

## Infra rules

### Rule name: check-jsr-kkcm-conn 
		> Description: "Report KKCM connection issues when NSR is configured"
		> Synopsis: "Check KKCM connections when NSR/JSR is enabled"
		> Rule file name: check-jsr-kkcm-conn.rule
		> Sensor type: iAgent 




		> More details:
		 Report KKCM connection issues, if nonstop-routing feature is configured.
		 If this rule reports an issue, make sure that nonstop-routing is indeed
		 configured. Try removing this configuration and then reconfiguring the same.
### Rule name: get-instance-details 


		> Rule file name: get-instance-details.rule
		> Sensor type: iAgent 




		> More details:
### Rule name: check-task-io-drops 
		> Description: "Monitors the task IO drops"
		> Synopsis: "Task I/O statistics analyzer"
		> Rule file name: task-io.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: task-io.yml;
		> More details:
### Rule name: check-task-memory-usage 
		> Description: "This rule collects task memory in use count periodically and notifies in case of anomalies"
		> Synopsis: "task memory in use analyzer"
		> Rule file name: task-memory.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: task-memory.yml;
		> More details:
