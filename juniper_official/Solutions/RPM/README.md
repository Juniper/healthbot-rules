# HealthBot RPM KPI rules and playbooks

## RPM playbooks
### Playbook name: rpm-probe-netconf-playbook 
		> Description: "Playbook to check RPM probe statistics"
		> Synopsis: "RPM probe performance indicators"
		> Playbook file name: rpm-probe-netconf.playbook
		> Detals:
		 Playbook contains rules which monitor RPM probs and notifies when
		 anomalies are found.
		
		 1) Rule rpm-probe-netconf, detects the RPM probe packet loss and
### Playbook name: rpm-twamp-openconf-playbook 
		> Description: "Playbook to check TWAMP probe statistics"
		> Synopsis: "TWAMP probe performance indicators"
		> Playbook file name: rpm-twamp-openconf.playbook
		> Detals:
		 Playbook contains rules which monitor RPM probs and notifies when
		 anomalies are found.
		
		 1) Rule rpm-twamp-packet-loss-openconfig, detects the RPM twamp packet loss
		 2) Rule rpm-twamp-rtt-openconfig, detects the RPM twamp RTT
### Playbook name: rpm-probe-playbook 
		> Description: "Playbook to check RPM probe statistics"
		> Synopsis: "RPM probe performance indicators"
		> Playbook file name: rpm-probe.playbook
		> Detals:
		 Playbook contains rules which monitor RPM probs and notifies when
		 anomalies are found.
		
		 1) Rule rpm-probe-packet-loss-openconfig, detects the RPM probe packet loss
		 2) Rule rpm-probe-rtt-openconfig, detects the RPM probe RTT

## RPM rules

### Rule name: rpm-twamp-rtt-openconfig 
		> Description: "Collects RPM twamp RTT periodically and notifies anomalies"
		> Synopsis: "RPM twamp RTT monitor"
		> Rule file name: rpm-twamp-rtt.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5100 QFX5200 ];

		> Supported healthbot version: 3.1.0
		> Detals:
		 Detects RPM twamp RTT value using OpenConfig sensor.
		 One inputs control detection
		   1) rtt-threshold-variable, is the threshold that causes the rule to report
		       an anomaly. By default it's 50000. This rule will set a dashboard
		       color to red when probe RTT value more than this threshold, otherwise
		       color is set to green.
### Rule name: rpm-probe-packet-loss-openconfig 
		> Description: "Collects RPM packet loss periodically and notifies anomalies"
		> Synopsis: "RPM probe packet loss monitor"
		> Rule file name: rpm-probe-packet-loss.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5100 QFX5200 ];

		> Supported healthbot version: 3.1.0
		> Detals:
		 Detects RPM probe packet loss using Netconf sensor.
### Rule name: rpm-probe-rtt-openconfig 
		> Description: "Collects RPM RTT periodically and notifies anomalies"
		> Synopsis: "RPM probe RTT monitor"
		> Rule file name: rpm-probe-rtt.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5100 QFX5200 ];

		> Supported healthbot version: 3.1.0
		> Detals:
		 Detects RPM probe packet loss and RTT value using OpenConfig sensor.
		 One inputs control detection
		   1) rtt-threshold-variable, is the threshold that causes the rule to report
		       an anomaly. By default it's 50000. This rule will set a dashboard
		       color to red when probe RTT value more than this threshold, otherwise
		       color is set to green.
### Rule name: rpm-probe-netconf 
		> Description: "RPM probe"
		> Synopsis: "RPM probe packet loss monitor"
		> Rule file name: rpm-probe-netconf.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5100 QFX5200 ];

		> Supported healthbot version: 3.1.0
		> Detals:
		 Detects RPM probe packet loss and RTT value using Netconf sensor.
		 One inputs control detection
		   1) rpm-threshold-variable, is the threshold that causes the rule to report
		       an anomaly. By default it's 50000. This rule will set a dashboard
		       color to red when probe RTT value more than this threshold, otherwise
		       color is set to green.
### Rule name: rpm-twamp-packet-loss-openconfig 
		> Description: "Collects TWAMP packet loss periodically and notifies anomalies"
		> Synopsis: "RPM probe packet loss monitor"
		> Rule file name: rpm-twamp-packet-loss.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5100 QFX5200 ];

		> Supported healthbot version: 3.1.0
		> Detals:
		 Detects TWAMP probe packet loss using OpenConfig sensor.
