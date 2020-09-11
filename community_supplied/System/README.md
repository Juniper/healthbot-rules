# HealthBot EVPN KPI rules and playbooks

## EVPN VXLAN playbooks
### Playbook name: system-additional-kpis 
		> Description: "To check system commit, OS file descriptors usage and sockets usage is within threshold."
		> Synopsis: "system key performance indicators"
		> Playbook file name: system-kpi.playbook
		> Detals:
		 Playbook contains multiple rules which checks the file descriptors and sockets
		 usage and notifies when anomalies are found.
		 1) Rule "check-file-descriptor-usage-netconf" monitors the file descriptor usage
		    and notifies anomalies when usage exceeds thresholds.
		 2) Rule "check-file-open-netconf" detects the count of number of open files and
		    is referenced by file descriptor usage rule.
		 3) Rule "check-socket-usage-netconf" monitors the file sockets usage and notifies
		    anomalies when usage exceeds thresholds.
		 4) Rule "check-sockets-open-netconf" detects the count of number of sockets and
		    is referenced by check-socket-usage rule .
		 5) Rule "commit-history" monitors the system commits and notifies anomalies.
### Playbook name: snmp-system-playbook 


		> Playbook file name: snmp-system.playbook
		> Detals:
### Playbook name: tcam-usage-community 
		> Description: "To check if TCAM Usage on QFX5K and QFX10K is below threshold."
		> Synopsis: "TCAM Usage on QFX5K and QFX10K"
		> Playbook file name: tcam-usage-kpi.playbook
		> Detals:
		 Playbook contains multiple rules which checks the tcam usage on qfx10k and qfx5k
		 devices and notifies when anomalies are found.
		 1) Rule "check-tcam-qfx5k-netconf" monitors the TCAM Usage on QFX5K.
		    and notifies anomalies when it exceeds thresholds.
		 2) Rule "check-tcam-qfx10k-netconf" monitors the TCAM Usage on QFX10K.
		    and notifies anomalies when it exceeds thresholds.

## EVPN VXLAN rules

### Rule name: check-socket-usage-netconf 
		> Description: "Check the socket usage on the system. "
		> Synopsis: "Free OS sockets KPI"
		> Rule file name: check-socket-usage-netconf.rule

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
### Rule name: check-file-descriptor-usage-netconf 
		> Description: "To monitor the usage of file descriptor"
		> Synopsis: "OS File Descriptors KPI"
		> Rule file name: check-file-descriptor-usage-netconf.rule

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
### Rule name: check-tcam-qfx5k-netconf 
		> Description: "Check TCAM Usage on QFX5K."
		> Synopsis: "TCAM Usage KPI"
		> Rule file name: check-tcam-qfx5k-netconf.rule

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
### Rule name: check-file-open-netconf 
		> Description: "To check the file descriptors that are open."
		> Synopsis: "OS File Descriptors KPI"
		> Rule file name: check-file-open-netconf.rule

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
### Rule name: check-tcam-qfx10k-netconf 
		> Description: "Check TCAM Usage on QFX10K."
		> Synopsis: "TCAM Usage KPI"
		> Rule file name: check-tcam-qfx10k-netconf.rule

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
### Rule name: check-sockets-open-netconf 
		> Description: "To check the number of open sockets."
		> Synopsis: "Free OS sockets KPI"
		> Rule file name: check-sockets-open-netconf.rule

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
### Rule name: check-snmp-system-cpu-memory 
		> Description: "Collects CPU, Memory Utilization details from Routing Engines and notify anomalies based on threshold values "
		> Synopsis: "System CPU, Memory Utilization change detector"
		> Rule file name: snmp-system-cpu-memory.rule

		> Supported products: MX 

			> Supported platforms: ALL;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects System CPU & memory utilization and notifies when anomalies are found.
		 One input control detection
		
		   1) Threshold, is the threshold value for CPU and memory utiilzation takes as input and pass to the rule to
		      report an anomaly.  By default value is 80
### Rule name: commit-history 
		> Description: "Pulls the commit history and displays it."
		> Synopsis: "commit history detector"
		> Rule file name: commit-history.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: all;
			> Supported platforms: all;
			> Supported platforms: all;
			> Supported platforms: all;

		> Supported healthbot version: 3.1.0
		> Detals:
		 Monitors commit history and notifies when anomalies are found.
		 Three inputs control detection
		   1) l1-commit-threshold, lowest threshold in minutes notifies the commit.
		       By default it monitors the commit in the last 5 minutes. If there is
		       any commits in the last 5 minutes, it'll turn the color to yellow.
		   2) l2-commit-threshold, lowest threshold in minutes notifies the commit.
		       By default it monitors the commit in the last 30 minutes. If there is
		       any commits in the last 30 minutes, it'll turn the color to yellow.
		   3) l3-commit-threshold, lowest threshold in minutes notifies the commit.
		       By default it monitors the commit in the last 60 minutes. If there is
		       any commits in the last 60 minutes, it'll turn the color to yellow.
		       if it's not matching above, it'll turn to green.
