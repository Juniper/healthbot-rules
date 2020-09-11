# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN playbooks
### Playbook name: chassis-kpis-playbook 
		> Description: "Playbook monitor the chassis health i.e. chassis, RE, RE CPU and linecards temperatures, power and fan health"
		> Synopsis: "Chassis key performance indicators"
		> Playbook file name: chassis-kpis.playbook
		> Detals:
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
		> Detals:
		 Detects mismatched chassis network-services setting, will advise corrective action if detected
		 Rule netsvc-rule, calls netsvc.py to determine the state and advise action if required

## EVPN VXLAN rules

### Rule name: check-re-cpu-temperature 
		> Description: "Collects RE CPU temperature periodically and notifies anomaly when temperature exceed threshold"
		> Synopsis: "RE CPU temperature check"
		> Rule file name: re-cpu-temperature.rule

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
### Rule name: check-chassis-temperature 
		> Description: "Collects chassis temperature periodically and notifies anomalies when temperature exceed threshold"
		> Synopsis: "Chassis temperature check"
		> Rule file name: chassis-temperature.rule

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
### Rule name: check-zone-power-usage 
		> Description: "Collects chassis zone power usage periodically and notifies anomaly when power usage exceed threshold"
		> Synopsis: "Zone power check"
		> Rule file name: zone-power-usage.rule

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
		> Helper files: [ chassis-power.yml used-percentage.py ];
		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects chassis power zone usage threshold breaches and notifies when
		 anomalies are found.
		 One input control detection
		   1) "zone-power-usage-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 80% of zone power usage. This rule
		      will set a dashboard color to red when power usage exceed threshold
		      'zone-power-usage-threshold'. Otherwise color is set to green.
### Rule name: check-chassis-alarms 
		> Description: "Collects chassis stats and notify anomalies when alarms found"
		> Synopsis: "Chassis alarms detector"
		> Rule file name: chassis-alarms.rule




		> Detals:
		 Detects chassis alarms and notifies when anomalies are found.
		
### Rule name: check-issu-failure 
		> Description: "This rule detects ISSU failure and displays the ISSU stage when it failed"
		> Synopsis: "Detect ISSU failure"
		> Rule file name: check-issu-failure.rule




		> Detals:
		 ISSU (In-Service Software Upgrade) failure detection
		 If ISSU is triggered and it fails, this rule will detect the failure.
		 It will also report during which phase the ISSU failed (validation, slave upgrade etc.).
### Rule name: check-failover-configured 
		> Description: "Checks if other RE is present and if GRES/failover is configured or not"
		> Synopsis: "Check whether graceful-switchover is configured or not"
		> Rule file name: check-failover-configured.rule




		> Detals:
		 Checks if graceful-switchover is configured on a dual RE chassis or not
		 First checks if other routing engine is present or not. If present, checks
		 if failover (set chassis redundancy graceful-switchover) is configured or not.
		
		 In dual RE chassis, for high availability it is recommended to have faiover
		 configured. A yellow color is reported if this configuration is not found
		 in a dual Routing Engine chassis.
### Rule name: check-system-power-usage 
		> Description: "Collects PEM power usage periodically and notifies anomaly when power usage exceed threshold"
		> Synopsis: "Chassis system power check"
		> Rule file name: system-power-usage.rule

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
		> Helper files: system-virtual-memory.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-re-temperature 
		> Description: "Collects routing-engine (RE) temperature periodically and notifies anomaly when temperature exceed threshold"
		> Synopsis: "Routing-engine temperature check"
		> Rule file name: re-temperature.rule

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
### Rule name: netsvc-rule 


		> Rule file name: netsvc.rule

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
		> Helper files: netsvc.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-fan-health 
		> Description: "Collects chassis environment statistics periodically and notifies anomalies when fan status is NOK"
		> Synopsis: "Chassis fans health analyzer"
		> Rule file name: chassis-fan-health.rule

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
		> Helper files: chassis-fan.yml;
		> Supported healthbot version: 3.1.0
		> Detals:
		 Monitors chassis fan health status and notifies when anomalies are found.
### Rule name: report-gres-readiness 
		> Description: "Check whether Failover/GRES is configured and if slave RE is ready for a switchover"
		> Synopsis: "Check if slave RE is ready for failover"
		> Rule file name: report-gres-readiness.rule




		> Detals:
		 Check if slave RE is ready for failover
		 In dual routing engine chassis, if graceful-switchover is configured, the
		 slave routing engine syncs the FIB states from Master RE and declares itself
		 ready for failover event.
		 If for some reason, Slave does not become ready for failover for significant
		 amount of time, this rule will report it.
### Rule name: check-failover-init-error 
		> Description: "Check if Ksyncd (Junos Kernel State Synchronization daemon) has reported an initialization error"
		> Synopsis: "Check failover Initialization error"
		> Rule file name: check-failover-init-error.rule




		> Detals:
		 Check failover Initialization error
		 Checks if Ksyncd (Junos Kernel State Synchronization daemon) has reported an
		 initialization error or not.
		 Ksyncd cleans up the FIB states on replicated routing engine before it
		 starts to resync the FIB states from the Master routing engine. It is possible
		 for this cleanup to fail in certain scenarios. But, if these cleanup failures
		 are persistent and are seen for more than 30 minutes, it can comprise high
		 availability feature and should be reported.
		 Rebooting backup RE should help in recovery.
### Rule name: check-ksyncd-core 
		> Description: "Check if Ksyncd core files are present in /var/tmp on the other RE"
		> Synopsis: "Check presence of Ksyncd core files"
		> Rule file name: check-ksyncd-core.rule




		> Detals:
		 Check presence of Ksyncd core files
		 Checks if Ksyncd core files are present in /var/tmp on the other RE.
		
		 While replicating a FIB state, if Ksyncd (Kernel state synchronization daemon)
		 gets an error from the backup routing engine kernel, it generates a ksyncd core
		 and Kernel live vmcores for debugging.
		 This rule detects the presence of Ksyncd core(s) and reports a yellow alarm.
### Rule name: check-fpc-temperature 
		> Description: "Collects FPC temperature periodically and notifies anomaly when temperature exceed threshold"
		> Synopsis: "FPC temperature check"
		> Rule file name: fpc-temperature.rule

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
### Rule name: check-pem-power-usage 
		> Description: "Collects PEM power usage periodically and notifies anomaly when power usage exceed threshold"
		> Synopsis: "PEM power check"
		> Rule file name: pem-power-usage.rule

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
