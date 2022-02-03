# HealthBot Predictive-Maintenance KPI rules and playbooks

## Predictive-Maintenance playbooks
### Playbook name: adapter-card-ml 
		> Description: "Playbook to monitor the anomalies in adc temperature and voltage"
		> Synopsis: "Anomalies KPI"
		> Playbook file name: adapter-card-ml.playbook
		> Details:
		 Playbook contains 2 rules which detects anomaly
		 and notifies when anomalies are found.
		
		 1) Rule adapter.card/check-adc-voltage-ml checks for anomalies
		    in adc voltage and notifies on the dashboard.
		 2) Rule adapter.card/check-adc-temperature-ml checks for anomalies
		    in adc temperature and notifies on the dashboard.
### Playbook name: predictive-maintenance 
		> Description: "Playbook to monitor the anomalies in temperature,voltage,power"
		> Synopsis: "Anomalies KPI"
		> Playbook file name: predictive-maintenance.playbook
		> Details:
		 Playbook contains 11 rules which detects anomaly
		 and notifies when anomalies are found.
		
		 1) Rule chassis.temperatures/check-re-temperature-ml checks for anomalies
		    in re tewmperature and notifies on the dashboard.
		 2) Rule control.board/check-cb-voltage-ml checks for anomalies
		    in comtrol board voltage and notifies on the dashboard.
		 3) Rule control.board/check-cb-temperature-ml checks for anomalies
		    in control board temperature and notifies on the dashboard.
		 4) Rule linecard.fpc/check-fpc-temperature-ml checks for anomalies
		    in fpc tewmperature and notifies on the dashboard.
		 5) Rule linecard.fpc/check-fpc-voltage-ml checks for anomalies
		    in fpc voltage and notifies on the dashboard.
		 6) Rule linecard.optical/check-optical-temperature-netconf-ml checks for anomalies
		    in optical tewmperature and notifies on the dashboard.
		 7) Rule linecard.optical/check-optics-tx-rx-power-ml  checks for anomalies
		    in optical tx and rx power and notifies on the dashboard.
		 8) Rule linecard.pfe/check-pfe-normal-discards-ml checks for anomalies
		    in pfe normal discards and notifies on the dashboard.
		 9) Rule interface.statistics/check-pcs-errors checks for anomalies
		    in pfe normal discards and notifies on the dashboard.
		 10) Rule linecard.optical/check-optical-interfaces-netconf checks for anomalies
		    in pfe normal discards and notifies on the dashboard.
		 11) Rule system.traffic/check-system-traffic-netconf checks for anomalies
		    in pfe normal discards and notifies on the dashboard.

## Predictive-Maintenance rules

### Rule name: check-adc-temperature-ml 
		> Description: "Check  if adapter card temp is within outlier"
		> Synopsis: "ADC card temperature anomaly"
		> Rule file name: check-adc-temperature-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:PTX, Platforms:A, Junos:18.1R1


		> Helper files: adc-temp-outlier.yml;
		> More details:
		 Checks for anomalies in temperature for ADC card
		
		 Two input control detection.
		
		   1) "high-temperature" variable is configured, if needed high values of temperature
		       can be checked.
		   2) "low-temperature " variable is configured, if needed low values of temperature
		       can be checked.
		
### Rule name: check-adc-voltage-ml 
		> Description: "Check if adc voltage is  having anomaly"
		> Synopsis: "ADC card voltage anomaly"
		> Rule file name: check-adc-voltage-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:PTX, Platforms:A, Junos:18.1R1


		> Helper files: adc-power-outlier.yml;
		> More details:
		 Checks for anomalies in reference voltage for ADC card
		
### Rule name: check-cb-temperature-ml 
		> Description: "Check  if control board temp is having anomaly"
		> Synopsis: "Control board temperature anomaly"
		> Rule file name: check-cb-temperature-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: control-board-temperature.yml;
		> More details:
		 Checks for anomalies in temperature for Control Boards
		
### Rule name: check-cb-voltage-ml 
		> Description: "Check if control board voltage is having  anomaly"
		> Synopsis: "Control board voltage anomaly"
		> Rule file name: check-cb-voltage-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: cb-power-voltage-outlier.yml;
		> More details:
		 Checks for anomalies in reference voltage for Control Board
		
### Rule name: check-fpc-temperature-ml 
		> Description: "Check  if  fpc temp is having anomaly"
		> Synopsis: "FPC temperature anomaly"
		> Rule file name: check-fpc-temperature-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: fpc-temp-outlier.yml;
		> More details:
		 Checks for anomalies in temperature for FPC card
		
### Rule name: check-fpc-voltage-ml 
		> Description: "Check  if  fpc voltage is having anomaly"
		> Synopsis: "FPC voltage anomaly"
		> Rule file name: check-fpc-voltage-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: fpc-power-outlier.yml;
		> More details:
		 Checks for anomalies in reference voltage for FPC Card
		
### Rule name: check-optical-temperature-netconf-ml 
		> Description: "Check if  optical temp is having  anomaly "
		> Synopsis: "Optical module temperature KPI"
		> Rule file name: check-optical-temperature-netconf-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.1.0
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1{ ## Warning: 'releases' is deprecated
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1 { ## Warning: 'releases' is deprecated
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX240, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX480, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX960, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX150, Junos:17.3R1 { ## Warning: 'releases' is deprecated
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1 { ## Warning: 'releases' is deprecated


		> Helper files: opticalTemperature.yml;
		> More details:
		 Checks for anomalies in optic module temperature.
		 One input controls detection
		
		  1) if-name variable, is the interface name to monitor. By default monitors all
		     interfaces.For specific interfaces to monitor, use regular expression.
		
### Rule name: check-optics-tx-rx-power-ml 
		> Description: "tx and rx anomaly for optic  interface"
		> Synopsis: "Optic module tx and rx anomaly"
		> Rule file name: check-optics-tx-rx-power-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: interfaceOpticsDiagnostics-tx-rx.yml;
		> More details:
		 Checks for anomalies in optic module tx and rx.
		
### Rule name: check-pcs-errors 
		> Description: "Checks for increase in pcs bit-error-seconds and errored-blocks-seconds and notifies when anomaly is detected"
		> Synopsis: "PCS anomalies"
		> Rule file name: check-pcs-errors.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 4.0.1
		> Supported product:MX, Platforms:A, Junos:18.1R1
		> Supported product:PTX, Platforms:A, Junos:18.1R1
		> Supported product:QFX, Platforms:A, Junos:18.1R1
		> Supported product:EX, Platforms:A, Junos:18.1R1
		> Supported product:SRX, Platforms:A, Junos:18.1R1


		> Helper files: pcs-outlier-Table.yml;
		> More details:
		 Checks for increase in pcs bit-error-seconds and errored-blocks-seconds.
		 One input controls detection
		
		  1) threshold variable, is the increase by which anomalies for pcs bit-error-seconds
		     and errored-blocks-seconds are monitored.
		
### Rule name: check-pfe-normal-discards-ml 
		> Description: "Collects packet forwarding engine hardware discard statistics  and notifies when normal  discard anomaly  is detected"
		> Synopsis: "Packet forwarding engine hardware discard statistics analyzer"
		> Rule file name: check-pfe-normal-discards-ml.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.0.1
		> Supported product:MX, Platforms:A, Junos:15.1R1 { ## Warning: 'releases' is deprecated


		> Helper files: pfe-discard-statistics.yml;
		> More details:
		 Checks for anomalies in pfe normal discard count
		 One input controls detection
		
		  1) discard-count variable, is the Number of discards increase between metrics,
		     before anomaly is reported.Default value is 1.
### Rule name: check-re-temperature-ml 
		> Description: "Collects routing-engine (RE) temperature periodically and notifies anomaly"
		> Synopsis: "Routing-engine temperature check"
		> Rule file name: check-re-temperature-ml.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX9200, Junos:17.3R1{ ## Warning: 'releases' is deprecated
		> Supported product:EX, Platforms:EX4650, Junos:18.3R1 { ## Warning: 'releases' is deprecated
		> Supported product:EX, Platforms:EX4600, Junos:18.4R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX240, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX480, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX960, Junos:16.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:MX, Platforms:MX150, Junos:17.3R1 { ## Warning: 'releases' is deprecated
		> Supported product:PTX, Platforms:PTX1000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:PTX, Platforms:PTX10000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:PTX, Platforms:PTX5000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX10000, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX5200, Junos:17.2R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX5100, Junos:18.1R1 { ## Warning: 'releases' is deprecated
		> Supported product:QFX, Platforms:QFX5120-48Y, Junos:18.3R1 { ## Warning: 'releases' is deprecated



		> More details:
		 Checks for anomalies in re temperature.
		 Four input controls detection
		
		  1) discard-count variable, is the Number of discards increase between metrics
		     before anomaly is reported.
		  2) re-slot-number variable, is the Routing engine slot numbers to monitor.
		     For specific re to monitor, use regular expression.
		  3) re-temperature-high-threshold variable, is the RE temperature high threshold
		     Utilization increase between metrics before anomaly is reported.Default is 55.
		  4) re-temperature-low-threshold variable, is the RE temperature low threshold
		     Utilization increase between metrics before anomaly is reported.Default is 45.
		
