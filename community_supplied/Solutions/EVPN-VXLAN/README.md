# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN rules

### Rule name: get-lldp-uplink-state 
		> Description: "Collects lldp session state periodically"
		> Synopsis: "LLDP neighbor state collector"
		> Rule file name: get-lldp-uplink-state-OC.rule

		> Supported products: MX 
                        > Supported platforms: All;
		> Supported products: QFX 
			> Supported platforms: All;

		> Supported healthbot version: 2.1.0
		> Detals:
### Rule name: get-lldp-uplink-latest-state 
		> Description: "Collects lldp session state periodically"
		> Synopsis: "LLDP neighbor state collector"
		> Rule file name: get-lldp-uplink-latest-state-OC.rule

		> Supported products: MX 
                        > Supported platforms: All;
		> Supported products: QFX 
			> Supported platforms: All;

		> Supported healthbot version: 2.1.0
		> Detals:
### Rule name: uplink-degradation-netconf 
		> Description: "finds the uplink degradation percent"
		> Synopsis: "kpi to calculate uplink degradation percent"
		> Rule file name: uplink-degradation-netconf.rule

		> Supported products: MX 
                        > Supported platforms: All;
		> Supported products: QFX 
			> Supported platforms: All;

		> Supported healthbot version: 2.1.0
		> Detals:
### Rule name: check-interface-flap-count-netconf 
		> Description: "Monitors the interface flap count"
		> Synopsis: "KPI to monitor the interface flap"
		> Rule file name: check-interface-flap-count-netconf.rule

		> Supported products: EX 
                        > Supported platforms: All;
		> Supported products: MX 
                        > Supported platforms: All;
		> Supported products: QFX 
			> Supported platforms: All;

		> Supported healthbot version: 2.1.0
		> Detals:
### Rule name: get-online-fpc-netconf 
		> Description: "collects online fpc using udf and updates dependent rules sensor table"
		> Synopsis: "collects online fpc using udf and updates dependent rules sensor table"
		> Rule file name: get-online-fpc.rule

		> Supported products: QFX 
			> Supported platforms: All;
		> Helper files: online-fpc-evpn-vxlan.yml;
		> Supported healthbot version: 3.0.0
		> Detals:

### Rule name: vni-provisioning-netconf 
		> Description: "This rule receives newlyadded vxlan vni syslog notification  event and provisions the vxlan vni in rest of the nodes"
		> Synopsis: "Vxlan vni provisioner"
		> Rule file name: vni-provisioning-netconf.rule

                > Supported products: QFX
                        > Supported platforms: All;

		> Detals:
		 Receives vxlan add vni syslog events from node and configures vxlan vni in
		 rest of the nodes in network.

## EVPN VXLAN playbooks
### Playbook name: evpn-vni-provisioning 
		> Description: "Playbook to check EVPN-VXLAN VNI provisioning"
		> Synopsis: "EVPN-VXLAN VNI provisioning"
		> Playbook file name: evpn-vni-provisioning.playbook
		> Detals:
		 Playbook contains rule which Receives vxlan add vni syslog notification
		 event and provisions the vxlan vni in rest of the nodes
		 1) Rule vni-provisioning-netconf.rule, Receives vxlan add vni syslog
		    notification  event and provisions the vxlan vni in rest of the nodes
		 NOTE: If you don't want to include any of the rule in the list, please create
		 new playbook and include only the required rules for your case.
