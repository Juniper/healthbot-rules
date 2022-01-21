# HealthBot Optical KPI rules and playbooks

## Optical playbooks
### Playbook name: interface-optical-kpis-netconf 
		> Description: "Playbook to check interface health regarding alarm conditions"
		> Synopsis: "Optical interface key performance indicators"
		> Playbook file name: interface-optical-kpis-netconf.playbook
		> Details:
		 Playbook contains rules which monitor interface optical and notifies when
		 anomalies are found.
		 1) Rule check-optical-interfaces-netconf, Monitors interface optical
		    state and notifies anomalies
		 2) Rule "check-optical-rx-netconf" monitors the optical Rx power levels
		    and notifies anomalies when it exceeds thresholds.
		 3) Rule "check-optical-temperature-netconf" monitors the optical temperature
		    and notifies anomalies when it exceeds thresholds.
### Playbook name: interface-optical-kpis 
		> Description: "Playbook to check interface health regarding FEC errors and optical alarm conditions"
		> Synopsis: "Optical interface key performance indicators"
		> Playbook file name: interface-optical-kpis.playbook
		> Details:
		 Playbook contains rules which monitor interface optical and notifies when
		 anomalies are found.
		 1) Rule check-optical-interfaces, Monitors interface optical state and
		 2) Rule check-optics-power-thresholds-openconfig, Monitors optical threshold value
		 3) Rule check-optics-power-openconfig, Monitors Linecard optics power and

## Optical rules

### Rule name: check-optical-interfaces-netconf 
		> Description: "Monitor the interface optical degradation"
		> Synopsis: "KPI for  interface optical degradation"
		> Rule file name: check-optical-interfaces-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:19.2R1
		> Supported product:QFX, Platforms:A, Junos:19.2R1



		> More details:
		 Monitors interface optical state and notifies when anomalies are found.
### Rule name: check-optical-interfaces 
		> Description: "Optical interface status analyser monitors for loss of signal or FEC uncorrected words"
		> Synopsis: "Optical interface status analyser"
		> Rule file name: check-optical-interfaces.rule
		> Sensor type: open-config 

		> Supported product:ACX, Platforms:A, Junos:11.4R1



		> More details:
### Rule name: check-optical-rx-netconf 
		> Description: "To check if the Rx power is within limit."
		> Synopsis: "Optical module RX level KPI"
		> Rule file name: check-optical-rx-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1



		> More details:
### Rule name: check-optical-temperature-netconf 
		> Description: "To check if the optical temp is within limit."
		> Synopsis: "Optical module temperature KPI"
		> Rule file name: check-optical-temperature-netconf.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1
		> Supported product:MX, Platforms:, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:MX, Platforms:MX150, Junos:17.3R1
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1



		> More details:
### Rule name: check-optics-power-openconfig 
		> Description: "Collects the interface input optical power and notifies in case of anomalies"
		> Synopsis: "Interface rx optical power"
		> Rule file name: check-optics-power-openconfig.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:MX240, Junos:18.1R1
		> Supported product:MX, Platforms:MX480, Junos:18.1R1
		> Supported product:MX, Platforms:MX960, Junos:18.1R1
		> Supported product:MX, Platforms:MX2010, Junos:18.1R1
		> Supported product:MX, Platforms:MX2020, Junos:18.1R1
		> Supported product:PTX, Platforms:PTX5000, Junos:18.1R1
		> Supported product:PTX, Platforms:PTX1000, Junos:18.1R1
		> Supported product:PTX, Platforms:PTX10000, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:18.1R1



		> More details:
		 Detects interface flaps and notifies when anomalies are found.
		 Two inputs control detection
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) dec-place, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the flap-increases are greater than
		      'flaps-threshold-variable' for 180s. If it sees any flaps increase for a
		      period of less than 180s, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: check-optics-power-thresholds-openconfig 
		> Description: "Collects the interface input optical power and notifies in case of anomalies"
		> Synopsis: "Interface rx optical power"
		> Rule file name: check-optics-power-thresholds-openconfig.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:MX240, Junos:18.1R1
		> Supported product:MX, Platforms:MX480, Junos:18.1R1
		> Supported product:MX, Platforms:MX960, Junos:18.1R1
		> Supported product:MX, Platforms:MX2010, Junos:18.1R1
		> Supported product:MX, Platforms:MX2020, Junos:18.1R1
		> Supported product:PTX, Platforms:PTX5000, Junos:18.1R1
		> Supported product:PTX, Platforms:PTX1000, Junos:18.1R1
		> Supported product:PTX, Platforms:PTX10000, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:18.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:18.1R1



		> More details:
		 Detects interface optical power and notifies when anomalies are found.
		 One inputs control detection
		
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.    By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		
