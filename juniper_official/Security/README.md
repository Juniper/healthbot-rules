# HealthBot Security KPI rules and playbooks

## Security playbooks
### Playbook name: ddos-playbook 
		> Description: "To check if  ddos protection packets dropped are increasing for global packet violations,routing engine and linecard"
		> Synopsis: "ddos protection"
		> Playbook file name: ddos-playbook.playbook
		> Details:
		 Playbook contains ddos rules which checks if ipv4/ipv6 addresses are
		 present on lo0,checks for ipv6 link local address, queue depth and lacp packets
		 and notifies when anomalies are found.
		 1) Rule "check-global-ddos-statistics" checks for ddos protection different
		    types of global packet violations.
		 2) Rule "check-protcol-ddos-statistics" checks for ddos protection system packets
		    dropped at the protcol level.
		 3) Rule "check-protcol-ddos-system-statistics" checks for ddos protection packets
		    dropped for routing engine and line card.
### Playbook name: security-kpis-playbook 
		> Description: "This playbook monitors variexec, secure boot and dev keys periodically and notifies anomalies" 
		> Synopsis: "Junos security checker"
		> Playbook file name: security-kpis-playbook.playbook
		> Details:
		 Playbook contains multiple rules which checks the secure parameters fo junos
		  and notifies when anomalies are found.
		 1) Rule check-veriexec-status-iagent, monitor status of veriexec on the
		    network device
		 2) Rule get-dev-key-status, determines if development keys have been revoked
		
		 3) Rule heck-secureboot-status, checks that secure boot is running and enforced

## Security rules

### Rule name: check-no-alarms 
		> Description: "Refers rule system.alarm/check-alarm-status-netconf and shows system as healthy if no active alarms"
		> Synopsis: "Chassis alarms detector"
		> Rule file name: check-alarm-status-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.1


		> Helper files: [ SystemAlarmStatus.yml SystemAlarmStatusHA.yml SystemAlarmStatusSA.yml ];
		> More details:
		 Detects system security alarms and notifies
		 One input control detection.
		
		 1) "input-alarm-description" is used to filter the based on the alarm
		    description
### Rule name: check-appid-asc-cache-status-netconf 
		> Description: "To check the status of application system cache on SRX cluster"
		> Synopsis: "Check for application system cache status"
		> Rule file name: check-appid-asc-cache-status-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.1
		> Supported product:SRX, Platforms:A, Junos:15.1R1


		> Helper files: [ Security_APPID_ASC_Status.yml Security_APPID_ASC_Status_HA.yml Security_APPID_ASC_Status_SA.yml ];
		> More details:
		 Monitors application system cache and notifies anomalies
		
### Rule name: check-cpu-memory-utilization-netconf 
		> Description: "SPU cpu and memory utilization of SRX cluster"
		> Synopsis: "SPU cpu and memory analyzer"
		> Rule file name: check-cpu-memory-utilization-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.1
		> Supported product:SRX, Platforms:All-standalone-and-cluster-mode, Junos:15.1R1


		> Helper files: [ SecurityCPUMemoryUtilization.yml SecurityCPUMemoryUtilizationMidrangeHA.yml SecurityCPUMemoryUtilizationHighendHA.yml SecurityCPUMemoryUtilizationSA.yml SecurityCPUMemoryUtilizationHighendSA.yml ];
		> More details:
		 Monitors SPU's CPU and memory and notifies anomalies when CPU and memory
		 utilization exceeds threshold.
		 Two input control detection.
		
		  1) "max-threshold" variable, is the threshold that causes the rule to report
		  an anomaly.By default it's 80. This rule will set a dashboard color to red
		  when *all* the memory or cpu utilisation are greater than
		  'max-threshold'.
		  2) "min-threshold" variable, is the threshold that causes the rule to report
		   an anomaly.By default it's 60. This rule will set a dashboard color to yellow
		   when *all* the memory or cpu utilisation are greater than
		   'min-threshold'.If it is less than min-threshold it is set to green.
		
### Rule name: check-global-ddos-statistics 
		> Description: "Monitors global related distributed denial of service statistics"

		> Rule file name: check-global-ddos-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
### Rule name: check-idp-memory-counter-netconf 
		> Description: "Check idp memory counters of SRX cluster"
		> Synopsis: "IDP memory counters analyzer"
		> Rule file name: check-idp-memory-counter-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.1
		> Supported product:SRX, Platforms:All-standalone-and-cluster-mode, Junos:15.1R1


		> Helper files: [ SecurityIDPCountersMemory.yml SecurityIDPCountersMemoryHA.yml SecurityIDPCountersMemorySA.yml ];
		> More details:
		 Monitors idp memory counters and notifies anomalies when error count
		 increases.
### Rule name: check-idp-memory-utilization-netconf 
		> Description: "Used for to check the memory utilization of IDP data plane"
		> Synopsis: "IDP data plane memory utilization"
		> Rule file name: check-idp-memory-utilization-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.1
		> Supported product:SRX, Platforms:All-standalone-and-cluster-mode, Junos:15.1R1


		> Helper files: [ SecurityIdpMemoryUsage.yml SecurityIdpMemoryUsageHighendSA.yml SecurityIdpMemoryUsageMidrangeSA.yml SecurityIdpMemoryUsageHighendHA.yml SecurityIdpMemoryUsageMidrangeHA.yml ];
		> More details:
		 Monitors IDP memory and notifies anomalies when memory utilization exceeds
		 threshold.
		 Two input control detection.
		
		  1) "max-threshold" variable, is the threshold that causes the rule to report
		  an anomaly.By default it's 80. This rule will set a dashboard color to red
		  when *all* the idp-data plane memory utilisation are greater than
		  'max-threshold'.
		   2) "min-threshold" variable, is the threshold that causes the rule to report
		   an anomaly.By default it's 60.This rule will set a dashboard color to
		   yellow when *all* the idp-data plane memory utilisation are greater than
		   'min-threshold'.If it is less than min-threshold it is set to green.
		
### Rule name: check-protcol-ddos-statistics 
		> Description: "Monitors protocol related distributed denial of service statistics"

		> Rule file name: check-protcol-ddos-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
### Rule name: check-protcol-ddos-system-statistics 
		> Description: "Monitors protcol related distributed denial of service statistics"

		> Rule file name: check-protcol-ddos-system-statistics.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
### Rule name: check-veriexec-status-iagent 


		> Rule file name: check-veriexec-status-iagent.rule
		> Sensor type: iAgent 




		> More details:
		 This rule detects the status of veriexec in the system and detects the
		 anomalies based on if veriexec is loaded and enforced or not.
		 It's recommended to have always veriexec enabled and loaded.
### Rule name: check-veriexec-status 

		> Synopsis: "Checks for the veriexec status via OC sensor"
		> Rule file name: check-veriexec-status.rule
		> Sensor type: open-config 




		> More details:
		 This rule detects the status of veriexec in the system and detects the
		 anomalies based on if veriexec is loaded and enforced or not.
		 IMPORTANT: If telemetry is being done in plain text, veriexec state will
		 be visible over the network and can be a security risk. Hence prefer the
		 iagent rule below, unless the telemetry channel is secured.
### Rule name: get-dev-key-status 
		> Description: "Determines if development keys have been revoked"
		> Synopsis: "State of development keys"
		> Rule file name: get-dev-key-state.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:19.3R1
		> Supported product:PTX, Platforms:A, Junos:19.3R1
		> Supported product:QFX, Platforms:A, Junos:19.3R1
		> Supported product:NFX, Platforms:A, Junos:19.3R1
		> Supported product:SRX, Platforms:A, Junos:19.3R1



		> More details:
		 This rule checks if development keys have been left on the system.
		
		 If development keys were present, this rule will report the results
		 of the attempted revocation as Successful or a Failure.
		 This rule relies on a file present in 19.3R1 and further.
### Rule name: check-secureboot-status 
		> Description: "Checks that secure boot is running and enforced"
		> Synopsis: "System secure boot status"
		> Rule file name: secure-boot-status.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX4650-48Y, Junos:19.3R1
		> Supported product:EX, Platforms:EX9251, Junos:19.3R1
		> Supported product:EX, Platforms:EX9253, Junos:19.3R1
		> Supported product:MX, Platforms:MX10003, Junos:19.3R1
		> Supported product:MX, Platforms:MX10008, Junos:19.3R1
		> Supported product:MX, Platforms:MX2008, Junos:19.3R1
		> Supported product:MX, Platforms:MX204, Junos:19.3R1
		> Supported product:MX, Platforms:MX960, Junos:19.3R1
		> Supported product:MX, Platforms:MX2010, Junos:19.3R1
		> Supported product:MX, Platforms:MX2020, Junos:19.3R1
		> Supported product:MX, Platforms:MX240, Junos:19.3R1
		> Supported product:MX, Platforms:MX480, Junos:19.3R1
		> Supported product:NFX, Platforms:NFX250, Junos:19.3R1
		> Supported product:PTX, Platforms:PTX10008, Junos:19.3R1
		> Supported product:PTX, Platforms:PTX10016, Junos:19.3R1
		> Supported product:PTX, Platforms:PTX3000, Junos:19.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:19.3R1
		> Supported product:QFX, Platforms:QFX10002-60C, Junos:19.3R1
		> Supported product:QFX, Platforms:QFX10008, Junos:19.3R1
		> Supported product:QFX, Platforms:QFX10016, Junos:19.3R1
		> Supported product:QFX, Platforms:QFX5110, Junos:19.3R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:19.3R1
		> Supported product:SRX, Platforms:SRX1500, Junos:19.3R1
		> Supported product:SRX, Platforms:SRX4600, Junos:19.3R1



		> More details:
		 This rule checks if secure boot is running and enforced and returns
		 an error if it is not.
		 This rule relies on a file present in 19.3R1 and beyond.
		 This rule is only applicible to devices where secure boot is capable.
		 If this rule is run on a device that is incapable of secure boot,
		 the result will be "secureboot status is unknonw" and the rule should be
		 removed.
### Rule name: check-spu-performance-srx-cluster-netconf 
		> Description: "Collects SPU performance for each PIC and notifies in case of stats are above threshold"
		> Synopsis: "FPC SPU performance analyzer"
		> Rule file name: srx-cluster-performance-spu-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:SRX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects linecards SPU utilization percentage in SRX cluster device and notifies when
		 anomalies are found.
		
		   1) "spu-cpu-threshold" is the threshold that causes the rule to report
		      an anomaly. By default, it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when SPU utilization exceed high threshold
		
### Rule name: check-flow-session-summary-netconf 
		> Description: "Monitors and notify flow session details"
		> Synopsis: "Flow session summary statistics analyzer"
		> Rule file name: srx-flow-session-summary-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:SRX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects flow session details for each PIC and notifies when anomalies are found.
		
		   1) "active-sessions-threshold-value" is the threshold that causes the rule
		      to report an anomaly. By default, it's 50000000. This rule will set a
		      dashboard color to red when active sessions for a PIC slot is greater
		      than this value.
		   2) "max-sessions-threshold-value" is the threshold that causes the rule
		      to report an anomaly. By default, it's 80000000. This rule will set a
		      dashboard color to red when active sessions for a PIC slot is greater
		      than this value.
### Rule name: check-spu-performance-netconf 
		> Description: "Collects SPU performance for each PIC and notifies in case of stats are above threshold"
		> Synopsis: "FPC SPU performance analyzer"
		> Rule file name: srx-performance-spu-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:SRX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects linecards SPU utilization percentage and notifies when
		 anomalies are found.
		
		   1) "spu-cpu-threshold" is the threshold that causes the rule to report
		      an anomaly. By default, it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when SPU utilization exceed high threshold
		
