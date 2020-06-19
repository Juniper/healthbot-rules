# HealthBot Security KPI rules and playbooks

## Security playbooks
### Playbook name: security-kpis-playbook 
		> Description: "This playbook monitors variexec, secure boot and dev keys periodically and notifies anomalies" 
		> Synopsis: "Junos security checker"
		> Playbook file name: security-kpis-playbook.playbook
		> Detals:
		 Playbook contains multiple rules which checks the secure parameters fo junos
		  and notifies when anomalies are found.
		 1) Rule check-veriexec-status-iagent, monitor status of veriexec on the
		    network device
		 2) Rule get-dev-key-status, determines if development keys have been revoked
		
		 3) Rule heck-secureboot-status, checks that secure boot is running and enforced

## Security rules

### Rule name: get-dev-key-status 
		> Description: "Determines if development keys have been revoked"
		> Synopsis: "State of development keys"
		> Rule file name: get-dev-key-state.rule

		> Supported products: MX 
		> Supported products: NFX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 


		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks if development keys have been left on the system.
		
		 If development keys were present, this rule will report the results
		 of the attempted revocation as Successful or a Failure.
		 This rule relies on a file present in 19.3R1 and further.
### Rule name: check-flow-session-summary-netconf 
		> Description: "Monitors and notify flow session details"
		> Synopsis: "Flow session summary statistics analyzer"
		> Rule file name: srx-flow-session-summary-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects flow session details for each PIC and notifies when anomalies are found.
		
		   1) "active-sessions-threshold-value" is the threshold that causes the rule
		      to report an anomaly. By default, it's 50000000. This rule will set a
		      dashboard color to red when active sessions for a PIC slot is greater
		      than this value.
		   2) "max-sessions-threshold-value" is the threshold that causes the rule
		      to report an anomaly. By default, it's 80000000. This rule will set a
		      dashboard color to red when active sessions for a PIC slot is greater
		      than this value.
### Rule name: check-veriexec-status 

		> Synopsis: "Checks for the veriexec status via OC sensor"
		> Rule file name: check-veriexec-status.rule




		> Detals:
		 This rule detects the status of veriexec in the system and detects the
		 anomalies based on if veriexec is loaded and enforced or not.
		 IMPORTANT: If telemetry is being done in plain text, veriexec state will
		 be visible over the network and can be a security risk. Hence prefer the
		 iagent rule below, unless the telemetry channel is secured.
### Rule name: check-cpu-memory-utilization-netconf 
		> Description: "SPU cpu and memory utilization of SRX cluster"
		> Synopsis: "SPU cpu and memory analyzer"
		> Rule file name: check-cpu-memory-utilization-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All-standalone-and-cluster-models;
		> Helper files: [ SecurityCPUMemoryUtilization.yml SecurityCPUMemoryUtilizationMidrangeHA.yml SecurityCPUMemoryUtilizationHighendHA.yml SecurityCPUMemoryUtilizationSA.yml SecurityCPUMemoryUtilizationHighendSA.yml ];
		> Supported healthbot version: 2.1.1
		> Detals:
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
		
### Rule name: check-spu-performance-netconf 
		> Description: "Collects SPU performance for each PIC and notifies in case of stats are above threshold"
		> Synopsis: "FPC SPU performance analyzer"
		> Rule file name: srx-performance-spu-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects linecards SPU utilization percentage and notifies when
		 anomalies are found.
		
		   1) "spu-cpu-threshold" is the threshold that causes the rule to report
		      an anomaly. By default, it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when SPU utilization exceed high threshold
		
### Rule name: check-appid-asc-cache-status-netconf 
		> Description: "To check the status of application system cache on SRX cluster"
		> Synopsis: "Check for application system cache status"
		> Rule file name: check-appid-asc-cache-status-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All-standalone-and-cluster-models;
		> Helper files: [ Security_APPID_ASC_Status.yml Security_APPID_ASC_Status_HA.yml Security_APPID_ASC_Status_SA.yml ];
		> Supported healthbot version: 2.1.1
		> Detals:
		 Monitors application system cache and notifies anomalies
		
### Rule name: check-idp-memory-counter-netconf 
		> Description: "Check idp memory counters of SRX cluster"
		> Synopsis: "IDP memory counters analyzer"
		> Rule file name: check-idp-memory-counter-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All-standalone-and-cluster-models;
		> Helper files: [ SecurityIDPCountersMemory.yml SecurityIDPCountersMemoryHA.yml SecurityIDPCountersMemorySA.yml ];
		> Supported healthbot version: 2.1.1
		> Detals:
		 Monitors idp memory counters and notifies anomalies when error count
		 increases.
### Rule name: check-alarm-status-netconf 
		> Description: "Collects system alarm details periodically and notifies anomalies when alarms found in SRX cluster"
		> Synopsis: "System alarm analyzer"
		> Rule file name: check-alarm-status-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All-standalone-and-cluster-models;
		> Helper files: [ SystemAlarmStatus.yml SystemAlarmStatusHA.yml SystemAlarmStatusSA.yml ];
		> Supported healthbot version: 2.1.1
		> Detals:
		 Detects system security alarms and notifies
		 One input control detection.
		
		 1) "input-alarm-description" is used to filter the based on the alarm
		    description
### Rule name: check-spu-performance-srx-cluster-netconf 
		> Description: "Collects SPU performance for each PIC and notifies in case of stats are above threshold"
		> Synopsis: "FPC SPU performance analyzer"
		> Rule file name: srx-cluster-performance-spu-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects linecards SPU utilization percentage in SRX cluster device and notifies when
		 anomalies are found.
		
		   1) "spu-cpu-threshold" is the threshold that causes the rule to report
		      an anomaly. By default, it's 80% of CPU utilization. This rule will set
		      a dashboard color to red when SPU utilization exceed high threshold
		
### Rule name: check-secureboot-status 
		> Description: "Checks that secure boot is running and enforced"
		> Synopsis: "System secure boot status"
		> Rule file name: secure-boot-status.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: NFX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 

			> Supported platforms: [ EX4650-48Y EX9251 EX9253 ];
			> Supported platforms: [ MX10003 MX10008 MX2008 MX2010 MX2020 MX204 MX240 MX480 MX960 ];
			> Supported platforms: NFX250;
			> Supported platforms: [ PTX10008 PTX10016 PTX3000 PTX5000 ];
			> Supported platforms: [ QFX10002-60C QFX10008 QFX10016 QFX5110 QFX5120-48Y ];
			> Supported platforms: [ SRX1500 SRX4600 ];

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks if secure boot is running and enforced and returns
		 an error if it is not.
		 This rule relies on a file present in 19.3R1 and beyond.
		 This rule is only applicible to devices where secure boot is capable.
		 If this rule is run on a device that is incapable of secure boot,
		 the result will be "secureboot status is unknonw" and the rule should be
		 removed.
### Rule name: check-idp-memory-utilization-netconf 
		> Description: "Used for to check the memory utilization of IDP data plane"
		> Synopsis: "IDP data plane memory utilization"
		> Rule file name: check-idp-memory-utilization-netconf.rule

		> Supported products: SRX 

			> Supported platforms: All-standalone-and-cluster-models;
		> Helper files: [ SecurityIdpMemoryUsage.yml SecurityIdpMemoryUsageHighendSA.yml SecurityIdpMemoryUsageMidrangeSA.yml SecurityIdpMemoryUsageHighendHA.yml SecurityIdpMemoryUsageMidrangeHA.yml ];
		> Supported healthbot version: 2.1.1
		> Detals:
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
		
### Rule name: check-veriexec-status-iagent 


		> Rule file name: check-veriexec-status-iagent.rule




		> Detals:
		 This rule detects the status of veriexec in the system and detects the
		 anomalies based on if veriexec is loaded and enforced or not.
		 It's recommended to have always veriexec enabled and loaded.
