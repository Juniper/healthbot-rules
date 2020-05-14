# HealthBot Infra KPI rules and playbooks

## Infra playbooks

## Infra rules

### Rule name: check-task-io-drops 
		> Description: "Monitors the task IO drops"
		> Synopsis: "Task I/O statistics analyzer"
		> Rule file name: task-io.rule

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
		> Helper files: task-io.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-jsr-kkcm-conn 
		> Description: "Report KKCM connection issues when NSR is configured"
		> Synopsis: "Check KKCM connections when NSR/JSR is enabled"
		> Rule file name: check-jsr-kkcm-conn.rule




		> Detals:
		 Report KKCM connection issues, if nonstop-routing feature is configured.
		 If this rule reports an issue, make sure that nonstop-routing is indeed
		 configured. Try removing this configuration and then reconfiguring the same.
### Rule name: check-task-memory-usage 
		> Description: "This rule collects task memory in use count periodically and notifies in case of anomalies"
		> Synopsis: "task memory in use analyzer"
		> Rule file name: task-memory.rule

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
		> Helper files: task-memory.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
