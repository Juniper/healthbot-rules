# HealthBot SRX-security-monitoring KPI rules and playbooks

## SRX-security-monitoring playbooks
### Playbook name: srx-cluster-security-kpis-playbook 
		> Description: "Playbook checks SRX cluster system, linecard, SPU's cpu, memory and security parameters"
		> Synopsis: "SRX cluster system, linecard and security performance indicators"
		> Playbook file name: srx-cluster-security-kpis.playbook
		> Details:
		 Playbook contains multiple rules which monitors SRX cluster system,
		 linecard, SPU's CPU & Memory and security parameters and notifies when
		 anomalies are found.
		 1) Rule "check-spu-performance-srx-cluster-netconf" collects SPU performance
		    for each PIC and notifies in case of stats is above threshold.
		 2) Rule "check-flow-session-summary-netconf" collects and
		    monitors the active flow session details and notifies anomalies.
		 3) Rule "check-fpc-cpu-memory-usage-srx-cluster-netconf" collects system FPC
		    CPU statistics periodically and notifies anomalies when CPU utilization
		    exceed threshold.
		 4) Rule "check-interface-in-out-traffic-snmp" collects input and output
		    traffic periodically and notifies in case of traffic is above threshold.
		 5) Rule "check-system-cpu-memory-snmp" collects CPU, Memory Utilization
		    details from Routing Engines and notify anomalies based on threshold
		    values.
		 6) Rule "check-alarm-status-netconf" Monitors system security alarms and
		    notifies anomalies when alarms found.
		 7) Rule "check-appid-asc-cache-status-netconf" Verifies the status of
		    application system cache.
		 8) Rule "check-cpu-memory-utilization-netconf" Monitors spu cpu and memory
		    utilization and notifies when anomalies are found.
		 9) Rule "check-idp-memory-counter-netconf" Monitors idp memory counters
		    and notifies when anomalies are found.
		 10)Rule "check-idp-memory-utilization-netconf" Monitors idp memory
		    utilization and notifies anomalies when utilization exceeds threshold.
### Playbook name: srx-security-kpis-playbook 
		> Description: "Playbook checks SRX's system, linecard, SPU's cpu, memory and security parameters"
		> Synopsis: "SRX's system, linecard and security performance indicators"
		> Playbook file name: srx-security-kpis.playbook
		> Details:
		 Playbook contains multiple rules which monitors standalone SRX system,
		 linecard, SPU's CPU & Memory and security parameters and notifies when
		 anomalies are found.
		 1) Rule "check-spu-performance-netconf" collects SPU performance for each
		    PIC and notifies in case of stats is above threshold.
		 2) Rule "check-flow-session-summary-netconf" collects and monitors the
		    active flow session details and notifies anomalies.
		 3) Rule "check-fpc-cpu-memory-usage-netconf" collects system FPC CPU
		    statistics periodically and notifies anomalies when CPU utilization
		    exceed threshold.
		 4) Rule "check-interface-in-out-traffic-snmp" collects input and output
		    traffic periodically and notifies in case of traffic is above threshold.
		 5) Rule "check-system-cpu-memory-snmp" collects CPU, Memory Utilization
		    details from Routing Engines and notify anomalies based on threshold
		    values.
		 6) Rule "check-alarm-status-netconf" Monitors system security alarms and
		    notifies anomalies when alarms found.
		 7) Rule "check-appid-asc-cache-status-netconf" Verifies the status of
		    application system cache.
		 8) Rule "check-cpu-memory-utilization-netconf" Monitors spu cpu and memory
		    utilization and notifies when anomalies are found.
		 9) Rule "check-idp-memory-counter-netconf" Monitors idp memory counters
		    and notifies when anomalies are found.
		 10)Rule "check-idp-memory-utilization-netconf" Monitors idp memory
		    utilization and notifies anomalies when utilization exceeds threshold.

## SRX-security-monitoring rules

