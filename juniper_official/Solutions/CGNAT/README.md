# HealthBot CGNAT KPI rules and playbooks

## CGNAT playbooks
### Playbook name: cgnat-service-kpis 
		> Description: "Collects CGNAT information and displays session count, extern IP count, port block errors, port blocks, service CPU and memory utilization "
		> Synopsis: "CGNAT services KPI"
		> Playbook file name: cgnat-service-kpis.playbook
		> Detals:
		 This playbook collects the CGNAT statistics like sessions, internal IPs,
		 external IPs and computes and display Session count, IP mapping, pools,
		 ports used, ports blocks, errors, service cpu and memory utilization.

## CGNAT rules

### Rule name: check-nat-mapping 
		> Description: "Monitors the CGNAT utilization"
		> Synopsis: "CGNAT mapping statistics"
		> Rule file name: check-CGNAT-mapping-statistics.rule

		> Supported products: MX 
		> Supported products: MX 

			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: cgnat_multirow.py;
		> Supported healthbot version: 4.0.0
		> Detals:
### Rule name: check-port-block-stats 
		> Description: "Monitors CGNAT port block"
		> Synopsis: "CGNAT port block analyzer"
		> Rule file name: check-CGNAT-port-block-stats.rule

		> Supported products: MX 

			> Supported platforms: All;
		> Helper files: port-block.yml;
		> Supported healthbot version: 4.0.0
		> Detals:
### Rule name: check-service-cpu 
		> Description: "Monitors the CGNAT cpu utilization"
		> Synopsis: "CGNAT CPU utilization analyzer"
		> Rule file name: check-CGNAT-service-cpu.rule

		> Supported products: MX 

			> Supported platforms: All;
		> Helper files: cpu.yml;
		> Supported healthbot version: 4.0.0
		> Detals:
### Rule name: check-service-memory 
		> Description: "Monitors the CGNAT service memory utilization"
		> Synopsis: "CGNAT memory utilization analyzer"
		> Rule file name: check-CGNAT-service-memory.rule

		> Supported products: MX 

			> Supported platforms: All;
		> Helper files: memory.yml;
		> Supported healthbot version: 4.0.0
		> Detals:
