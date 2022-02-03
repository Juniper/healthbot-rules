# HealthBot CGNAT KPI rules and playbooks

## CGNAT playbooks
### Playbook name: cgnat-service-kpis 
		> Description: "Collects CGNAT information and displays session count, extern IP count, port block errors, port blocks, service CPU and memory utilization "
		> Synopsis: "CGNAT services KPI"
		> Playbook file name: cgnat-service-kpis.playbook
		> Details:
		 This playbook collects the CGNAT statistics like sessions, internal IPs,
		 external IPs and computes and display Session count, IP mapping, pools,
		 ports used, ports blocks, errors, service cpu and memory utilization.

## CGNAT rules

### Rule name: check-nat-mapping 
		> Description: "Monitors the CGNAT utilization"
		> Synopsis: "CGNAT mapping statistics"
		> Rule file name: check-CGNAT-mapping-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:18.1R1


		> Helper files: cgnat_multirow.py;
		> More details:
		 Monitors CGNAT relevant metrices and displays the internal and external mapping counts
		 Please modify the sensor frequency according CGNAT table size on production environment
### Rule name: check-port-block-stats 
		> Description: "Monitors CGNAT port block"
		> Synopsis: "CGNAT port block analyzer"
		> Rule file name: check-CGNAT-port-block-stats.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:18.1R1


		> Helper files: port-block.yml;
		> More details:
		 Monitors CGNAT relevant metrices and displays the CGNAT port blocks statistics
		 Please modify the sensor frequency according CGNAT table size on production environment
### Rule name: check-service-cpu 
		> Description: "Monitors the CGNAT cpu utilization"
		> Synopsis: "CGNAT CPU utilization analyzer"
		> Rule file name: check-CGNAT-service-cpu.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:18.1R1


		> Helper files: cpu.yml;
		> More details:
		 Monitors CGNAT service CPU utilization for different interfaces and service sets.
### Rule name: check-service-memory 
		> Description: "Monitors the CGNAT service memory utilization"
		> Synopsis: "CGNAT memory utilization analyzer"
		> Rule file name: check-CGNAT-service-memory.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:18.1R1


		> Helper files: memory.yml;
		> More details:
		 Monitors the CGNAT service memory utilization for interfaces and service sets.
