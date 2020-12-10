# HealthBot Tnp KPI rules and playbooks

## Tnp playbooks



		> Playbook file name: tnp-frag-drop-cnt.playbook
		> Detals:
		 with the help of TNP fragment drop count parameter, and notifies when anomalies
		 are found.
		 1) Rule "check-tnp-fragment-drops" checks the value of tnp fragment drop count parameter
		    and notifies the anomalies. Sensor type Openconfig.
		 2) Rule "check-tnp-fragment-drops-iagent" checks the value of tnp fragment drop count parameter
		    and notifies the anomalies. Sensor type iAgent.



		> Playbook file name: tnp-hello-drop-cnt.playbook
		> Detals:
		 with the help of TNP hello drop count parameter, and notifies when anomalies
		 are found.
		 1) Rule "check-tnp-hello-drops" checks the value of the parameter TNP hello drop
		    count and notifies the anomalies. Sensor type Openconfig.
		 2) Rule "check-tnp-hello-drops-iagent" checks the value of the parameter TNP hello drop count
		    and notifies the anomalies. Sensor type iAgent.

## Tnp rules

### Rule name: check-tnp-fragment-drops 
		> Description: "Monitors system health with the help of TNP fragment drop count parameter. The sensor used is open-config"
		> Synopsis: "Check TNP fragment drop count"
		> Rule file name: check-tnp-fragment-drops.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors the system health on the basis of the tnp fragment drop count parameter.
		 Open config sensor is used here.
		 The rule collects the TNP fragment drop count and notifies anomaly if
		 the parameter exceeds the threshold.
### Rule name: check-tnp-hello-drops-iagent 
		> Description: "Monitors system health with the help of TNP hello drop count parameter. The sensor used is iAgent"
		> Synopsis: "Check TNP hello drop count"
		> Rule file name: check-tnp-hello-drops-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors the health of the system with the help of the tnp hello drop count parameter.
		
		 It uses iAgent sensor.
		 The rule collects tnp hello drop count and notifies anomaly if
		 the parameter exceeds the threshold.
### Rule name: check-tnp-fragment-drops-iagent 
		> Description: "Monitors system health with the help of TNP fragment drop count parameter. The sensor used is iAgent"
		> Synopsis: "Check TNP fragment drop count"
		> Rule file name: check-tnp-fragment-drops-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors the system health on the basis of the tnp fragment drop count parameter.
		 iAgent sensor is used here.
		 The rule collects the TNP fragment drop count and notifies anomaly if
		 the parameter exceeds the threshold.
### Rule name: check-tnp-hello-drops 
		> Description: "Monitors system health with the help of TNP hello drop count parameter. The sensor used is open-config"
		> Synopsis: "Check TNP hello drop count"
		> Rule file name: check-tnp-hello-drops.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors the health of the system with the help of the tnp hello drop count parameter.
		 It uses open config sensor.
		 The rule collects the tnp hello drop count and notifies anomaly if
		 the parameter exceeds threshold.
