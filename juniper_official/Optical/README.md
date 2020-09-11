# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN playbooks
### Playbook name: interface-optical-kpis 
		> Description: "Playbook to check interface health regarding FEC errors and optical alarm conditions"
		> Synopsis: "Optical interface key performance indicators"
		> Playbook file name: interface-optical-kpis.playbook
		> Detals:
		 Playbook contains rules which monitor interface optical and notifies when
		 anomalies are found.
		 1) Rule check-optical-interfaces, Monitors interface optical state and
		 2) Rule check-optics-power-thresholds-openconfig, Monitors optical threshold value
		 3) Rule check-optics-power-openconfig, Monitors Linecard optics power and
### Playbook name: interface-optical-kpis-netconf 
		> Description: "Playbook to check interface health regarding alarm conditions"
		> Synopsis: "Optical interface key performance indicators"
		> Playbook file name: interface-optical-kpis-netconf.playbook
		> Detals:
		 Playbook contains rules which monitor interface optical and notifies when
		 anomalies are found.
		 1) Rule check-optical-interfaces-netconf, Monitors interface optical
		    state and notifies anomalies
		 2) Rule "check-optical-rx-netconf" monitors the optical Rx power levels
		    and notifies anomalies when it exceeds thresholds.
		 3) Rule "check-optical-temperature-netconf" monitors the optical temperature
		    and notifies anomalies when it exceeds thresholds.

## EVPN VXLAN rules

### Rule name: check-optics-power-thresholds-openconfig 
		> Description: "Collects the interface input optical power and notifies in case of anomalies"
		> Synopsis: "Interface rx optical power"
		> Rule file name: check-optics-power-thresholds-openconfig.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 3.1.0
		> Detals:
		 Detects interface optical power and notifies when anomalies are found.
		 One inputs control detection
		
		   1) interface-name-variable, is a regular expression that matches the
		      interfaces that you would like to monitor.    By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		
### Rule name: check-optical-interfaces 
		> Description: "Optical interface status analyser monitors for loss of signal or FEC uncorrected words"
		> Synopsis: "Optical interface status analyser"
		> Rule file name: check-optical-interfaces.rule

		> Supported products: ACX 

			> Supported platforms: All;


		> Detals:
### Rule name: check-optics-power-openconfig 
		> Description: "Collects the interface input optical power and notifies in case of anomalies"
		> Synopsis: "Interface rx optical power"
		> Rule file name: check-optics-power-openconfig.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 3.1.0
		> Detals:
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
### Rule name: check-optical-temperature-netconf 
		> Description: "To check if the optical temp is within limit."
		> Synopsis: "Optical module temperature KPI"
		> Rule file name: check-optical-temperature-netconf.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-optical-rx-netconf 
		> Description: "To check if the Rx power is within limit."
		> Synopsis: "Optical module RX level KPI"
		> Rule file name: check-optical-rx-netconf.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;
			> Supported platforms: all;
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 ];
			> Supported platforms: MX150;
			> Supported platforms: [ PTX1000 PTX10000 PTX5000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;

		> Supported healthbot version: 3.1.0
		> Detals:
### Rule name: check-optical-interfaces-netconf 
		> Description: "Monitor the interface optical degradation"
		> Synopsis: "KPI for  interface optical degradation"
		> Rule file name: check-optical-interfaces-netconf.rule

		> Supported products: MX 
		> Supported products: QFX 

			> Supported platforms: All;
			> Supported platforms: All;

		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors interface optical state and notifies when anomalies are found.
