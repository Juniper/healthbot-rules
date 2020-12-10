# HealthBot Multicast KPI rules and playbooks

## Multicast playbooks



		> Playbook file name: multicast-iif-mismatch.playbook
		> Detals:
		 help of multicast IIF mismatch error count parameter, and notifies when anomalies are
		 found.
		 1) Rule "check-multicast-iif-mismatch-error-cnt" checks the value of IIF mismatch error
		    count parameter and notifies the anomalies. Sensor type Openconfig.
		 2) Rule "check-multicast-iif-mismatch-error-cnt-iagent" checks the value of IIF mismatch error count
		    parameter and notifies the anomalies. Sensor type iAgent.



		> Playbook file name: multicast-resolve-request.playbook
		> Detals:
		 system with the help of multicast resolve request error count parameter,
		 and notifies when anomalies are found.
		 1) Rule "check-resolve-request-error-cnt" checks the value of resolve
		    request error count parameter and notifies the anomalies. Sensor type
		    Open config.
		 2) Rule "check-resolve-request-error-cnt-iagent" checks the value of resolve
		    request error count parameter and notifies the anomalies. Sensor type
		    iAgent.

## Multicast rules

### Rule name: check-multicast-iif-mismatch-error-cnt 
		> Description: "Monitors system health with the help of the iif mismatch error count parameter. The sensor used is open-config"
		> Synopsis: "Check multicast iif mismatch error count"
		> Rule file name: check-multicast-iif-mismatch-error-cnt.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks the health of the system on the basis of the iif_mismatch_err_cnt parameter.
		 The sensor used is Open config.
		 This rule collects iif mismatch error count and notifies anomaly if
		 iif mismatch error count exceeds threshold.
### Rule name: check-multicast-iif-mismatch-error-cnt-iagent 
		> Description: "Monitors system health with the help of the parameter iif mismatch error count. The sensor used is iAgent"
		> Synopsis: "Check multicast iif mismatch error count"
		> Rule file name: check-multicast-iif-mismatch-error-cnt-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks the health of the system on the basis of the iif_mismatch_err_cnt parameter.
		 The sensor used is iAgent.
		 This rule collects iif mismatch error count and notifies anomaly if
		 iif mismatch error count exceeds threshold.
### Rule name: check-resolve-request-error-cnt-iagent 
		> Description: "This rule helps to monitor the system health with the help of the parameter resolve request error count. The sensor used is iAgent"
		> Synopsis: "Check resolve request error count"
		> Rule file name: check-resolve-request-error-cnt-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring the health of the system on the basis of the resolve request error count parameter.
		 The sensor used is iAgent.
		 The rule collects resolve request error count and notifies anomaly if
		 resolve request error count exceeds threshold.
### Rule name: check-resolve-request-error-cnt 
		> Description: "This rule helps to monitor the system health with the parameter resolve request error count. The sensor used is open-config"
		> Synopsis: "Check resolve request error count"
		> Rule file name: check-resolve-request-error-cnt.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring the health of the system on the basis of the resolve request error count parameter.
		 The sensor used is open-config.
		 The rule throws collects resolve request error count and notifies anomaly if
		 resolve request error count exceeds threshold.
