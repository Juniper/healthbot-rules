# HealthBot Mpls-blackhole-detection KPI rules and playbooks

## Mpls-blackhole-detection playbooks
### Playbook name: mpls-blackhole-detection-playbook 
		> Description: "Playbook detects blackhole based on jnh exceptions and compares with RSVP session statistics and notifies anomalies"
		> Synopsis: "Mpls blackhole detection key performance indicators"
		> Playbook file name: mpls-blackhole-detection.playbook
		> Detals:
		 Playbook contains multiple rules which monitor jnh exception traces& RSVP
		 session statistics and notifies when anomalies are found.
		
		 1) Rule jnh-drop-packets.rule, detects the jnh exception traces and notifies
		     anomalies when error count increases.
		 2) Rule rsvp-status.rule, detects the RSVP session statistics out and feeds
		     RSVP session data to rule jnh-drop-packets.rule

## Mpls-blackhole-detection rules

### Rule name: check-drop-packets 
		> Description: "Collects jnh exception traces from line cards and analyzes"
		> Synopsis: "Jnh exception traces analyzer"
		> Rule file name: jnh-drop-packets.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: [ jnhexceptionpkt.yml mplslabel.py ];
		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: check-rsvp 
		> Description: "Collects RSVP statistics and analyzes"
		> Synopsis: "RSVP statistics analyzer"
		> Rule file name: rsvp-status.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 
		> Supported products: ACX 
		> Supported products: SRX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: rsvpsession.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
