# HealthBot EX-KPIs-monitoring KPI rules and playbooks

## EX-KPIs-monitoring playbooks
### Playbook name: DHCP-server-statistics 
		> Description: "Playbook to monitor dhcp counters w.r.t. dhcpleaseunknown, bootrequest, dhcpdecline, dhcpforcerenew etc"
		> Synopsis: "DHCP Local Server and Relay Statistics KPIs"
		> Playbook file name: DHCP-server-statistics.playbook
		> Detals:
		 Playbook contains 2 rules which monitors dhcp local server and dhcp relay statistics
		 and notifies when anomalies are found.
		
		 1) Rule dhcp.localserver/check-dhcp-server-statistics-netconf, detects the dhcp decline value and notifies
		    anomalies when count exceeds threshold values.
		 2) Rule dhcp.relayserver/check-dhcp-server-statistics-netconf, detects the dhcp decline value and notifies
		     anomalies when count exceeds threshold value.
### Playbook name: PoE-KPI-Playbook 
		> Description: "Playbook to monitor dot1x POE Interface and Controller characteristics like state and power consumption."
		> Synopsis: "PoE related KPI"
		> Playbook file name: PoE-KPI-Playbook.playbook
		> Detals:
		 Playbook contains 3 rules which monitors POE status , interface and controller
		 power consumption and notifies the status.
		
		 1) Rule check-poe-total-power-netconf, checks POE Controller power consumption and raises
		    alarm in case of power consumption is above threshold
		 2) Rule check-poe-operational-status-netconf, POE Interface Operational state and
		    notifies when state is down.
		 3) Rule check-power-consumption-netconf, POE Interface Power consumption and notifies
		    when power consumption is above threshold
### Playbook name: layer2-switch-interface-kpis 
		> Description: "Playbook to check interface health w.r.t. auto-negotiation status, flaps, interface status, input & output traffic and errors"
		> Synopsis: "Interface key performance indicators"
		> Playbook file name: layer2-switch-interface-kpis.playbook
		> Detals:
### Playbook name: layer2-switch-system-kpis 
		> Description: "Playbook checks the system health i.e. system cpu and memory utilization, process cpu and memory utilization,packet drops on input and output interface, IP no socket buffer drops and System uptime"
		> Synopsis: "System key performance indicators"
		> Playbook file name: layer2-switch-system-kpis.playbook
		> Detals:
### Playbook name: dot1x-user-authentication-kpis 
		> Description: "Playbook to detect dot1x authenticated ,bypassed and authentication failed users"
		> Synopsis: "dot1x authentication KPI"
		> Playbook file name: dot1x-user-authentication-kpis.playbook
		> Detals:
		 Playbook contains 3 rules which monitors dot1x authentication and notifies the status.
		
		 1) Rule check-dot1x-authenticated-users-netconf, monitors the authenticated user count
		    and the interface through which user is authenticating.
		 2) Rule check-dot1x-authentication-bypassed-users-netconf, detects the mac id and
		     interface through which user is authenticating.
		 3) Rule check-dot1x-authentication-failed-users-netconf, detects authentication failures
		     and notifies user id, mac id, interface name and fail count.

## EX-KPIs-monitoring rules

### Rule name: check-dot1x-authentication-bypassed-users-netconf 
		> Description: "Monitors dot1x authenticated bypass users mac id and displays information"
		> Synopsis: "dot1x authenticated bypass users mac id KPI"
		> Rule file name: check-dot1x-authentication-bypassed-users-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Detects mac-id that has bypassed authentication and the interface through which user tries to login..
### Rule name: check-system-statistics-ip 
		> Description: "Monitors incoming ip no socket buffer drops"
		> Synopsis: "Incoming raw ip packets analyzer"
		> Rule file name: check-system-statistics-ip-netconf.rule

		> Supported products: ACX 
		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: system-statistics-ip.yml;
		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-dot1x-authentication-failed-users-netconf 
		> Description: "Monitors dot1x authentication failed users and displays information"
		> Synopsis: "dot1x authentication failed user mac ,userid, fail count  KPI"
		> Rule file name: check-dot1x-authentication-failed-users-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Detects authentication failure and displays details.
### Rule name: check-interface-errors-netconf 
		> Description: "Collects the interface errors (errors (all), drops,discards, timeouts and runts) periodically and notifies in case of anomalies"
		> Synopsis: "Interface error analyzer"
		> Rule file name: check-interface-errors-netconf.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-poe-total-power-netconf 
		> Description: "Monitors PoE controller power consumption and display anomaly where power usage is more than the threshold"
		> Synopsis: "Controller power consumption KPI"
		> Rule file name: poe-controller-total-power-netconf.rule

		> Supported products: EX 

			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Detects POE Controller Power consumption and notifies when anomalies are found.
		 One input control detection
		
		   1) poe-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 80. This rule will set a dashboard
		      color to red when the controller power utilization is greater than
		      poe-threshold-variable.Otherwise color is set to green.
		
### Rule name: check-system-uptime-snmp 
		> Description: "Collects the time when the system was last booted."
		> Synopsis: "System uptime analyzer"
		> Rule file name: check-system-uptime-snmp.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-interface-traffic-netconf 
		> Description: "Collects the interface input and output traffic."
		> Synopsis: "Interface input and output traffic analyzer"
		> Rule file name: check-interface-traffic-netconf.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-interface-auto-negotiation-netconf 
		> Description: "Collects interface auto negotiation state periodically and notifies when status is incomplete "
		> Synopsis: "Interface auto negotiation status analyzer"
		> Rule file name: check-interface-auto-negotiation-netconf.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-stp-state-netconf 
		> Description: "Monitors member vlan STP state periodically and notifies in case of anomalies"
		> Synopsis: "STP state analyzer"
		> Rule file name: check-stp-state-netconf.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-dot1x-authenticated-users-netconf 
		> Description: "Monitors dot1x authenticated users count and displays information"
		> Synopsis: "dot1x authenticated users count KPI"
		> Rule file name: check-dot1x-authenticated-users-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Measures authenticated user count and the interface through which user tries to login.
### Rule name: check-dhcp-server-statistics-netconf 
		> Description: "Monitors DHCP local server statistics and display anomalies"
		> Synopsis: "DHCP local server statistics KPI"
		> Rule file name: dhcp-localserver-statistics-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Detects DHCP local server statistics and notifies when anomalies are found.
		 Two inputs control detection
		
		   1) threshold-ratio-variable, is the threshold ratio that causes the rule to
		      report an anomaly.  By default it's 10.If the packet drop ratio is greater
		      than or equal to 10 then it will turn red else it will show green.
		
		   2) threshold-value-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when the counters for dhcp fields are greater than
		      threshold-value-variable for 300s. If it sees any count increase for a
		      period of less than 300s, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: check-system-traffic-netconf 
		> Description: "Collects system total io packets and notifies in case of anomalies when io traffic difference is above static and dynamic threshold"
		> Synopsis: "system traffic statistics analyzer"
		> Rule file name: check-system-traffic-netconf.rule

		> Supported products: ACX 
		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: [ SystemTrafficTable.yml traffic_diff.py ];
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-interface-flaps-netconf 
		> Description: "Collects link flap count periodically and notifies when flap count increases"
		> Synopsis: "Link flaps detector"
		> Rule file name: check-interface-flaps-netconf.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-power-consumption-netconf 
		> Description: "Monitors PoE interface power consumption and display anomaly where power usage is more than the threshold"
		> Synopsis: "PoE interface power consumption KPI"
		> Rule file name: poe-interface-total-power-netconf.rule

		> Supported products: EX 

			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Detects POE Interface Power consumption and notifies when anomalies are found.
		 Two inputs control detection
		
		   1) poe-threshold-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 80. This rule will set a dashboard
		      color to red when the interface power utilization is greater than
		      poe-threshold-variable.Otherwise color is set to green.
		
		   2) variable-status-variable, is used to check if the interface operational
		      state is ON.
### Rule name: check-dhcp-server-statistics-netconf 
		> Description: "Monitors DHCP relay server statistics and display anomaly when dhcp packets drop"
		> Synopsis: "DHCP relay server statistics KPI"
		> Rule file name: dhcp-relayserver-statistics-netconf.rule

		> Supported products: MX 
		> Supported products: EX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Detects DHCP relay server statistics and notifies when anomalies are found.
		 One input control detection
		
		   1) threshold-value-variable, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when the value for dhcp decline is greater than
		      threshold-value-variable continuosly for 300s. If it sees any count increase,
		      it'll turn the color to yellow,otherwise color is set to green.
		
### Rule name: check-interface-status-netconf 
		> Description: "Collects interface link oper state periodically and notifies when neighbor sate is down"
		> Synopsis: "Interface state analyzer"
		> Rule file name: check-interface-status-netconf.rule

		> Supported products: EX 
		> Supported products: MX 

			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
### Rule name: check-poe-operational-status-netconf 
		> Description: "Monitors PoE operational and display anomaly when operational state is OFF"
		> Synopsis: "PoE operational KPI"
		> Rule file name: poe-interface-operational-netconf.rule

		> Supported products: EX 

			> Supported platforms: all;

		> Supported healthbot version: 3.0.1
		> Detals:
		 Detects POE Interface Operational state and notifies when anomalies are found.
