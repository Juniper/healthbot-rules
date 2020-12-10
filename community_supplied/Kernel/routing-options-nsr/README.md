# HealthBot routing-options-nsr KPI rules and playbooks

## routing-options-nsr playbooks
### Playbook name: routing-options-nsr-playbook 
		> Description: "Playbook monitors the kernel non-stop-routing health i.e Junos socket replication merge & split failure count and PRL queue full count"
		> Synopsis: "Kernel non-stop-routing key performance indicators"
		> Playbook file name: routing-options-nsr.playbook
		> Detals:
		 Playbook contains multiple rules which checks the health of kernel non-stop-routing
		 and notifies when anomalies are found.
		 1) Rule "check-jsr-merge-failure-count" detects the JSR merge failure breaches
		    and notifies the anomalies. Sensor type OpenConfig.
		 2) Rule "check-jsr-merge-failure-count-iagent" detects the JSR merge failure breaches
		    and notifies the anomalies. Sensor type iAgent.
		 3) Rule "check-jsr-prl-queue-full-count" detects the PRL queue full breaches
		    and notifies the anomalies. Sensor type OpenConfig.
		 4) Rule "check-jsr-prl-queue-full-count-iagent" detects the PRL queue full breaches
		    and notifies the anomalies. Sensor type iAgent.
		 5) Rule "check-jsr-split-failure-count" detects the JSR split failure breaches
		    and notifies the anomalies. Sensor type OpenConfig.

## routing-options-nsr rules

### Rule name: check-jsr-merge-failure-count 
		> Description: "Checks for Junos Socket Replication merge failure"
		> Synopsis: "Detect JSR Merge Failure"
		> Rule file name: check-jsr-merge-failure-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the Junos Socket Replication Merge failure count in the system.
		 It shows YELLOW alarm when the count is increased by minimum 1 from its previous value.
		 It's sampling time is 1 minute.
### Rule name: check-jsr-split-failure-count 
		> Description: "Checks for Junos Socket Replication split failure"
		> Synopsis: "Detect JSR Split Failure"
		> Rule file name: check-jsr-split-failure-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the Junos Socket Replication Split failure count in the system.
		 It shows YELLOW alarm when the count is increased by minimum 1 from its previous value.
		 It's sampling time is 1 minute.
### Rule name: check-jsr-prl-queue-full-count 
		> Description: "Checks for Junos Socket Replication PRL Queue Full"
		> Synopsis: "Detect JSR PRL Queue Full"
		> Rule file name: check-jsr-prl-queue-full-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the Junos Socket Replication PRL Queue full count in the system.
		 It shows YELLOW alarm when the count is increased by minimum 1 from its previous value.
		 It's sampling time is 1 minute.
### Rule name: check-jsr-merge-failure-count-iagent 
		> Description: "Checks for Junos Socket Replication merge failure"
		> Synopsis: "Detect JSR Merge Failure"
		> Rule file name: check-jsr-merge-failure-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the Junos Socket Replication Merge failure count in the system.
		 It shows YELLOW alarm when the count is increased by minimum 1 from its previous value.
		 It's sampling time is 1 minute.
### Rule name: check-jsr-prl-queue-full-count-iagent 
		> Description: "Checks for Junos Socket Replication PRL Queue Full"
		> Synopsis: "Detect JSR PRL Queue Full"
		> Rule file name: check-jsr-prl-queue-full-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the Junos Socket Replication PRL Queue full count in the system.
		 It shows YELLOW alarm when the count is increased by minimum 1 from its previous value.
		 It's sampling time is 1 minute.
