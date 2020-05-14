# HealthBot Pfe-wedge-detection KPI rules and playbooks

## Pfe-wedge-detection playbooks
### Playbook name: linecard-pfe-wedge-playbook 
		> Description: "Playbook to monitor pfe events"
		> Synopsis: "Playbook to monitor pfe events"
		> Playbook file name: linecard-pfe-wedge.playbook
		> Detals:
		 Playbook contains multiple rules which monitor syslog events as per the GROK patterns
		 defined by the users. Playbook is intended to filter PFE wedge related events and notify
		 anomalies in case of PFE wedge events
		 1) Rule "check-pfe-alarms" monitors PFE Alarm events as per the GROK
		    patterns defined by the user.
		 2) Rule "check-pfe-chassisd-events" monitors chassisd syslog events as per the GROK
		    patterns defined by the user.
		 3) Rule "check-pfe-eachip-events" monitors eachip syslog events as per the GROK
		    patterns defined by the user.
		 4) Rule "check-pfe-fpc-events" monitors FPC syslog events as per the GROK
		    patterns defined by the user.
		 5) Rule "check-pfe-luchip-events" monitors luchip syslog events as per the GROK
		    patterns defined by the user.
		 6) Rule "check-pfe-lueachip-events" monitors lueachip syslog events as per the GROK
		    patterns defined by the user.
		 7) Rule "check-pfe-manual-jmb-events" monitors manual jmb syslog events as per the GROK
		    patterns defined by the user.
		 8) Rule "check-pfe-misc-events" monitors pfe misc syslog events as per the GROK
		    patterns defined by the user.
		 9) Rule "check-pfe-mqchip-events" monitors mqchip syslog events as per the GROK
		    patterns defined by the user.
		 10) Rule "check-pfe-qsfp-events" monitors qsfp syslog events as per the GROK
		    patterns defined by the user.
		 11) Rule "/check-pfe-rpd-events" monitors pfe RPD syslog events as per the GROK
		    patterns defined by the user.
		 12) Rule "check-pfe-snmp-events" monitors pfe SNMP syslog events as per the GROK
		    patterns defined by the user.
		 13) Rule "check-pfe-wedge-events" monitors pfe wedge syslog events as per the GROK
		    and notify anomalies.
		 14) Rule "check-pfe-xmchip-events" monitors XMCHIP syslog events as per the GROK
		    patterns defined by the user.

## Pfe-wedge-detection rules

### Rule name: check-pfe-misc-events 
		> Description: "Using this rule the Misc pfe events will be monitored"
		> Synopsis: "Misc pfe events monitor"
		> Rule file name: pfe-misc-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors PFE MISC syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-alarms 
		> Description: "Using this rule the pfe alarms will be monitored"
		> Synopsis: "PFE alarms monitor"
		> Rule file name: pfe-alarms-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors PFE Alarms syslog messages as per the GROK patterns defined by the user.
### Rule name: check-pfe-xmchip-events 
		> Description: "Using this rule the xmchip events will be monitored"
		> Synopsis: "xmchip events monitor"
		> Rule file name: xmchip-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors XMCHIP syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-eachip-events 
		> Description: "Using this rule the eachip events will be monitored"
		> Synopsis: "eachip events monitor"
		> Rule file name: eachip-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors eachip syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-qsfp-events 
		> Description: "Using this rule the qsfp events will be monitored"
		> Synopsis: "qsfp events monitor"
		> Rule file name: qsfp-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors QSFP syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-luchip-events 
		> Description: "Using this rule the luchip events will be monitored"
		> Synopsis: "luchip events monitor"
		> Rule file name: luchip-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors luchip syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-snmp-events 
		> Description: "Using this rule the snmp events will be monitored"
		> Synopsis: "snmp events monitor"
		> Rule file name: pfe-snmp-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors PFE SNMP syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-rpd-events 
		> Description: "Using this rule the rpd events will be monitored"
		> Synopsis: "rpd events monitor"
		> Rule file name: pfe-rpd-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors PFE RPD syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-wedge-events 
		> Description: "Using this rule the PFE Wedge events will be monitored"
		> Synopsis: "PFE Wedge events monitor"
		> Rule file name: wedge-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors PFE WEDGE syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-manual-jmb-events 
		> Description: "Using this rule the jmb events will be monitored"
		> Synopsis: "jmb events monitor"
		> Rule file name: manual-jmb-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors JMB syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-lueachip-events 
		> Description: "Using this rule the lueachip events will be monitored"
		> Synopsis: "lueachip events monitor"
		> Rule file name: lueachip-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors lueachip syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-fpc-events 
		> Description: "Using this rule the pfe fpc events will be monitored"
		> Synopsis: "FPC events monitor"
		> Rule file name: fpc-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors FPC syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-mqchip-events 
		> Description: "Using this rule the mqchip events will be monitored"
		> Synopsis: "mqchip events monitor"
		> Rule file name: mqchip-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors mqchip syslog events as per the GROK patterns defined by the user.
### Rule name: check-pfe-chassisd-events 
		> Description: "Using this rule the Chassisd events will be monitored"
		> Synopsis: "Chassisd events monitor"
		> Rule file name: chassisd-events-syslog.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 3.0.0
		> Detals:
		 Monitors chassisd syslog events as per the GROK patterns defined by the user.
