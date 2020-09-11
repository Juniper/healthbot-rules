# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN playbooks
### Playbook name: evo-route-summary-playbook 
		> Description: "Playbook checks each table's and protocol's route count and notifies anomaly when route count is above or below dynamic threshold"
		> Synopsis: "Route table and protocol routes key performance indicators"
		> Playbook file name: evo-route-summary.playbook
		> Detals:
		 Playbook contains multiple rules which monitors each route-table's and
		 protocol's router count and notifies when anomalies are found.
		 1) Rule "check-ascertain-routes" sets the dynamic thresholds based on
		    the learned data (route count of each table) using ML(Machine Learning)
		    algorithms and detects threshold breaches and notify anomalies.
		 2) Rule "check-protocol-route-coun" sets the dynamic thresholds based on
		    learned data (route count of each protocol) using ML(Machine Learning)
		    algorithms and detects threshold breaches and notify anomalies.
### Playbook name: evo-chassis-kpis-playbook 
		> Description: "Playbook monitor the chassis health i.e. RE and linecards temperatures, power and fan health"
		> Synopsis: "Chassis key performance indicators"
		> Playbook file name: evo-chassis-kpis.playbook
		> Detals:
### Playbook name: evo-rca-ospf-playbook 
		> Description: "Playbook detects OSPF protocol and its subsystems anomalies"
		> Synopsis: "OSPF RCA kpis"
		> Playbook file name: evo-rca-ospf-subsystems.playbook
		> Detals:
### Playbook name: evo-lldp-kpis-playbook 
		> Description: "Playbook checks health of each lldp session and notify anomalies"
		> Synopsis: "LLDP session statistics KPI playbook"
		> Playbook file name: evo-lldp-session-stats.playbook
		> Detals:
		 Playbook contains multiple rules which checks the health of system and
		 notifies when anomalies are found.
		 1) Rule "check-lldp-session-statistics" detects the LLDP session satistics threshold
		    breaches and notify anomalies.
		 2) Rule "get-lldp-state" collects the LLDP neighbor state.
		    and notify anomalies.
		 3) Rule "check-lldp-session" refers neighbor state information from rule
		    "get-lld-state" and detects the LLDP neighbor session state changes and
		    notify anomalies.
### Playbook name: evo-bgp-session-stats-playbook 
		> Description: "Playbook checks the BGP neighbor sessions health and notify anomaly when statistics are unusual"
		> Synopsis: "BGP neighbor sessions key performance indicators using iAgent sensor"
		> Playbook file name: evo-bgp-session-stats.playbook
		> Detals:
		 Playbook contains multiple rules which checks the statistics of BGP neighbor
		 sessions and notifies when anomalies are found.
		 1) Rule "evo-check-bgp-session-state" detects the BGP neighbor session state
		    changes and notify anomalies when session state is down.
		 2) Rule "evo-check-bgp-neighbor-flaps" detects the BGP neighbor session flaps
		    and notify anomalies when session state is down.
		 3) Rule "evo-check-bgp-received-routes" detects the received route count
		    threshold breaches and notify anomalies.
### Playbook name: evo-interface-kpis-playbook 
		> Description: "Playbook to check interface health w.r.t. links, flaps, input & output traffic and errors"
		> Synopsis: "Interface key performance indicators"
		> Playbook file name: evo-interface-kpis.playbook
		> Detals:
		 Playbook contains multiple rules which monitor interfaces and notifies when
		 anomalies are found.
		
		 1) Rule check-in-errors, detects the interface in errors and notifies
		 2) Rule check-out-errors, detects the interface out errors and notifies
		 3) Rule check-interface-flaps, detects interface flaps and notifies
		 4) Rule check-in-traffic, monitors the interface in traffic and notifies
		 5) Rule check-out-traffic, monitors the interface out traffic and notifies
		 6) Rule check-interface-status, monitors the interface status and notifies
### Playbook name: evo-system-kpis-playbook 
		> Description: "Playbook checks the system health i.e. system cpu, memory, storage and junos processes cpu and memory utilization"
		> Synopsis: "System key performance indicators"
		> Playbook file name: evo-system-kpis.playbook
		> Detals:

## EVPN VXLAN rules

### Rule name: evo-check-fpc-temperature 


		> Rule file name: evo-chassis-environment-fpc.rule




		> Detals:
### Rule name: evo-check-version 
		> Description: "Validates the product name and Junos version"
		> Synopsis: "System product name and software version analyzer"
		> Rule file name: evo-software-version.rule




		> Detals:
### Rule name: evo-check-process-memory 
		> Description: "Collects system process's memory utilization periodically and notifies anomalies when daemon memory usage exceed threshold"
		> Synopsis: "System processes memory utilization analyzer"
		> Rule file name: evo-system-process-memory.rule




		> Detals:
### Rule name: evo-check-bgp-received-routes 
		> Description: "Collects BGP session received routes count periodically and notifies anomaly when received route count exceed threshold"
		> Synopsis: "BGP received routes analyzer"
		> Rule file name: evo-bgp-received-routes.rule




		> Detals:
### Rule name: evo-check-process-cpu 
		> Description: "Collects system process's cpu utilization periodically and notifies anomalies when daemon CPU usage exceed threshold"
		> Synopsis: "System processes cpu analyzer"
		> Rule file name: evo-system-processes-cpu.rule




		> Detals:
### Rule name: evo-check-fan-health 
		> Description: "Collects chassis fan statistics periodically and notifies anomalies when fan status is NOK"
		> Synopsis: "Chassis fans health analyzer"
		> Rule file name: evo-chassis-fan.rule




		> Detals:
		 Monitors chassis fan health status and notifies when anomalies are found.
### Rule name: evo-check-bgp-neighbor-flaps 
		> Description: "iAgent sensor to collect telemetry data from network device"
		> Synopsis: "BGP iAgent sensor definition"
		> Rule file name: evo-bgp-neighbor-flap.rule




		> Detals:
### Rule name: evo-check-pem-temperature 


		> Rule file name: evo-chassis-environment-pem.rule




		> Detals:
### Rule name: evo-check-storage 
		> Description: "Collects filesystem storage usage periodically and notifies anomalies when used space exceed threshold"
		> Synopsis: "system storage usage analyzer"
		> Rule file name: evo-system-storage.rule

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
		> Helper files: system-storage.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects system storage utilization threshold breaches and notifies when
		 anomalies are found.
		 Two inputs control detection
		
		   1) storage-usage-high-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 80% of total size. This rule will
		      set a dashboard color to red when storage used exceed
		      'storage-usage-high-threshold'.
		
		   2) storage-usage-low-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 50%. This rule will set a dashboard
		      color to green when storage used below 'storage-usage-low-threshold'.
		      otherwise color is set to yellow as used % is between 50% and 80%.
### Rule name: evo-check-re-temperature 


		> Rule file name: evo-chassis-environment-re.rule




		> Detals:
### Rule name: evo-check-bgp-session-state 
		> Description: "Collects BGP session state periodically and notify anomalies when neighbor session down"
		> Synopsis: "BGP session state analyzer"
		> Rule file name: evo-bgp-neighbor-state.rule




		> Detals:
