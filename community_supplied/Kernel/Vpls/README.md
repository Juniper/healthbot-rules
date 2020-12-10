# HealthBot Vpls KPI rules and playbooks

## Vpls playbooks



		> Playbook file name: vpls-flood-token-cnt.playbook
		> Detals:
		 of VPLS flood token count parameter, and notifies when anomalies are found.
		 1) Rule "check-flood-token-cnt" checks the value of flood token count parameter and notifies
		    the anomalies. Sensor type Openconfig.
		 2) Rule "check-flood-token-cnt-iagent" checks the value of flood token count parameter and
		    notifies the anomalies. Sensor type iAgent.



		> Playbook file name: vpls-unicast-token-cnt.playbook
		> Detals:
		 with the help of the VPLS unicast token count parameter, and notifies when anomalies
		 are found.
		 1) Rule "check-ucst-token-cnt" checks the value of unicast token count and notifies
		    the anomalies. Sensor type Openconfig.
		 2) Rule "check-ucst-token-cnt-iagent" checks the value of unicast token count and
		    notifies the anomalies. Sensor type iAgent.

## Vpls rules

### Rule name: check-ucst-token-cnt-iagent 
		> Description: "Monitors system health with the help of unicast token count parameter. The sensor used is iAgent"
		> Synopsis: "Check unicast token count"
		> Rule file name: check-ucst-token-cnt-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring system health based on the value of the unicast token count.
		 This rule used iAgent sensor.
		 If this value is below 80% of unicast token max, the system is stable.
		 Any value between 80-90% of unicast token max is considered a warning.
		 Any value above 90% of unicast token max is considered risky and must be taken seriously.
### Rule name: check-ucst-token-cnt 
		> Description: "Monitors system health with the help of unicast token count parameter. The sensor used is open-config"
		> Synopsis: "Check unicast token count"
		> Rule file name: check-ucst-token-cnt.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring system health based on the value of the unicast token count.
		 This rule used iAgent sensor.
		 If this value is below 80% of unicast token max, the system is stable.
		 Any value between 80-90% of unicast token max is considered a warning.
		 Any value above 90% of unicast token max is considered risky and must be taken seriously.
### Rule name: check-flood-token-cnt-iagent 
		> Description: "Monitors system health with the help of flood token count parameter. The sensor used is iAgent"
		> Synopsis: "Check flood token count"
		> Rule file name: check-flood-token-cnt-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring system health based on the value of the flood token count.
		 The sensor used is iAgent.
		 If this value is below 80% of flood token max, the system is stable.
		 Any value between 80-90% of flood token max is considered a warning. Any value above 90% of flood token max is considered risky and must be taken seriously."
### Rule name: check-flood-token-cnt 
		> Description: "Monitors system health with the help of flood token count parameter. The sensor used is open-config"
		> Synopsis: "Check flood token count"
		> Rule file name: check-flood-token-cnt.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring system health based on the value of the flood token count.
		 The sensor used is openconfig.
		 If this value is below 80% of flood token max, the system is stable.
		 Any value between 80-90% of flood token max is considered a warning. Any value above 90% of flood token max is considered risky and must be taken seriously."
