# HealthBot IOS_XR KPI rules and playbooks

## IOS_XR playbooks

## IOS_XR rules

### Rule name: check-ios-xr-isis-neighbor-state-netconf 
		> Description: "Collects ISIS adjacency state periodically and notify anomaly when state is down"
		> Synopsis: "ISIS session state analyzer"
		> Rule file name: check-ios-xr-isis-neighbor-state-netconf.rule


		> Helper files: XRIsisNeighborsTable.yml;

		> Detals:
		 Detects ISIS adjacency state changes and notifies when anomalies are found.
### Rule name: check-ios-xr-processes-cpu-netconf 
		> Description: "Collects system process's cpu utilization periodically and notifies anomalies when daemon CPU usage exceed threshold"
		> Synopsis: "System processes cpu analyzer"
		> Rule file name: check-ios-xr-processes-cpu-netconf.rule


		> Helper files: [ XRCpuProcessesTable.yml cisco_xr_show_processes_cpu.textfsm ];

		> Detals:
		 Detects cisco IOS-XR processes(daemons) CPU utilization threshold breaches
		 and notifies when anomalies are found.
### Rule name: check-ios-xr-interface-state-netconf 
		> Description: "Collects interface statistics periodically and notifies when interface operator state is down"
		> Synopsis: "Interface state analyzer"
		> Rule file name: check-ios-xr-interface-state-netconf.rule


		> Helper files: XRInterfaceTable.yml;

		> Detals:
		 Monitors interface link state and notifies when anomalies are found.
		
