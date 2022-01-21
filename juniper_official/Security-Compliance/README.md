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
### Rule name: check-interface-protocols 
		> Description: "Checks protocol is not enabled on all interfaces"

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
### Rule name: check-interface-to-disable 
		> Description: "Lists the interfaces that can be disabled"
		> Synopsis: ""
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
### Rule name: check-interfaces-present 
		> Description: "List of interfaces present on the device"
		> Synopsis: "Tnterface state analyzer"
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
### Rule name: check-login-message 
		> Description: "Checks if system login message is configured"

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
### Rule name: check-network-security 
		> Description: "Checks system network security"

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
### Rule name: check-ntp-authentication-list 
		> Description: "Collects ntp authentication information"

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
### Rule name: check-ntp-servers-configured 
		> Description: "Checks if more than one NTP servers are configured"

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
### Rule name: check-ntp-servers-list 
		> Description: "Collects names of ntp servers"

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
### Rule name: check-ntp-src-address 
		> Description: "Checks if source address is confgured for ntp"

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
### Rule name: check-ntp-trusted-list 


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
### Rule name: check-ports-config-secure 


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
### Rule name: check-ports-configured 
		> Description: "Ports that have configuration on them."

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
### Rule name: check-proxy-arp 
		> Description: "Checks if porxy-arp restricted and unrestricted are configured"

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
### Rule name: check-service-analytics-addr 
		> Description: "Checks if local address is configured for profile."

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
### Rule name: check-snmp-server-config 


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
### Rule name: check-snmp-server-list 


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
### Rule name: check-snmp-src-address 
		> Description: "Checks if source address is confgured for snmp"

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
### Rule name: check-ssh-services 
		> Description: "Checks ssh services configuration"

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
### Rule name: check-syslog-hosts-list 
		> Description: "Collects syslog host names."

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
### Rule name: check-syslog-hosts 
		> Description: "Checks for number of syslog hosts and if enhanced timestamp is configured."

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
### Rule name: check-syslog-src-address 
		> Description: "Checks if source address is confgured for syslog."

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
### Rule name: check-target-parameters 


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
### Rule name: check-trap-group-list 


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
### Rule name: check-trap-group 


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
