# HealthBot Security-Compliance KPI rules and playbooks

## Security-Compliance playbooks
### Playbook name: security-compliance 
		> Description: "Playbook to monitor and check security features for Device Hardening."
		> Synopsis: "Device Hardening KPI's"
		> Playbook file name: security-compliance.playbook
		> Details:

## Security-Compliance rules

### Rule name: check-community-access 
		> Description: "Checks for snmp community access"
		> Synopsis: "Community-Access KPI"
		> Rule file name: check-community-access.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: snmpcommunityAccess.yml;
		> More details:
		 Checks snmp configuration for community accesss for read/write permission.
		
### Rule name: check-interface-protocols 
		> Description: "Checks protocol is not enabled on all interfaces"
		> Synopsis: "Interface protocols KPI"
		> Rule file name: check-interface-protocols.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: protocolsInterface.yml;
		> More details:
		 Checks protocol is not enabled on all interfaces
		
### Rule name: check-interface-to-disable 
		> Description: "Lists the interfaces that can be disabled"
		> Synopsis: "Interfaces to disable KPI"
		> Rule file name: check-interface-to-disable.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: syslogconfig.yml;
		> More details:
		 Lists the interfaces that can be disabled.
		 One input control detection.
		
		   1) "interface-name" variable is configured, if needed ge interface name can be
		       updated.
		
### Rule name: check-interfaces-present 
		> Description: "List of interfaces present on the device"
		> Synopsis: "Interface state analyzer"
		> Rule file name: check-interfaces-present.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: interface-details.yml;
		> More details:
		 Checks for List of interfaces present on the device
		 One input control detection.
		
		   1) "interface-name" variable is configured, if needed ge interface name can be
		       updated.
### Rule name: check-login-message 
		> Description: "Checks if system login message is configured"
		> Synopsis: "Login message KPI"
		> Rule file name: check-login-message.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: systemmessage.yml;
		> More details:
		 Checks if system login message is configured.
		
### Rule name: check-network-security 
		> Description: "Checks system network security"
		> Synopsis: "Network security KPI"
		> Rule file name: check-network-security.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: systemconfig.yml;
		> More details:
		 Checks system network security parameters.
		
### Rule name: check-ntp-authentication-list 
		> Description: "Collects ntp authentication information"
		> Synopsis: "NTP authentication KPI"
		> Rule file name: check-ntp-authentication-list.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: ntpAuthentication.yml;
		> More details:
		 Collects ntp authentication information.
		
### Rule name: check-ntp-servers-configured 
		> Description: "Checks if more than one NTP servers are configured"
		> Synopsis: "NTP authentication KPI"
		> Rule file name: check-ntp-servers-configured.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: ntpServers.yml;
		> More details:
		 Checks if more than one NTP servers are configured
		
### Rule name: check-ntp-servers-list 
		> Description: "Collects names of ntp servers"
		> Synopsis: "NTP authentication KPI"
		> Rule file name: check-ntp-servers-list.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: ntpServers.yml;
		> More details:
		 Checks information about NTP server names.
		
### Rule name: check-ntp-src-address 
		> Description: "Checks if source address is confgured for ntp"
		> Synopsis: "NTP source address KPI"
		> Rule file name: check-ntp-src-address.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: ntpSrcAddr.yml;
		> More details:
		 Checks if source address is confgured for ntp
		
### Rule name: check-ntp-trusted-list 
		> Description: "Collects NTP trusted key information"
		> Synopsis: "NTP trusted keys KPI"
		> Rule file name: check-ntp-trusted-list.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: ntpTrusted.yml;
		> More details:
		 Collects NTP trusted key information.
		
### Rule name: check-ports-config-secure 
		> Description: "Checks for configuration that secures console,auxillary and diagnostic ports"
		> Synopsis: "ports configuration KPI"
		> Rule file name: check-ports-config-secure.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: systemportsconfig.yml;
		> More details:
		 Checks for configuration that secures console,auxillary and diagnostic ports.
		
### Rule name: check-ports-configured 
		> Description: "Ports that have configuration on them."
		> Synopsis: "ports configuration KPI"
		> Rule file name: check-ports-configured.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: interfaceconfig.yml;
		> More details:
		 Checks for Ports that have configuration on them.
		   1) "interface-name" variable is configured, if needed ge interface name can be
		       updated.
		
### Rule name: check-proxy-arp 
		> Description: "Checks if porxy-arp restricted and unrestricted are configured"
		> Synopsis: "proxy arp KPI"
		> Rule file name: check-proxy-arp.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: interfaceProxyArpConfig.yml;
		> More details:
		 Checks if porxy-arp restricted and unrestricted are conifgured
		
### Rule name: check-service-analytics-addr 
		> Description: "Checks if local address is configured for profile."
		> Synopsis: "service analytics address KPI"
		> Rule file name: check-service-analytics-addr.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: ServiceAnalyticsAddress.yml;
		> More details:
		 Checks if local address is configured for profile
		
### Rule name: check-snmp-server-config 
		> Description: "Checks the snmp server configuration and displays message. "
		> Synopsis: "snmp server configuration KPI"
		> Rule file name: check-snmp-server-config.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: snmpServerConfig.yml;
		> More details:
		 Checks the snmp server configuration and displays message.
		
### Rule name: check-snmp-server-list 
		> Description: "Collects snmp information about target address and name"
		> Synopsis: "snmp server KPI"
		> Rule file name: check-snmp-server-list.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: snmpServerConfig.yml;
		> More details:
		 Collects snmp information about target address and name.
		
### Rule name: check-snmp-src-address 
		> Description: "Checks if source address is confgured for snmp"
		> Synopsis: "snmp source address KPI"
		> Rule file name: check-snmp-src-address.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: snmpSrcAddr.yml;
		> More details:
		 Checks if source address is confgured for snmp
		
### Rule name: check-ssh-services 
		> Description: "Checks ssh services configuration"
		> Synopsis: "ssh services KPI"
		> Rule file name: check-ssh-services.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: check-ssh-services;
		> More details:
		 Checks ssh services configuration.
		
### Rule name: check-syslog-hosts-list 
		> Description: "Collects syslog host names."
		> Synopsis: "syslog hosts KPI"
		> Rule file name: check-syslog-hosts-list.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: syslogconfig.yml;
		> More details:
		 Collect syslog host names.
		   1) "host-name" variable is configured, it filters the hostname "log".
		
		
### Rule name: check-syslog-hosts 
		> Description: "Checks for number of syslog hosts and if enhanced timestamp is configured."
		> Synopsis: "syslog hosts KPI"
		> Rule file name: check-syslog-hosts.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: syslogconfig.yml;
		> More details:
		 Checks for number of syslog hosts and if enhanced timestamp is configured.
		   1) "host-name" variable is configured, it filters the hostname "log".
		
		
### Rule name: check-syslog-src-address 
		> Description: "Checks if source address is confgured for syslog."
		> Synopsis: "syslog source address KPI"
		> Rule file name: check-syslog-src-address.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: syslogSrcAddr.yml;
		> More details:
		 Checks if source address is confgured for syslog
		
### Rule name: check-target-parameters 
		> Description: "Collects information about snmp target parameters"
		> Synopsis: "snmp target parameters KPI"
		> Rule file name: check-target-parameters.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: snmptargetParameters.yml;
		> More details:
		 Collects information about snmp target parameters.
		
### Rule name: check-trap-group-list 
		> Description: "Collects information about snmp trap group"
		> Synopsis: "snmp trap group KPI"
		> Rule file name: check-trap-group-list.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: snmptrapGroup.yml;
		> More details:
		 Collects information about snmp trap group.
		
### Rule name: check-trap-group 
		> Description: "Counts the SNMP Trap servers configured for the trap group "
		> Synopsis: "snmp trap group KPI"
		> Rule file name: check-trap-group.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: snmptrapGroup.yml;
		> More details:
		 Counts the SNMP Trap servers configured for the trap group
		
