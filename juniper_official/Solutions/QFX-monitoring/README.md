# HealthBot QFX-monitoring KPI rules and playbooks

## QFX-monitoring playbooks
### Playbook name: qfx-chassis-kpis 
		> Description: "Playbook monitor the chassis health i.e. chassis, RE, RE CPU and linecards temperatures and fan health"
		> Synopsis: "Chassis key performance indicators"
		> Playbook file name: qfx-chassis-kpis.playbook
		> Details:
		 Playbook contains multiple rules which checks the health of chassis and
		 notifies when anomalies are found.
		 1) Rule "check-chassis-temperature" detects the chassis temperature
		    threshold breaches and notifies anomalies.
		 2) Rule "check-re-temperature" detects the RE temperature threshold breaches
		    and notifies anomalies.
		 3) Rule "check-re-cpu-temperature" detects the RE CPU temperature threshold
		    breaches and notifies anomalies.
		 4) Rule "check-fpc-temperature" detects the FPC temperature threshold
		    breaches and notifies anomalies.
		 5) Rule "check-fan-health" Monitors the fan state changes and notifies
		    anomalies.
		 6) Rule "check-chassis-alarms" detects chassis alarms
### Playbook name: qfx-linecard-kpis 
		> Description: "Playbook checks linecard health i.e. cpu, memory, PFE discards and CM errors"
		> Synopsis: "Linecards key performance indicators"
		> Playbook file name: qfx-linecard-kpis.playbook
		> Details:
		 Playbook contains multiple rules which monitor linecards and notifies when
		 anomalies are found.
		 1) Rule "check-fpc-cpu" detects the line cards cpu utilization threshold
		    breaches and notifies anomalies.
		 2) Rule "check-fpc-memory" detects the line cards memory usage threshold
		    breaches and notifies anomalies.
### Playbook name: qfx-system-kpis 
		> Description: "Playbook checks the system health i.e. system cpu, memory, storage and junos processes cpu and memory utilization"
		> Synopsis: "System key performance indicators"
		> Playbook file name: qfx-system-kpis.playbook
		> Details:
		 Playbook contains multiple rules which checks the health of system and
		 notifies when anomalies are found.
		
		 1) Rule check-system-cpu, detects the system cpu utilization threshold
		    breaches and notifies anomalies.
		 2) Rule check-system-cpu-load-average, detects the system cpu load average
		    (1min/5min/15min) utilization threshold breaches and notifies anomalies.
		 3) Rule check-system-memory, detects the system memory utilization threshold
		    breaches and notifies anomalies.
		 4) Rule check-process-cpu, detects the system **all** daemon cpu utilization
		    threshold breaches and notifies anomalies.
		 5) Rule check-process-memory, detects the system **all** daemon memory
		    utilization threshold breaches and notifies anomalies.
		 6) Rule check-system-storage, detects the system storage usage of **all
		    mounts threshold breaches and notifies anomalies.

## QFX-monitoring rules

