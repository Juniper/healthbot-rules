# HealthBot Paloalto KPI rules and playbooks

## Paloalto playbooks

## Paloalto rules

### Rule name: check-paloalto-processes-cpu-memory-netconf 
		> Description: "Collects system process's cpu utilization periodically and notifies anomalies when daemon CPU usage exceed threshold"
		> Synopsis: "System processes cpu analyzer"
		> Rule file name: check-paloalto-processes-cpu-memory-netconf.rule


		> Helper files: [ paloalto_panos_show_system_resources.textfsm PaloaltoSysytemResource.yml];

		> Detals:
		 Detects PANOS processes (daemons) CPU and memory utilization threshold breaches and
		 notifies when anomalies are found.
		 Three inputs control detection
		
		   1) process-name-input, is a regular expression that matches the daemons that you
		      would like to monitor. By default it's '.*', which matches all daemons.
		      Use something like 'rpdbind|syslogd|authd' to match only rotuing, firewall and
		      interface daemons.
		
		   2) process-high-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 80% of daemon CPU and Memory utilization. This
		      rule will set a dashboard color to red when daemon CPU and Memory utilization
		      exceed high threshold 'process-high-threshold' for period of
		      3 minutes.
		
		   3) process-low-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 50% of daemon CPU and Memory utilization. This
		      rule will set a dashboard color to yellow when daemon CPU and Memory utilization
		      exceed low threshold 'process-low-threshold' for period of
		      3 minutes. Otherwise color is set to green.
### Rule name: check-paloalto-storage-netconf 
		> Description: "Collects filesystem storage usage periodically and notifies anomalies when used space exceed threshold"
		> Synopsis: "system storage usage analyzer"
		> Rule file name: check-paloalto-storage-netconf.rule


		> Helper files: [ paloalto_panos_show_system_disk-space.textfsm PaloaltoSysytemDiskspace.yml];

		> Detals:
		 Detects system storage utilization threshold breaches and notifies when
		 anomalies are found.
