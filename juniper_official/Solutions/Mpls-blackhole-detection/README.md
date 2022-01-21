# HealthBot Mpls-blackhole-detection KPI rules and playbooks

## Mpls-blackhole-detection playbooks
### Playbook name: mpls-blackhole-detection-playbook 
		> Description: "Playbook detects blackhole based on jnh exceptions and compares with RSVP session statistics and notifies anomalies"
		> Synopsis: "Mpls blackhole detection key performance indicators"
		> Playbook file name: mpls-blackhole-detection.playbook
		> Details:
		 Playbook contains multiple rules which monitor jnh exception traces& RSVP
		 session statistics and notifies when anomalies are found.
		
		 1) Rule jnh-drop-packets.rule, detects the jnh exception traces and notifies
		     anomalies when error count increases.
		 2) Rule rsvp-status.rule, detects the RSVP session statistics out and feeds
		     RSVP session data to rule jnh-drop-packets.rule
		 3) Rule "update-online-fpc-ospf" finds all the online FPCs in the chassis.

## Mpls-blackhole-detection rules

### Rule name: check-drop-packets 
		> Description: "Collects jnh exception traces from line cards and analyzes"
		> Synopsis: "Jnh exception traces analyzer"
		> Rule file name: jnh-drop-packets.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: [ jnhexceptionpkt.yml mplslabel.py ];
		> More details:
### Rule name: check-rsvp 
		> Description: "Collects RSVP statistics and analyzes"
		> Synopsis: "RSVP statistics analyzer"
		> Rule file name: rsvp-status.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:A, Junos:15.2R1
		> Supported product:PTX, Platforms:A, Junos:15.2R1
		> Supported product:QFX, Platforms:A, Junos:15.2R1
		> Supported product:EX, Platforms:A, Junos:15.2R1
		> Supported product:ACX, Platforms:A, Junos:15.2R1
		> Supported product:SRX, Platforms:A, Junos:15.2R1


		> Helper files: rsvpsession.yml;
		> More details:
