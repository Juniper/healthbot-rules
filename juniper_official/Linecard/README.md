# HealthBot Linecard KPI rules and playbooks

## Linecard playbooks
### Playbook name: FPC-PFE-resource-monitoring-playbook 
		> Description: "Monitoring linecard resources - Heap memory, RTT delay, IFL denied count, Client session denied count, Service session denied count, IFL counter memory, Filter counter memory, Expansion memory, CoS queue utilizations, NH memory free, Firewall memory free and Encap memory free."
		> Synopsis: "Monitor FPC and PFE resources"
		> Playbook file name: FPC-PFE-resource-monitoring.playbook
		> Details:
		 Playbook contains multiple rules which monitor FPC and PFE resources and
		 notifies when anomalies are found.
		
		 1) Rule monitor-denied-count, monitors the IFL denied count,
		 2) Rule monitor-heap-memory, monitors the heap memory used and notifies
		 3) Rule monitor-round-trip-time, monitors Average RTT delay and notifies
		 4) Rule monitor-cos-queues-utilization, monitors the PFE CoS queue utilization and notifies
		 5) Rule monitor-counter-and-expansion-memory, monitors the PFE IFL counter memory used,
		 6) Rule monitor-firewall-nh-encap-memory, monitors free FW memory,
### Playbook name: linecard-kpis-playbook 
		> Description: "Playbook checks linecard health i.e. cpu, memory, PFE discards and CM errors"
		> Synopsis: "Linecards key performance indicators"
		> Playbook file name: linecard-kpis.playbook
		> Details:
		 Playbook contains multiple rules which monitor linecards and notifies when
		 anomalies are found.
		 1) Rule "check-fpc-cpu" detects the line cards cpu utilization threshold
		    breaches and notifies anomalies.
		 2) Rule "check-fpc-memory" detects the line cards memory usage threshold
		    breaches and notifies anomalies.
		 3) Rule "check-cm-events" detects the cm errors and notifies anomalies
		    when error count increases.
		 4) Rule "check-pfe-discards" detects the PFE discards and notifies anomalies
		    when discard count increases.
		 5) Rule "check-fabric-netconf", detects the fabric discoards and notifies
		    anomalies when drop count is high.
### Playbook name: online-fpc-playbook 
		> Description: "Playbook collects online FPCs list"
		> Synopsis: "Collects online FPCs"
		> Playbook file name: online-fpc.playbook
		> Details:
		 Playbook contains the rule which monitor online FPC
		 1) Rule "update-online-fpc" finds all the online FPCs in the chassis.

## Linecard rules

### Rule name: check-fabric-netconf 
		> Description: "To check for packet drops for source/destination FPC and PFE"
		> Synopsis: "Packet Drop KPI"
		> Rule file name: check-fabric-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1



		> More details:
### Rule name: check-pfe-discards 
		> Description: "Collects packet forwarding engine hardware discard statistics  and notifies when discard count increases"
		> Synopsis: "Packet forwarding engine hardware discard statistics analyzer"
		> Rule file name: check-pfe-discards.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.0.1
		> Supported product:MX, Platforms:, Junos:15.1R1



		> More details:
		 Detects PFE discards and notifies when anomalies are found.
		 One inputs control detection
		
		   1) discard-count, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the discards are greater than
		      'discard-count' for 75s. otherwise color is set to green.
### Rule name: check-cm-error-table 
		> Description: "This rule collects CM error statistics periodically and notifies in case of anomalies"
		> Synopsis: "CM error analyzer"
		> Rule file name: cm-error.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: cm-error.yml;
		> More details:
### Rule name: check-cm-events 
		> Description: "Collects CM errors and count periodically and notifies when error count increases"
		> Synopsis: "CM error analyzer"
		> Rule file name: cm-events.rule
		> Sensor type: native-gpb 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:MX240, Junos:17.2
		> Supported product:MX, Platforms:MX480, Junos:17.2
		> Supported product:MX, Platforms:MX960, Junos:17.2
		> Supported product:MX, Platforms:MX2010, Junos:17.2
		> Supported product:MX, Platforms:MX2020, Junos:17.2



		> More details:
		 Detects CM (chassis manager) errors on linecards and notifies when anomalies
		 are found.
		 One input control detection
		
		   1) "cm-error-threshold-variable" is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when any of the CM error count increases are greater than
		      'cm-error-threshold-variable' for 3m period. If it sees any CM error count
		      increase for a period of less than 3m, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: check-center-chip-fabric-in-errors 
		> Description: "Monitors the center chip cell fabric-in cell timeouts,crc error packets,late cells,error cells and malloc drops"
		> Synopsis: "Center chip cell statistics analyzer"
		> Rule file name: fi-error.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chip.yml;
		> More details:
### Rule name: check-center-chip-fabric-in 
		> Description: "Monitors the center chip fabric-in packets dropped ,error packets, received and sent packets"
		> Synopsis: "center chip fabric-in packets statistics analyzer"
		> Rule file name: fi-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chip.yml;
		> More details:
### Rule name: check-fpc-cpu-memory-usage-netconf 
		> Description: "Collects system FPC CPU statistics periodically and notifies anomalies when CPU utilization exceed threshold"
		> Synopsis: "FPC CPU analyzer"
		> Rule file name: fpc-cpu-memory-state-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:SRX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects linecards CPU utilization threshold breaches and notifies when
		 anomalies are found.
		
		   1) "buffer-usage-threshold" is the threshold that causes the rule to
		       report an anomaly. By default it's 80% of CPU utilization. This
		       rule will set a dashboard color to red when FPC CPU utilization
		       exceed high threshold
		   2) "cpu-usage-threshold" is the threshold that causes the rule to report
		      an anomaly. By default it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when FPC CPU utilization exceed high threshold
		   3) "heap-usage-threshold" is the threshold that causes the rule to report
		      an anomaly. By default it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when FPC CPU utilization exceed high threshold
### Rule name: check-fpc-cpu-memory-usage-srx-cluster-netconf 
		> Description: "Collects FPC CPU statistics periodically and notifies anomalies when CPU utilization exceed threshold"
		> Synopsis: "FPC CPU analyzer"
		> Rule file name: fpc-cpu-memory-state-srx-cluster-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:SRX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects linecards CPU utilization threshold breaches in SRX cluster device and notifies when
		 anomalies are found.
		 Three inputs control detection
		
		   1) "buffer-usage-threshold" is the threshold that causes the rule to report
		      an anomaly. By default, it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when FPC CPU utilization exceed high threshold
		
		   2) "cpu-usage-threshold" is the threshold that causes the rule to report
		      an anomaly. By default, it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when FPC CPU utilization exceed high threshold
		   3) "heap-usage-threshold" is the threshold that causes the rule to report
		      an anomaly. By default, it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when FPC CPU utilization exceed high threshold
### Rule name: check-fpc-cpu 
		> Description: "Collects system FPC CPU statistics periodically and notifies anomalies when CPU utilization exceed threshold"
		> Synopsis: "FPC CPU analyzer"
		> Rule file name: fpc-cpu-utilization.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1



		> More details:
		 Detects linecards CPU utilization threshold breaches and notifies when
		 anomalies are found.
		 Three inputs control detection
		
		   1) "fpc-slot-no" is a regular expression that matches the linecard
		      that you would like to monitor.  By default it's '0-20', which matches
		      FPC 0 to 20 linecards. Use something like '0-3' to match only specific
		      FPCs i.e. 0 to 3.
		
		   2) "fpc-cpu-high-threshold" is the threshold that causes the rule to report
		      an anomaly. By default it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when FPC CPU utilization exceed high threshold
		      'fpc-cpu-high-threshold' for a period of 3 minutes.
		
		   3) "fpc-cpu-low-threshold" is the threshold that causes the rule to report
		      an anomaly. By default it's 50% of CPU utilization. This rule will set
		      a dashboard color to yellow when RE CPU utilization exceed low
		      threshold 'fpc-cpu-low-threshold' for a period of 3 minutes.
		      Otherwise color is set to green.
### Rule name: check-fpc-memory 
		> Description: "Collects system FPC memory statistics periodically and notifies anomalies when heap and buffer utilization exceed threshold"
		> Synopsis: "FPC memory analyzer"
		> Rule file name: fpc-memory-utilization.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1



		> More details:
		 Detects linecards memory utilization threshold breaches and notifies when
		 anomalies are found.
		 Five inputs control detection
		
		   1) "fpc-slot-no" is a regular expression that matches the linecard
		      that you would like to monitor.  By default it's '0-20', which matches
		      FPC 0 to 20 linecards. Use something like '0-3' to match only specific
		      FPCs i.e. 0 to 3.
		
		   2) "fpc-buffer-high-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 80% of memory buffer utilization.
		      This rule will set a dashboard color to red when FPC memory buffer
		      utilization exceed high threshold 'fpc-buffer-high-threshold' for a
		      period of 3 minutes.
		
		   3) "fpc-buffer-low-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 50% of memory buffer utilization.
		      This rule will set a dashboard color to yellow when FPC memory buffer
		      utilization exceed low threshold 'fpc-buffer-low-threshold' for a
		      period of 3 minutes.
		   4) "fpc-heap-high-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 80% of memory heap utilization.
		      This rule will set a dashboard color to red when FPC memory heap
		      utilization exceed high threshold 'fpc-heap-high-threshold' for a
		      period of 3 minutes.
		
		   5) "fpc-heap-low-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 50% of memory heap utilization.
		      This rule will set a dashboard color to yellow when FPC memory heap
		      utilization exceed low threshold 'fpc-heap-low-threshold' for a
		      period of 3 minutes.
### Rule name: check-fpc-threads 
		> Description: "Monitors the CPU utilization by FPC threads"
		> Synopsis: "Linecard CPU usage analyzer"
		> Rule file name: fpc-threads.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: fpc-threads.yml;
		> More details:
### Rule name: check-fpc-utilization-information 
		> Description: "Monitors FPC buffer, heap and cpu utilization"
		> Synopsis: "Linecard FPC, heap and CPU analyzer"
		> Rule file name: fpc-utilization.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: fpc-utilization.yml;
		> More details:
### Rule name: check-center-chip-host-path 
		> Description: "Monitors the center chip hostpath drops"
		> Synopsis: "Center chip hostpath analyzer"
		> Rule file name: host-drops.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chip.yml;
		> More details:
### Rule name: check-host-loopback-status 
		> Description: "Monitors the host loopback to detected wedges, toolkit errors"
		> Synopsis: "Host loopback analyzer"
		> Rule file name: host-loopback-status.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: task-io.yml;
		> More details:
### Rule name: check-ithrottle-statistics 
		> Description: "Monitors throttle statistics such as adjacency ups and downs, starts and stops, disables and enables"
		> Synopsis: "Throttle statistics analyzer"
		> Rule file name: ithrottle-id.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: ithrottle.yml;
		> More details:
### Rule name: check-ithrottle 
		> Description: "Monitors interrupt throttle configuration, state and usage"
		> Synopsis: "iThrottle statistics analyzer"
		> Rule file name: ithrottle.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: ithrottle.yml;
		> More details:
### Rule name: check-jnh-exceptions 
		> Description: "Monitors the jnh exception packets"
		> Synopsis: "JNH packet drop analyzer"
		> Rule file name: jnh-exceptions.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: jnh-exceptions.yml;
		> More details:
### Rule name: check-jnh-interface-statistics 
		> Description: "Monitors the jnh ifd stream"
		> Synopsis: "JNH IFD stream kpi"
		> Rule file name: jnh-ifd-stream.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: jnh-ifd-stream.yml;
		> More details:
### Rule name: check-center-chip-lookup-in 
		> Description: "Monitors center chip lookup in interrupts counters"
		> Synopsis: "Center chip lookup analyzer"
		> Rule file name: li-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chip.yml;
		> More details:
### Rule name: check-linecard-ethernet-statistics 
		> Description: "This rule collects linecard ethernet statistics periodically and notifies in case of anomalies"
		> Synopsis: "Linecard ethernet statistics kpi"
		> Rule file name: linecard-ethernet-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: linecard-ethernet-statistics.yml;
		> More details:
### Rule name: check-center-chip-lookup-out 
		> Description: "This topic is to monitors and notify Center chip lookup out error"
		> Synopsis: "Center chip lookup analyzer"
		> Rule file name: lo-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chip.yml;
		> More details:
### Rule name: update-online-fpc 
		> Description:  "collects online fpc using udf and updates dependent rules sensor table"
		> Synopsis: "collects online fpc using udf and updates dependent rules sensor table"
		> Rule file name: online-fpc.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: online_fpc.yml;
		> More details:
		 These two rules are used to collect online FPCs in network device and update dependent yml files
### Rule name: check-pci-error-counters 
		> Description: "Monitors the PCI link status"
		> Synopsis: "PCI invalid status analyzer"
		> Rule file name: pci-error.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: pci-error.yml;
		> More details:
### Rule name: check-center-chip-pt-entries 
		> Description: "Monitors the center chip packet table wan & fabric entries"
		> Synopsis: "Center chip packet statistics analyzer"
		> Rule file name: pt-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chip.yml;
		> More details:
### Rule name: monitor-cos-queues-utilization 
		> Description: "Collects periodically CoS queues utilization for each PFE instance in all FPCs and reports whether it is normal or exceeded threshold "
		> Synopsis: "CoS queues analyser"
		> Rule file name: resource-monitor-cos-queue.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:MX80, Junos:15.1R1
		> Supported product:MX, Platforms:MX104, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1
		> Supported product:EX, Platforms:EX9200, Junos:16.1R1


		> Helper files: resource-monitor-cos-queue.yml;
		> More details:
		 This rule collects periodically CoS queues utilization for each PFE instance in all FPCs
		 and reports whether it is normal (green) or exceeded threshold (red).
		 CoS queue utilization value and the threshold value is available in o/p of CLI command
		 "show system resource-monitor summary"
### Rule name: monitor-counter-and-expansion-memory 
		> Description: "Collects periodically Filter counter memory, IFL counter memory and Expansion memory utilisation for each PFE instance in all FPCs and reports whether it is normal or exceeded threshold "
		> Synopsis: "Filter counter memory, IFL counter memory and expansion memory analyser"
		> Rule file name: resource-monitor-counter-expansion-mem.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:16.1R1
		> Supported product:MX, Platforms:MX80, Junos:15.1R1
		> Supported product:MX, Platforms:MX104, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1


		> Helper files: resource-monitor-counter-expansion-mem.yml;
		> More details:
		 This rule collects periodically Filter counter memory used, IFL counter memory used
		 and Expansion memory used for each PFE instance in all FPCs and reports whether it is
		 normal (green) or exceeded threshold (red).
		 Memory used values and the threshold values are available in o/p of CLI command
		 "show system resource-monitor summary"
		 This is combined rule for 3 rules:
		 resource-monitor-expansion-mem.rule
		 resource-monitor-ifl-counter-mem.rule
		 resource-monitor-filter-counter-mem.rule
### Rule name: monitor-denied-count 
		> Description: "Check client session denied count, service session denied count and IFL denied count for each FPC and reports whether denied count is zero, non-zero or increasing."
		> Synopsis: "Denied count analyser"
		> Rule file name: resource-monitor-denied-count.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:16.1R1
		> Supported product:MX, Platforms:MX80, Junos:15.1R1
		> Supported product:MX, Platforms:MX104, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1


		> Helper files: resource-monitor-denied-count.yml;
		> More details:
		 This rule chekcs periodically client session denied count, service session denied count
		 load based client session denied count, load based service session denied count,
		 and IFL denied count for each FPC and reports if denied count is zero (green)
		 non-zero (yellow) or increasing (red).
		 Denied count values are available in o/p of CLI command
		 "show system resource-monitor summary"
### Rule name: monitor-heap-memory 
		> Description: "Check heap memory utilization periodically for each FPC and reports whether it is normal or exceeded threshold"
		> Synopsis: "Heap memory analyser"
		> Rule file name: resource-monitor-heap-memory.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:16.1R1
		> Supported product:MX, Platforms:MX80, Junos:15.1R1
		> Supported product:MX, Platforms:MX104, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1


		> Helper files: resource-monitor-heap-mem.yml;
		> More details:
		 This rule collects periodically heap memory used for each FPC
		 and reports whether it is normal (green) or exceeded threshold (red).
		 Memory used values and the threshold values are available in o/p of CLI command
		 "show system resource-monitor summary"
### Rule name: monitor-firewall-nh-encap-memory 
		> Description: "Collects periodically Firewall memory, NH memory and Encap memory availability for each PFE instance in all FPCs and reports whether it is normal or below watermark"
		> Synopsis: " Firewall memory, NH memory and Encap memory analyser"
		> Rule file name: resource-monitor-nh-fw-encap-mem.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:16.1R1
		> Supported product:MX, Platforms:MX80, Junos:15.1R1
		> Supported product:MX, Platforms:MX104, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1


		> Helper files: resource-monitor-nh-fw-encap-mem.yml;
		> More details:
		 This rule collects periodically free NH memory used, free Firewall memory and
		 free Encapsulation memory for each PFE instance in all FPCs and reports whether it is
		 normal (green) or below watermark (red).
		
		 Memory used values and the watermark values are available in o/p of CLI command
		 "show system resource-monitor fpc"
		 Encapsulation memory is specific to I-chips and not applicable for Trio-based chips.
		 It is reported as green with value as 'NA' for Trio-based chips.
### Rule name: monitor-round-trip-time 
		> Description: "Check Round Trip Time dealy periodically for each FPC and reports whether it is normal or exceeded threshold"
		> Synopsis: "RTT analyser"
		> Rule file name: resource-monitor-rtt.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:16.1R1
		> Supported product:MX, Platforms:MX80, Junos:15.1R1
		> Supported product:MX, Platforms:MX104, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1


		> Helper files: resource-monitor-rtt.yml;
		> More details:
		 This rule collects periodically average round trip time delay for each FPC
		 and reports whether it is normal (green) or exceeded threshold (red).
		 RTT delay values and the threshold values are available in o/p of CLI command
		 "show system resource-monitor summary"
### Rule name: check-fpc-cpu-scheduler-info 
		> Description: "Monitors FPC CPU utilization"
		> Synopsis: "FPC CPU statistics analyzer"
		> Rule file name: scheduler-info.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: scheduler-info.yml;
		> More details:
### Rule name: check-traffic-offload-engine-status 
		> Description: "Monitors  TOE packets, Asic blocks, Wedge declaration, Wedge window size, Ucode, Hostpath app status"
		> Synopsis: "TOE packets analyzer"
		> Rule file name: toe-pfe.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: toe-pfe.yml;
		> More details:
### Rule name: update-online-fpc-chipset 
		> Description:  "collects online fpc using udf and updates dependent rules sensor table"
		> Synopsis: "collects online fpc using udf and updates dependent rules sensor table"
		> Rule file name: update-online-fpc-chipset.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: online_fpc_chipset.yml;
		> More details:
### Rule name: update-online-fpc-evpn 
		> Description:  "collects online fpc using udf and updates dependent rules sensor table"
		> Synopsis: "collects online fpc using udf and updates dependent rules sensor table"
		> Rule file name: update-online-fpc-evpn.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: online_fpc_evpn.yml;
		> More details:
### Rule name: update-online-fpc-ospf 
		> Description:  "collects online fpc using udf and updates dependent rules sensor table"
		> Synopsis: "collects online fpc using udf and updates dependent rules sensor table"
		> Rule file name: update-online-fpc-ospf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: online_fpc_ospf.yml;
		> More details:
### Rule name: check-center-chip-wan-out 
		> Description: "Monitors the center chip wan out transmitted packets"
		> Synopsis: "Center chip wan out statistics analyzer"
		> Rule file name: wo-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chip.yml;
		> More details:
