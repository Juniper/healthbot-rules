# HealthBot Chassis KPI rules and playbooks

## Chassis playbooks
### Playbook name: chassis-kpis-playbook 
		> Description: "Playbook monitor the chassis health i.e. chassis, RE, RE CPU and linecards temperatures, power and fan health"
		> Synopsis: "Chassis key performance indicators"
		> Playbook file name: chassis-kpis.playbook
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
		 5) Rule "check-system-power-usage" detects the system power usage threshold
		    breaches and notifies anomalies.
		 6) Rule "check-zone-power-usage" detects the zone power usage threshold
		    breaches and notifies anomalies.
		 7) Rule "check-pem-power-usage" detects the PEM power usage threshold
		    breaches and notifies anomalies.
		 8) Rule "check-fan-health" Monitors the fan state changes and notifies
		    anomalies.
		 9) Rule "check-chassis-alarms" detects chassis alarms
### Playbook name: netsvc-playbook 
		> Description: "Verifies network-services configuration versus service state and notify anomaly if there is a mismatch"
		> Synopsis: "Network services detector"
		> Playbook file name: netsvc.playbook
		> Details:
		 Detects mismatched chassis network-services setting, will advise corrective action if detected
		 Rule netsvc-rule, calls netsvc.py to determine the state and advise action if required

## Chassis rules

### Rule name: check-no-alarms 
		> Description: "Refers rule chassis.alarms/check-chassis-alarms and shows system as healthy if no active alarms"
		> Synopsis: "Chassis alarms detector"
		> Rule file name: chassis-alarms.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: Chassis-Alarms.yml;
		> More details:
		 Detects chassis alarms and notifies when anomalies are found.
		
### Rule name: check-fan-health 
		> Description: "Collects chassis environment statistics periodically and notifies anomalies when fan status is NOK"
		> Synopsis: "Chassis fans health analyzer"
		> Rule file name: chassis-fan-health.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chassis-fan.yml;
		> More details:
		 Monitors chassis fan health status and notifies when anomalies are found.
### Rule name: check-chassis-temperature 
		> Description: "Collects chassis temperature periodically and notifies anomalies when temperature exceed threshold"
		> Synopsis: "Chassis temperature check"
		> Rule file name: chassis-temperature.rule
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
		 Detects chassis temperature threshold breaches and notifies when anomalies
		 are found.
		 Two inputs control detection
		
		   1) "chassis-temperature-low-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 45 degree Cecilius of
		      chassis temperature. This rule will set a dashboard color to green
		      when temperature is below low threshold.
		
		   2) "chassis-temperature-high-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 55 degree Cecilius of
		      chassis temperature. This rule will set a dashboard color to yellow
		      when temperature is below high threshold. Otherwise color is set to
		      red and notify anomaly.
### Rule name: check-failover-configured 
		> Description: "Checks if other RE is present and if GRES/failover is configured or not"
		> Synopsis: "Check whether graceful-switchover is configured or not"
		> Rule file name: check-failover-configured.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1


		> Helper files: failover-info.yml;
		> More details:
		 Checks if graceful-switchover is configured on a dual RE chassis or not
		 First checks if other routing engine is present or not. If present, checks
		 if failover (set chassis redundancy graceful-switchover) is configured or not.
		
		 In dual RE chassis, for high availability it is recommended to have faiover
		 configured. A yellow color is reported if this configuration is not found
		 in a dual Routing Engine chassis.
### Rule name: check-failover-init-error 
		> Description: "Check if Ksyncd (Junos Kernel State Synchronization daemon) has reported an initialization error"
		> Synopsis: "Check failover Initialization error"
		> Rule file name: check-failover-init-error.rule
		> Sensor type: open-config 




		> More details:
		 Check failover Initialization error
		 Checks if Ksyncd (Junos Kernel State Synchronization daemon) has reported an
		 initialization error or not.
		 Ksyncd cleans up the FIB states on replicated routing engine before it
		 starts to resync the FIB states from the Master routing engine. It is possible
		 for this cleanup to fail in certain scenarios. But, if these cleanup failures
		 are persistent and are seen for more than 30 minutes, it can comprise high
		 availability feature and should be reported.
		 Rebooting backup RE should help in recovery.
### Rule name: check-issu-failure 
		> Description: "This rule detects ISSU failure and displays the ISSU stage when it failed"
		> Synopsis: "Detect ISSU failure"
		> Rule file name: check-issu-failure.rule
		> Sensor type: open-config 




		> More details:
		 ISSU (In-Service Software Upgrade) failure detection
		 If ISSU is triggered and it fails, this rule will detect the failure.
		 It will also report during which phase the ISSU failed (validation, slave upgrade etc.).
### Rule name: check-ksyncd-core 
		> Description: "Check if Ksyncd core files are present in /var/tmp on the other RE"
		> Synopsis: "Check presence of Ksyncd core files"
		> Rule file name: check-ksyncd-core.rule
		> Sensor type: iAgent 




		> More details:
		 Check presence of Ksyncd core files
		 Checks if Ksyncd core files are present in /var/tmp on the other RE.
		
		 While replicating a FIB state, if Ksyncd (Kernel state synchronization daemon)
		 gets an error from the backup routing engine kernel, it generates a ksyncd core
		 and Kernel live vmcores for debugging.
		 This rule detects the presence of Ksyncd core(s) and reports a yellow alarm.
### Rule name: check-lacp-statistics-openconfig 
		> Description: "Checks if LACP Tx and Rx packets are being sent"
		> Synopsis: "LACP statistics analyzer"
		> Rule file name: check-lacp-statistics-openconfig.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1

		> Other vendor product support: cisco-IOS-XR 

		> More details:
		 Monitors lacp link status and notifies when anomalies are found.
		 Four input control detection
		 1) lacp-threshold,  is the threshold that causes the rule to report
		 an anomaly. By default it is 1. This rule will set a
		 dashboard color to red when lacp tx and rx packets are not increasing by
		 lacp-threshold value during each cycle.
		 2) detached, is the threshold that causes the rule to report
		 an anomaly. By default it is 50.00 %. This rule will set a
		 dashboard color to yellow when file descriptor usage percent
		 exceeds threshold value in time range of 2 days. Otherwise
		 it is set to green.
		 3) interface-name, is a regular expression that matches the
		 interfaces that you would like to monitor. By default it '.*',
		 which matches all interfaces. Use something like 'ge.*' to
		 match only gigabit ethernet interfaces.
		 4) unknown-illegal-threshold,  is the threshold that causes the rule to report
		 an anomaly. By default it is 1. This rule will set a
		 dashboard color to red when illegal or unknown packets are increasing by
		 unknown-illegal-threshold value during range interval of 300s.
### Rule name: check-fpc-temperature 
		> Description: "Collects FPC temperature periodically and notifies anomaly when temperature exceed threshold"
		> Synopsis: "FPC temperature check"
		> Rule file name: fpc-temperature.rule
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
		 Detects FPC temperature threshold breaches and notifies when
		 anomalies are found.
		 Three inputs control detection
		   1) "fpc-slot-no" is a regular expression that matches the FPCs that you
		      would like to monitor.  By default it's '0-20', which matches 0 to 20
		      FPC slots. Use something like '0-3' to match only FPC slots 0 to 3.
		   2) "fpc-temperature-low-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 45 degree Cecilius of
		      FPC temperature. This rule will set a dashboard color to green
		      when temperature is below low threshold.
		
		   3) "fpc-temperature-high-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 55 degree Cecilius of FPC
		      temperature. This rule will set a dashboard color to yellow when
		      temperature is below high threshold. Otherwise color is set to
		      red and notify anomaly.
### Rule name: netsvc-rule 
		> Description: "Calls netsvc.py to determine the state and advise action if required"
		> Synopsis: "Check Network Services"
		> Rule file name: netsvc.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: netsvc.yml;
		> More details:
		 Detects mismatched chassis network-services setting, will advise corrective
		 action if detected.
### Rule name: check-pem-power-usage 
		> Description: "Collects PEM power usage periodically and notifies anomaly when power usage exceed threshold"
		> Synopsis: "PEM power check"
		> Rule file name: pem-power-usage.rule
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
		 Detects PEMs (Power Entry Modules) power usage threshold breaches and
		 notifies when anomalies are found.
		 Detects PEMs state changes and notifies when anomalies are found.
		 Detects PEMs temperature changes and notifies when anomalies are found.
		 Detects PEMs AC or DC input state changes and notifies when anomalies are found.
		 One input control detection
		   1) "pem-power-usage-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 80% of PEM power usage. This rule
		      will set a dashboard color to red when PEM power usage exceed
		      threshold 'pem-power-usage-threshold'. Otherwise color is set to green.
		   2) "power-input-type" is selects the input type as power-dc-input or
		      power-ac-input
### Rule name: check-re-cpu-temperature 
		> Description: "Collects RE CPU temperature periodically and notifies anomaly when temperature exceed threshold"
		> Synopsis: "RE CPU temperature check"
		> Rule file name: re-cpu-temperature.rule
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
		> Supported product:QFX, Platforms:QFX5200, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:18.3R1
		> Supported product:EX, Platforms:QFX5200, Junos:17.3R1
		> Supported product:EX, Platforms:QFX5200, Junos:18.3R1
		> Supported product:EX, Platforms:QFX5200, Junos:18.4R1



		> More details:
		 Detects routing-engine CPU temperature threshold breaches and notifies when
		 anomalies are found.
		 Three inputs control detection
		   1) "re-slot-no" is a regular expression that matches the routing engine
		      that you would like to monitor.  By default it's '0-1', which matches
		      both the routing engines. Use something like '0' to match only
		      routing engine 0.
		   2) "re-cpu-temperature-low-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 45 degree Cecilius of
		      RE CPU temperature. This rule will set a dashboard color to green
		      when temperature is below low threshold.
		
		   3) "re-cpu-temperature-high-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 55 degree Cecilius of RE
		      CPU temperature. This rule will set a dashboard color to yellow when
		      temperature is below high threshold. Otherwise color is set to
		      red and notify anomaly.
### Rule name: check-re-temperature 
		> Description: "Collects routing-engine (RE) temperature periodically and notifies anomaly when temperature exceed threshold"
		> Synopsis: "Routing-engine temperature check"
		> Rule file name: re-temperature.rule
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
		 Detects routing-engine temperature threshold breaches and notifies when
		 anomalies are found.
		 Three inputs control detection
		   1) "re-slot-no" is a regular expression that matches the routing engine
		      that you would like to monitor.  By default it's '0-1', which matches
		      both the routing engines. Use something like '0' to match only
		      routing engine 0.
		   2) "re-temperature-low-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 45 degree Cecilius of
		      RE temperature. This rule will set a dashboard color to green
		      when temperature is below low threshold.
		
		   3) "re-temperature-high-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 55 degree Cecilius of RE
		      temperature. This rule will set a dashboard color to yellow when
		      temperature is below high threshold. Otherwise color is set to
		      red and notify anomaly.
### Rule name: report-gres-readiness 
		> Description: "Check whether Failover/GRES is configured and if slave RE is ready for a switchover"
		> Synopsis: "Check if slave RE is ready for failover"
		> Rule file name: report-gres-readiness.rule
		> Sensor type: open-config 




		> More details:
		 Check if slave RE is ready for failover
		 In dual routing engine chassis, if graceful-switchover is configured, the
		 slave routing engine syncs the FIB states from Master RE and declares itself
		 ready for failover event.
		 If for some reason, Slave does not become ready for failover for significant
		 amount of time, this rule will report it.
### Rule name: check-system-power-usage 
		> Description: "Collects PEM power usage periodically and notifies anomaly when power usage exceed threshold"
		> Synopsis: "Chassis system power check"
		> Rule file name: system-power-usage.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Junos:16.1R1
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
		 Detects system power usage threshold breaches and notifies when  anomalies
		 are found.
		 One input control detection
		   1) "system-power-remaining-threshold" is the threshold that causes the
		      rule to report an anomaly. By default it's 20% of system remaining
		      power. This rule will set a dashboard color to red when system
		      remaining power is below threshold 'system-power-remaining-threshold'.
		      Otherwise color is set to green.
### Rule name: check-system-virtual-memory-information 
		> Description: "Monitors the virtual memory and interrupt rate"
		> Synopsis: "Virtual memory information analyzer"
		> Rule file name: system-virtual-memory.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: system-virtual-memory.yml;
		> More details:
		 Monitors the virtual memory and interrupt rate and notifies when
		 anomalies are found.
		 Two inputs control detection
		   1) "interrupt-rate-threshold-value" is System Interrupt Rate threshold value.
		      By default it's '500'.
		   2) "virtual-memory-threshold" is the Virtual Memory threshold value in bytes.
		      By default it's 1000000000.
		
### Rule name: check-zone-power-usage 
		> Description: "Collects chassis zone power usage periodically and notifies anomaly when power usage exceed threshold"
		> Synopsis: "Zone power check"
		> Rule file name: zone-power-usage.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: chassis-power.yml;
		> More details:
		 Detects chassis power zone usage threshold breaches and notifies when
		 anomalies are found.
		 One input control detection
		   1) "zone-power-usage-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 80% of zone power usage. This rule
		      will set a dashboard color to red when power usage exceed threshold
		      'zone-power-usage-threshold'. Otherwise color is set to green.
