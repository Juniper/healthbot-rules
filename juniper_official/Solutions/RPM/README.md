# HealthBot RPM KPI rules and playbooks

## RPM playbooks
### Playbook name: rpm-probe-netconf-playbook 
		> Description: "Playbook to check RPM probe statistics"
		> Synopsis: "RPM probe performance indicators"
		> Playbook file name: rpm-probe-netconf.playbook
		> Details:
		 Playbook contains rules which monitor RPM probs and notifies when
		 anomalies are found.
		
		 1) Rule rpm-probe-netconf, detects the RPM probe packet loss and
### Playbook name: rpm-probe-playbook 
		> Description: "Playbook to check RPM probe statistics"
		> Synopsis: "RPM probe performance indicators"
		> Playbook file name: rpm-probe.playbook
		> Details:
		 Playbook contains rules which monitor RPM probs and notifies when
		 anomalies are found.
		
		 1) Rule rpm-probe-packet-loss-openconfig, detects the RPM probe packet loss
		 2) Rule rpm-probe-rtt-openconfig, detects the RPM probe RTT
### Playbook name: rpm-twamp-openconf-playbook 
		> Description: "Playbook to check TWAMP probe statistics"
		> Synopsis: "TWAMP probe performance indicators"
		> Playbook file name: rpm-twamp-openconf.playbook
		> Details:
		 Playbook contains rules which monitor RPM probs and notifies when
		 anomalies are found.
		
		 1) Rule rpm-twamp-packet-loss-openconfig, detects the RPM twamp packet loss
		 2) Rule rpm-twamp-rtt-openconfig, detects the RPM twamp RTT

## RPM rules

### Rule name: rpm-probe-netconf 
		> Description: "RPM probe"
		> Synopsis: "RPM probe packet loss monitor"
		> Rule file name: rpm-probe-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1
		> Supported product:PTX, Platforms:PTX5000, Junos:15.1R1
		> Supported product:PTX, Platforms:PTX1000, Junos:15.1R1
		> Supported product:PTX, Platforms:PTX10000, Junos:15.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:15.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:15.1R1
		> Supported product:QFX, Platforms:QFX5100, Junos:15.1R1


		> Helper files: RPMprobe.yml;
		> More details:
		 Detects RPM probe packet loss and RTT value using Netconf sensor.
		 One inputs control detection:
		   1) rtt-threshold-variable, is the threshold that causes the rule to report
		       an anomaly. By default it's 50000. This rule will set a dashboard
		       color to red when probe RTT value more than this threshold, otherwise
		       color is set to green.
### Rule name: rpm-probe-packet-loss-openconfig 
		> Description: "Collects RPM packet loss periodically and notifies anomalies"
		> Synopsis: "RPM probe packet loss monitor"
		> Rule file name: rpm-probe-packet-loss.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:MX240, Junos:18.3R1
		> Supported product:MX, Platforms:MX480, Junos:18.3R1
		> Supported product:MX, Platforms:MX960, Junos:18.3R1
		> Supported product:MX, Platforms:MX2010, Junos:18.3R1
		> Supported product:MX, Platforms:MX2020, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX1000, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX10000, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX10000, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX5200, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.3R1



		> More details:
		 Detects RPM probe packet loss using open config sensor.
### Rule name: rpm-probe-rtt-openconfig 
		> Description: "Collects RPM RTT periodically and notifies anomalies"
		> Synopsis: "RPM probe RTT monitor"
		> Rule file name: rpm-probe-rtt.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:MX240, Junos:18.3R1
		> Supported product:MX, Platforms:MX480, Junos:18.3R1
		> Supported product:MX, Platforms:MX960, Junos:18.3R1
		> Supported product:MX, Platforms:MX2010, Junos:18.3R1
		> Supported product:MX, Platforms:MX2020, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX1000, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX10000, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX10000, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX5200, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.3R1



		> More details:
		 Detects RPM probe packet loss and RTT value using OpenConfig sensor.
		 One inputs control detection
		   1) rtt-threshold-variable, is the threshold that causes the rule to report
		       an anomaly. By default it's 50000. This rule will set a dashboard
		       color to red when probe RTT value more than this threshold, otherwise
		       color is set to green.
### Rule name: rpm-twamp-packet-loss-openconfig 
		> Description: "Collects TWAMP packet loss periodically and notifies anomalies"
		> Synopsis: "RPM probe packet loss monitor"
		> Rule file name: rpm-twamp-packet-loss.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:MX240, Junos:18.3R1
		> Supported product:MX, Platforms:MX480, Junos:18.3R1
		> Supported product:MX, Platforms:MX960, Junos:18.3R1
		> Supported product:MX, Platforms:MX2010, Junos:18.3R1
		> Supported product:MX, Platforms:MX2020, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX1000, Junos:18.3R1
		> Supported product:PTX, Platforms:PTX10000, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX10000, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX5200, Junos:18.3R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.3R1



		> More details:
		 Detects TWAMP probe packet loss using OpenConfig sensor.
### Rule name: rpm-twamp-rtt-openconfig 
		> Description: "Collects RPM twamp RTT periodically and notifies anomalies"
		> Synopsis: "RPM twamp RTT monitor"
		> Rule file name: rpm-twamp-rtt.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 3.1.0
		> Supported product:MX, Platforms:MX240, Junos:20.1R1
		> Supported product:MX, Platforms:MX480, Junos:20.1R1
		> Supported product:MX, Platforms:MX960, Junos:20.1R1
		> Supported product:MX, Platforms:MX2010, Junos:20.1R1
		> Supported product:MX, Platforms:MX2020, Junos:20.1R1
		> Supported product:PTX, Platforms:PTX5000, Junos:20.1R1
		> Supported product:PTX, Platforms:PTX1000, Junos:20.1R1
		> Supported product:PTX, Platforms:PTX10000, Junos:20.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:20.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:20.1R1
		> Supported product:QFX, Platforms:QFX5100, Junos:20.1R1



		> More details:
		 Detects RPM twamp RTT value using OpenConfig sensor.
		 One inputs control detection
		   1) rtt-threshold-variable, is the threshold that causes the rule to report
		       an anomaly. By default it's 50000. This rule will set a dashboard
		       color to red when probe RTT value more than this threshold, otherwise
		       color is set to green.
