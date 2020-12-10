# HealthBot Arista KPI rules and playbooks

## Arista playbooks

## Arista rules

### Rule name: check-arista-eos-fan-ps-status-netconf 
		> Description: "Monitors FAN and power supply health and notifies anomaly if status is not ok."
		> Synopsis: "Chassis fan and power supply status analyzer"
		> Rule file name: check-arista-eos-fan-ps-status-netconf.rule


		> Helper files: [ AristaFanStatusTable.yml arista_eos_show_system_environment_cooling.textfsm ];

		> Detals:
### Rule name: check-arista-eos-interface-state-netconf 
		> Description: "Collects interface statistics periodically and notifies when interface operator state is down"
		> Synopsis: "Interface state analyzer"
		> Rule file name: check-arista-eos-interface-state-netconf.rule


		> Helper files: AristaInterfaceStatusTable.yml;

		> Detals:
### Rule name: check-arista-eos-kernel-ip-counters-netconf 
		> Description: "Monitors kernel ip counters and detects discards"
		> Synopsis: "Kernel IP counter statistics analyzer"
		> Rule file name: check-arista-eos-kernel-ip-counters-netconf.rule


		> Helper files: [ AristaKernelIpCountersTable.yml arista_eos_show_kernel_ip_counters.textfsm ];

		> Detals:
