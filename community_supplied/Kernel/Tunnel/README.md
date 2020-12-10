# HealthBot Tunnel KPI rules and playbooks

## Tunnel playbooks



		> Playbook file name: looped-tunnel-cnt.playbook
		> Detals:
		 Playbook contains multiple rules which monitor the health of the system with the help
		 of the parameter looped tunnel count.
		
		 1) Rule "check-looped-tunnel-cnt" checks the value of looped tunnel count and
		    notifies anomalies. Sensor type Openconfig.
		 2) Rule "check-looped-tunnel-cnt-iagent" checks the value of looped tunnel count and
		    notifies anomalies. Sensor type iAgent.
		 3) Rule "check-looped-tunnel-cnt-sampling-based" checks the successive values of looped
		    tunnel count and notifies anomalies. Sensor type Openconfig.
		 4) Rule "check-looped-tunnel-cnt-sampling-based-iagent" checks the successive values of looped
		    tunnel count and notifies anomalies. Sensor type iAgent.



		> Playbook file name: rpf-tunnel-id-cnt.playbook
		> Detals:
		 of the system with the help of rpf tunnel id count
		 and notifies when anomalies are found
		 1) Rule "check-rpf-tunnel-id-cnt" checks the value of rpf tunnel id count
		    and notifies the anomalies. Sensor type Openconfig.
		 2) Rule "check-rpf-tunnel-id-cnt-iagent" checks the value of rpf tunnel id count
		    and notifies the anomalies. Sensor type iAgent.



		> Playbook file name: nonrpf-tunnel-id-cnt.playbook
		> Detals:
		 of the system with the help of non-rpf tunnel id count
		 parameter, and notifies when anomalies are found.
		 1) Rule "check-nonrpf-tunnel-id-cnt" checks the value of nonrpf tunnel id count
		    and notifies the anomalies. Sensor type Openconfig.
		 2) Rule "check-nonrpf-tunnel-id-cnt-iagent" checks the value of nonrpf tunnel id
		    count and notifies the anomalies. Sensor type iAgent.

## Tunnel rules

### Rule name: check-nonrpf-tunnel-id-cnt-iagent 
		> Description: "Monitors system health with the non-rpf tunnel id count parameter. The sensor used is iAgent"
		> Synopsis: "Check non-rpf tunnel id count"
		> Rule file name: check-nonrpf-tunnel-id-cnt-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in reporting the health of the system based on the value of non-rpf tunnel id count.
		 iAgent sensor is being used.
		 If non-rpf tunnel id count is between 85-99%, it is a warning sign.
		 If it is more than 99%, the system is under risk. Else, the system is healthy.
### Rule name: check-nonrpf-tunnel-id-cnt 
		> Description: "Monitors system health with the non-rpf tunnel id count parameter. The sensor used is open-config"
		> Synopsis: "Check non-rpf tunnel id count"
		> Rule file name: check-nonrpf-tunnel-id-cnt.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in reporting the health of the system based on the value of non-rpf tunnel id count.
		 Openconfig sensor is being used.
		 If non-rpf tunnel id count is between 85-99%, it is a warning sign.
		 If it is more than 99%, the system is under risk. Else, the system is healthy.
### Rule name: check-rpf-tunnel-id-cnt-iagent 
		> Description: "Monitors system health with RPF tunnel id count. The sensor used is iAgent"
		> Synopsis: "Check RPF tunnel id count"
		> Rule file name: check-rpf-tunnel-id-cnt-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring system health based on the value of rpf tunnel id count.
		 The sensor used is iAgent.
		 If the rpf tunnel id count value is between 80-95%, it is a warning sign.
		 If it is more than 95%, the system is under risk. Else, the system is healthy.
### Rule name: check-looped-tunnel-cnt 
		> Description: "Monitors system health with the looped tunnel count parameter. The sensor used is open-config"
		> Synopsis: "Check looped tunnel count"
		> Rule file name: check-looped-tunnel-cnt.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors system health based on looped tunnel count.
		 The sensor used is openconfig.
		 The rule throws red alarm if this value is non-zero, else it remains green.
		 If the value remains green, we also check whether consecutive samples are zero. If not, we raise a red alarm
### Rule name: check-looped-tunnel-cnt-iagent 
		> Description: "Monitors system health with looped tunnel id count parameter. The sensor used is iAgent"
		> Synopsis: "Check looped tunnel id count"
		> Rule file name: check-looped-tunnel-cnt-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: [ PTX-Series-All PTX-Series-Allset ];

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors system health based on looped tunnel count.
		 The sensor used is iAgent.
		 The rule throws red alarm if this value is non-zero, else it remains green.
		 If the value remains green, we also check whether consecutive samples are zero. If not, we raise a red alarm
### Rule name: check-looped-tunnel-cnt-sampling-based-iagent 
		> Description: "Monitors system health by comparing successive values of looped tunnel count parameter. The sensor used is iAgent"
		> Synopsis: "Check looped tunnel count (sampling)"
		> Rule file name: check-looped-tunnel-cnt-sampling-based-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors system health based on looped tunnel count.
		 The sensor used is iAgent.
		 The rule throws red alarm if the value between successive samplies is non-zero.
		 This rule kicks in when the alarm from the rule check-looped-tunnel-cnt-iagent is green.
### Rule name: check-rpf-tunnel-id-cnt 
		> Description: "Monitors system health with RPF tunnel id count. The sensor used is open-config"
		> Synopsis: "Check RPF tunnel id count"
		> Rule file name: check-rpf-tunnel-id-cnt.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule helps in monitoring system health based on the value of rpf tunnel id count.
		 The sensor used is openconfig.
		 If the rpf tunnel id count value is between 80-95%, it is a warning sign.
		 If it is more than 95%, the system is under risk. Else, the system is healthy.
### Rule name: check-looped-tunnel-cnt-sampling-based 
		> Description: "Monitors system health by comparing successive values of looped tunnel count. The sensor used is open-config"
		> Synopsis: "Check looped tunnel count (sampling)"
		> Rule file name: check-looped-tunnel-cnt-sampling-based.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule monitors system health based on looped tunnel count.
		 The sensor used is openconfig.
		 The rule throws red alarm if the difference between successive samples is non-zero.
		 The rule kicks in when the result from "check-looped-tunnel-cnt" rule is green.
