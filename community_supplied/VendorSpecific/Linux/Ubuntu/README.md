# HealthBot Ubuntu KPI rules and playbooks

## Ubuntu playbooks

## Ubuntu rules

### Rule name: check-docker-cpu-mem-netconf 


		> Rule file name: check-docker-cpu-mem-netconf.rule


		> Helper files: [ linux_docker_stats_--no-stream.textfsm DockerStatsTable.yml];

		> Detals:
		 Monitors docker container's CPU and memory and notifies when anomalies are
		 found.
		 One input control detection
		
		   1) Threshold, is the threshold value for CPU and memory utilization takes
		   as input and pass to the rule to report an anomaly. By default value is 80
### Rule name: check-docker-cpu-mem 


		> Rule file name: check-docker-cpu-mem.rule




		> Detals:
		 Monitors docker container's CPU and memory and notifies when anomalies are
		 found.
		 One input control detection
		
		   1) Threshold, is the threshold value for CPU and memory utilization takes
		   as input and pass to the rule to report an anomaly. By default value is 80
