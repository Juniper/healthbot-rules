# HealthBot EX-KPIs-monitoring KPI rules and playbooks

## EX-KPIs-monitoring playbooks
### Playbook name: DHCP-server-statistics 
		> Description: "Playbook to monitor dhcp counters w.r.t. dhcpleaseunknown, bootrequest, dhcpdecline, dhcpforcerenew etc"
		> Synopsis: "DHCP Local Server and Relay Statistics KPIs"
		> Playbook file name: DHCP-server-statistics.playbook
		> Details:
		 Playbook contains 2 rules which monitors dhcp local server and dhcp relay statistics
		 and notifies when anomalies are found.
		
		 1) Rule dhcp.localserver/check-dhcp-server-statistics-netconf, detects the dhcp decline value and notifies
		    anomalies when count exceeds threshold values.
		 2) Rule dhcp.relayserver/check-dhcp-server-statistics-netconf, detects the dhcp decline value and notifies
		     anomalies when count exceeds threshold value.
### Playbook name: dot1x-user-authentication-kpis 
		> Description: "Playbook to detect dot1x authenticated ,bypassed and authentication failed users"
		> Synopsis: "dot1x authentication KPI"
		> Playbook file name: dot1x-user-authentication-kpis.playbook
		> Details:
		 Playbook contains 3 rules which monitors dot1x authentication and notifies the status.
		
		 1) Rule check-dot1x-authenticated-users-netconf, monitors the authenticated user count
		    and the interface through which user is authenticating.
		 2) Rule check-dot1x-authentication-bypassed-users-netconf, detects the mac id and
		     interface through which user is authenticating.
		 3) Rule check-dot1x-authentication-failed-users-netconf, detects authentication failures
		     and notifies user id, mac id, interface name and fail count.
### Playbook name: layer2-switch-interface-kpis 
		> Description: "Playbook to check interface health w.r.t. auto-negotiation status, flaps, interface status, input & output traffic and errors"
		> Synopsis: "Interface key performance indicators"
		> Playbook file name: layer2-switch-interface-kpis.playbook
		> Details:
### Playbook name: layer2-switch-system-kpis 
		> Description: "Playbook checks the system health i.e. system cpu and memory utilization, process cpu and memory utilization,packet drops on input and output interface, IP no socket buffer drops and System uptime"
		> Synopsis: "System key performance indicators"
		> Playbook file name: layer2-switch-system-kpis.playbook
		> Details:
### Playbook name: PoE-KPI-Playbook 
		> Description: "Playbook to monitor dot1x POE Interface and Controller characteristics like state and power consumption."
		> Synopsis: "PoE related KPI"
		> Playbook file name: PoE-KPI-Playbook.playbook
		> Details:
		 Playbook contains 3 rules which monitors POE status , interface and controller
		 power consumption and notifies the status.
		
		 1) Rule check-poe-total-power-netconf, checks POE Controller power consumption and raises
		    alarm in case of power consumption is above threshold
		 2) Rule check-poe-operational-status-netconf, POE Interface Operational state and
		    notifies when state is down.
		 3) Rule check-power-consumption-netconf, POE Interface Power consumption and notifies
		    when power consumption is above threshold

## EX-KPIs-monitoring rules

### Rule name: check-dot1x-authenticated-users-netconf 
		> Description: "Monitors dot1x authenticated users count and displays information"
		> Synopsis: "dot1x authenticated users count KPI"
		> Rule file name: check-dot1x-authenticated-users-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
		 Measures authenticated user count and the interface through which user tries to login.
### Rule name: check-dot1x-authentication-bypassed-users-netconf 
		> Description: "Monitors dot1x authenticated bypass users mac id and displays information"
		> Synopsis: "dot1x authenticated bypass users mac id KPI"
		> Rule file name: check-dot1x-authentication-bypassed-users-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:17.3R1



		> More details:
		 Detects mac-id that has bypassed authentication and the interface through which user tries to login..
### Rule name: check-dot1x-authentication-failed-users-netconf 
		> Description: "Monitors dot1x authentication failed users and displays information"
		> Synopsis: "dot1x authentication failed user mac ,userid, fail count  KPI"
		> Rule file name: check-dot1x-authentication-failed-users-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
		 Detects authentication failure and displays details.
### Rule name: check-interface-auto-negotiation-netconf 
		> Description: "Collects interface auto negotiation state periodically and notifies when status is incomplete "
		> Synopsis: "Interface auto negotiation status analyzer"
		> Rule file name: check-interface-auto-negotiation-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
### Rule name: check-interface-errors-netconf 
		> Description: "Collects the interface errors (errors (all), drops,discards, timeouts and runts) periodically and notifies in case of anomalies"
		> Synopsis: "Interface error analyzer"
		> Rule file name: check-interface-errors-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
### Rule name: check-interface-flaps-netconf 
		> Description: "Collects link flap count periodically and notifies when flap count increases"
		> Synopsis: "Link flaps detector"
		> Rule file name: check-interface-flaps-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
### Rule name: check-interface-status-netconf 
		> Description: "Collects interface link oper state periodically and notifies when neighbor sate is down"
		> Synopsis: "Interface state analyzer"
		> Rule file name: check-interface-status-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
### Rule name: check-interface-traffic-netconf 
		> Description: "Collects the interface input and output traffic."
		> Synopsis: "Interface input and output traffic analyzer"
		> Rule file name: check-interface-traffic-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
### Rule name: check-stp-state-netconf 
		> Description: "Monitors member vlan STP state periodically and notifies in case of anomalies"
		> Synopsis: "STP state analyzer"
		> Rule file name: check-stp-state-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:EX, Platforms:A, Junos:17.3R1
		> Supported product:MX, Platforms:A, Junos:15.1R1



		> More details:
### Rule name: check-system-statistics-ip 
		> Description: "Monitors incoming ip no socket buffer drops"
		> Synopsis: "Incoming raw ip packets analyzer"
		> Rule file name: check-system-statistics-ip-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.0.1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:MX, Platforms:A, Junos:11.4R1
		> Supported product:PTX, Platforms:A, Junos:11.4R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: system-statistics-ip.yml;
		> More details:
