# HealthBot System KPI rules and playbooks

## System playbooks
### Playbook name: system-kpis-playbook 
		> Description: "Playbook checks the system health i.e. system cpu, memory, storage and junos processes cpu and memory utilization"
		> Synopsis: "System key performance indicators"
		> Playbook file name: system-kpis.playbook
		> Detals:-
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
### Playbook name: vmhost-kpis-playbook 
		> Description: "Playbook checks the vmhost system health i.e. system cpu, memory, storage and junos processes cpu and memory utilization"
		> Synopsis: "VMHost system key performance indicators"
		> Playbook file name: vm-host-kpis.playbook
		> Detals:
		 Playbook contains multiple rules which checks the health of vmhost and
		 notifies when anomalies are found.
		
		 1) Rule check-vmhost-cpu-iagent, detects the vmhost cpu utilization threshold
		    breaches and notifies anomalies.
		 2) Rule check-vmhost-management-interface-iagent, detects the management
		    interface state changes and notifies when anomalies are found.
		 3) Rule check-vmhost-memory-iagent, detects the vmhost memory utilization
		    threshold breaches and notifies anomalies.
		 4) Rule check-vmhost-resource-iagent, Collects VMhost resource status
		    periodically and notifies anomalies.
		 5) Rule check-vmhost-status-iagent, Collects VMhost status periodically
		    and notifies anomalies
		 6) Rule check-vmhost-storage-iagent, detects the vmhost storage usage of
		     **all** mounts threshold breaches and notifies anomalies.

## System rules

### Rule name: check-vmcores 


		> Rule file name: check-vmcores.rule




		> Detals:
		 This rule detects presence of vmcore (Kernel crash) file(s) on the device.
		 If vmcore is detected, this rule raises a yellow alarm. It will continue
		 to report yellow alarm till the vmcore is moved from /var/crash into
		 some other location or some other device.
### Rule name: check-vmhost-cpu-iagent 
		> Description: "Collects VMhost  CPU statistics periodically and notifies anomalies when CPU utilization exceeds threshold"
		> Synopsis: "VMhost CPU analyzer"
		> Rule file name: vmhost-cpu-iagent.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [MX240 MX480 MX960 MX2010 MX2020];
			> Supported platforms: [PTX500 PTX1000 PTX5000 PTX10000];
			> Supported platforms: [QFX10002 QFX10008 QFX10016];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Detects VMhost cpu utilization and notifies when anomalies are found.
		 Two input control detection
		 1) cpu-name-variable, is a regular expression that matches the cpu that you
		  would like to monitor.  By default it's '.*', which matches all cpu's.
		
		 2) cpu-threshold-variable, is the threshold that causes the rule to report an
		  anomaly. By default it's 80. This rule will set a dashboard color to red
		  when *all* the cpu-utilisation-increases are greater than
		  'cpu-threshold-variable' for 5 mins or more. If it sees any cpu-utilisation
		  increase by more than threshold-variable, it'll turn the color to yellow,
		  else color is set to green.
		
### Rule name: check-system-statistics-ip 
		> Description: "Monitors incoming ip no socket buffer drops"
		> Synopsis: "Incoming raw ip packets analyzer"
		> Rule file name: system-statistics-ip.rule

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
		> Helper files: system-statistics-ip.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: fpc-memory 
		> Description: "Monitors FPC memory usage percentage and notifies anomalies"
		> Synopsis: "FPC memory analyzer"
		> Rule file name: fpc-memory.rule

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
		> Helper files: fpc_memory.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-vmhost-storage-iagent 
		> Description: "Collects VMhost  storage status periodically and notifies anomaly"
		> Synopsis: "VMhost Storage Analyzer"
		> Rule file name: vmhost-storage-iagent.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [MX240 MX480 MX960 MX2010 MX2020];
			> Supported platforms: [PTX500 PTX1000 PTX5000 PTX10000];
			> Supported platforms: [QFX10002 QFX10008 QFX10016];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Detects VMhost storage utilization and notifies when anomalies are found.
		 One input control detection
		
		 1) storage-threshold-variable, is the threshold that causes the rule to report
		 an anomaly.By default it's 80. This rule will set a dashboard color to red
		 when *all* the storage-utilisation-increases are greater than
		 'storage-threshold-variable' for 5 mins or more. If it sees any
		 storage-utilisation increase more than threshold-variable it'll turn the
		 color to yellow,else color is set to green.
		
### Rule name: check-version 
		> Description: "Validates the product name and Junos version"
		> Synopsis: "System product name and software version analyzer"
		> Rule file name: software-version.rule

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
		> Helper files: software-version.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-system-output-queues 
		> Description: "Monitors packet drops on the output interface"
		> Synopsis: "Packet drops on the output interface analyzer"
		> Rule file name: system-queues.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 
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
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: system-queues.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-pfe-traffic-statistics 
		> Description: "Monitors PFE traffic statistics such as fabric drops, host path hardware drops, info cell discards, OSPF hello counts"
		> Synopsis: "Linecard drops, discards and ospf hello analyzer"
		> Rule file name: pfe-traffic-statistics.rule

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
		> Helper files: pfe-traffic-statistics.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-system-process-memory 


		> Rule file name: system-proc-ext.rule

		> Supported products: ACX 
		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: sys-proc-ext.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-system-cpu 
		> Description: "Collects system RE CPU statistics periodically and notifies anomalies when CPU utilization exceeds threshold"
		> Synopsis: "Routing engine CPU analyzer"
		> Rule file name: system-cpu.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;
			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
		> Helper files: system-sensors.py;

		> Detals:
		 Detects RE CPU utilization threshold breaches and notifies when anomalies
		 are found.
		 Three inputs control detection
		
		   1) re-slot-no, is a regular expression that matches the routing engine
		      that you would like to monitor.  By default it's '0-1', which matches
		      both the routing engines. Use something like '0' to match only
		      routing engine 0.
		
		   2) re-cpu-high-threshold, is the threshold that causes the rule to report
		      an anomaly. By default it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when RE CPU utilization exceeds high threshold
		      're-cpu-high-threshold' for a period of 5 minutes.
		
		   3) re-cpu-low-threshold, is the threshold that causes the rule to report
		      an anomaly. By default it's 50% of CPU utilization. This rule will set
		      a dashboard color to yellow when RE CPU utilization exceeds low
		      threshold 're-cpu-low-threshold' for a period of 5 minutes.
		      Otherwise color is set to green.
### Rule name: check-storage 
		> Description: "Collects filesystem storage usage periodically and notifies anomalies when used space exceed threshold"
		> Synopsis: "system storage usage analyzer"
		> Rule file name: system-storage.rule

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
### Rule name: check-process-memory 
		> Description: "Collects system process's memory utilization periodically and notifies anomalies when daemon memory usage exceed threshold"
		> Synopsis: "System processes memory utilization analyzer"
		> Rule file name: system-processes-memory.rule

		> Supported products: ACX 
		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: [ generic_functions.py system-proc-ext.yml system-processes.py ];
		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects junos processes (daemons) memory utilization threshold breaches and
		 notifies when anomalies are found.
		 Three inputs control detection
		   1) process-name-input, is a regular expression that matches the daemons that you
		      would like to monitor. By default it's '.*', which matches all daemons.
		      Use something like 'rpd|dfwd|dcd' to match only routing, firewall and
		      interface daemons.
		   2) process-memory-high-threshold, is the threshold that causes the rule
		      to report an anomaly. By default it's 80% of daemon memory utilization.
		      This rule will set a dashboard color to red when daemon memory
		      utilization exceed high threshold 'process-memory-high-threshold'
		      for a period of 5 minutes.
		   3) process-memory-low-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 50% of daemon memory utilization.
		      This rule will set a dashboard color to red when daemon memory
		      utilization exceed low threshold 'process-memory-low-threshold'
		      for a period of 5 minutes. Otherwise color is set to green.
### Rule name: check-system-storage-capacity 
		> Description: "Monitors the system storage capacity"
		> Synopsis: "System storage capacity analyzer"
		> Rule file name: system-storage-capacity.rule

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
		> Helper files: system-storage-capacity.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-system-cpu-memory-snmp 
		> Description: "Collects CPU, Memory Utilization details from Routing Engines and notify anomalies based on threshold values "
		> Synopsis: "System CPU, Memory Utilization change detector"
		> Rule file name: system-cpu-memory-snmp.rule

		> Supported products: MX 
		> Supported products: SRX 

			> Supported platforms: ALL;
			> Supported platforms: All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects System CPU & memory utilization and notifies when anomalies are found.
		 One input control detection
		
		   1) Threshold, is the threshold value for CPU and memory utilization takes
		   as input and pass to the rule to report an anomaly. By default value is 80
### Rule name: check-routing-engine-cpu-utilization 
		> Description: "Monitors the routing engine's cpu utilization"
		> Synopsis: "Routing Engine CPU utilization analyzer"
		> Rule file name: re-cpu-utilization.rule

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
		> Helper files: re-cpu-utilization.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-pre-classifier-dropped-packets 
		> Description: "Monitors the rate of increase of packets dropped by the pre-classifier"
		> Synopsis: "Pre-classifier packer drop analyzer"
		> Rule file name: pre-classifier.rule

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
		> Helper files: pre-classifier.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-vmhost-memory-iagent 


		> Rule file name: vmhost-memory-monitoring.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [MX240 MX480 MX960 MX2010 MX2020];
			> Supported platforms: [PTX500 PTX1000 PTX5000 PTX10000];
			> Supported platforms: [QFX10002 QFX10008 QFX10016];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Detects VMhost memory utilization and notifies when anomalies are found.
		 One input control detection
		
		 1) memory-threshold-variable, is the threshold that causes the rule to report
		   an anomaly.By default it's 80. This rule will set a dashboard color to red
		   when *all* the memory-utilisation-increases are greater than
		   'memory-threshold-variable' for 5 mins or more. If it sees any
		   memory-utilisation increase by more than threshold, it'll turn the color
		   to yellow,else the color is set to green.
		
### Rule name: check-process-cpu 
		> Description: "Collects system process's cpu utilization periodically and notifies anomalies when daemon CPU usage exceed threshold"
		> Synopsis: "System processes cpu analyzer"
		> Rule file name: system-processes-cpu.rule

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
		> Helper files: system-proc-ext.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects Junos processes (daemons) CPU utilization threshold breaches and
		 notifies when anomalies are found.
		 Three inputs control detection
		
		   1) process-name-input, is a regular expression that matches the daemons that you
		      would like to monitor. By default it's '.*', which matches all daemons.
		      Use something like 'rpd|dfwd|dcd' to match only rotuing, firewall and
		      interface daemons.
		
		   2) process-cpu-high-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 80% of daemon CPU utilization. This
		      rule will set a dashboard color to red when daemon CPU utilization
		      exceed high threshold 'process-cpu-high-threshold' for period of
		      3 minutes.
		
		   3) process-cpu-low-threshold, is the threshold that causes the rule to
		      report an anomaly. By default it's 50% of daemon CPU utilization. This
		      rule will set a dashboard color to yellow when daemon CPU utilization
		      exceed low threshold 'process-cpu-low-threshold' for period of
		      3 minutes. Otherwise color is set to green.
### Rule name: check-vmhost-status-iagent 
		> Description: "Collects VMhost  status periodically and notifies anomalies "
		> Synopsis: "VMhost status analyzer"
		> Rule file name: vmhost-status-iagent.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [MX240 MX480 MX960 MX2010 MX2020];
			> Supported platforms: [PTX500 PTX1000 PTX5000 PTX10000];
			> Supported platforms: [QFX10002 QFX10008 QFX10016];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Detects VMhost status and notifies when anomalies are found.
### Rule name: check-vmhost-management-interface-iagent 
		> Description: "Collects VMhost  Management interface status periodically and notifies anomaly"
		> Synopsis: "VM Host Management interface analyzer"
		> Rule file name: vmhost-mgmt-interface-status-iagent.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [MX240 MX480 MX960 MX2010 MX2020];
			> Supported platforms: [PTX500 PTX1000 PTX5000 PTX10000];
			> Supported platforms: [QFX10002 QFX10008 QFX10016];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Detects management interface state changes and notifies when anomalies are found.
### Rule name: check-system-cpu-load-average 
		> Description: "Collects RE CPU load average data periodically and notifies anomalies when CPU utilization exceed threshold"
		> Synopsis: "RE CPU load average analyzer"
		> Rule file name: system-cpu-load-average.rule

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
		> Helper files: [ system-cpu.yml system-sensors.py ];
		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects RE CPU load average utilization(1min/5min/15min) threshold breaches
		 and notifies when anomalies are found.
		 Two inputs control detection for each 1,5 & 15 minutes CPU load average
		 utilization KPIs.
		   1) re-cpu-15min-low-threshold or re-cpu-1min-low-threshold
		      or re-cpu-5min-low-threshold, is the threshold will set a dashboard
		      color to green when RE CPU utilization below low threshold.
		   2) re-cpu-15min-high-threshold or re-cpu-1min-high-threshold
		      or re-cpu-5min-high-threshold, is the threshold that causes the rule
		      to report an anomaly. This rule will set a dashboard color to yellow
		      when RE CPU utilization below high threshold. Otherwise color is set
		      to red.
### Rule name: check-system-memory 
		> Description: "Collects REs' system memory statistics periodically and notifies anomaly when memory usage exceed threshold"
		> Synopsis: "RE system memory statistics analyzer"
		> Rule file name: system-memory.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;
			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;


		> Detals:
		 Detects RE memory buffer utilization threshold breaches and notifies when
		 anomalies are found.
		 Three inputs control detection
		
		   1) re_slot_No, is a regular expression that matches the routing engine
		      that you would like to monitor.  By default it's '0-1', which matches
		      both the routing engines. Use something like '0' to match only
		      routing engine 0.
		
		   2) memory-buffer-re-high-threshold, is the threshold that causes the rule
		      to report an anomaly. By default it's 75% of memory utilization.
		      This rule will set a dashboard color to red when RE memory buffer
		      utilization exceed high threshold'memory-buffer-re-high-threshold'
		      for a period of 5 minutes.
		
		   3)  memory-buffer-re-low-threshold, is the threshold that causes the rule
		      to report an anomaly. By default it's 50% of memory utilization.
		      This rule will set a dashboard color to red when RE memory buffer
		      utilization exceed high threshold'memory-buffer-re-low-threshold'
		      for a period of 5 minutes. Otherwise color is set to green.
### Rule name: check-vmhost-resource-iagent 
		> Description: "Collects vmhost resource status periodically and notifies anomaly"
		> Synopsis: "VM Host Resource analyzer"
		> Rule file name: vmhost-resource-status-iagent.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [MX240 MX480 MX960 MX2010 MX2020];
			> Supported platforms: [PTX500 PTX1000 PTX5000 PTX10000];
			> Supported platforms: [QFX10002 QFX10008 QFX10016];

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors VMhost resource status and notifies when anomalies are found.
