# HealthBot Mpls KPI rules and playbooks

## Mpls playbooks
### Playbook name: mpls-lsp-rsvp-kpis 
		> Description: "Playbook to check MPLS statistics w.r.t. LSP state, flaps, RSVP neighbor state, RSVP TE interface and global errors"
		> Synopsis: "Mpls key performance indicators"
		> Playbook file name: mpls-lsp-rsvp-kpis.playbook
		> Detals:
		 Playbook contains multiple rules which monitor MPLS statistics and notifies
		 when anomalies are found.
		
		 1) Rule check-lsp-state-oc, Collects LSP stats periodically and notifies
		    when LSP state is down.
		 2) Rule check-lsp-flap-count-oc, Collects LSP stats periodically and
		    notifies when LSP flaps.
		 3) Rule check-rsvp-neighbor-state-oc, Collects RSVP neighbor stats
		    periodically and notifies when rsvp neighbor state is down.
		 4) Rule check-te-rsvp-interface-errors-oc, Collects RSVP TE interface error
		    statistics periodically and notifies when error count increases.
		 5) check-te-rsvp-global-errors-oc, Collects RSVP TE global error statistics
		    periodically and notifies when error count increases.

## Mpls rules

### Rule name: check-lsp-state-oc 
		> Description: "Collects LSP stats periodically and notifies when LSP state is down"
		> Synopsis: "LSP state analyzer"
		> Rule file name: check-lsp-state-oc.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors MPLS LSP state and notifies when LSP state is UP or DOWN.
		 One input controls detection
		   1) input-lsp-name, is a regular expression that matches the LSP name that
		      you would like to monitor.  By default it's '.*', which matches all
		      LSPs. Use something like 'LSP1|LSP2' to match only LSP1 and LSP2.
### Rule name: check-lsp-flap-count-oc 
		> Description: "Collects LSP stats periodically and notifies when LSP flaps"
		> Synopsis: "LSP state analyzer"
		> Rule file name: check-lsp-flap-count-oc.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 2.1.0
		> Detals:
		 Detects MPLS LSP state changes and notifies when state change count
		 increases frequently.
		 One input controls detection
		
		   1) input-lsp-name, is a regular expression that matches the LSP name that
		      you would like to monitor.  By default it's '.*', which matches all
		      LSPs. Use something like 'LSP1|LSP2' to match only LSP1 and LSP2.
### Rule name: check-rsvp-neighbor-state-oc 
		> Description: "Collects RSVP neighbor stats periodically and notifies when rsvp neighbor state is down"
		> Synopsis: "RSVP neighbor state analyzer"
		> Rule file name: check-rsvp-neighbor-state-oc.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors MPLS LSP state and notifies when LSP state is UP or DOWN.
		 One input controls detection
		
		 1) input-rsvp-neighbor, is a regular expression that matches the RSVP
		    neighbor address you would like to monitor.  By default it's '.*',
		    which matches all neighbors. Use something like '192.168.1.*' to
		    match neighbors with 192.168.1.0 subnet.
### Rule name: check-te-rsvp-interface-errors-oc 
		> Description: "Collects RSVP TE interface error statistics periodically and notifies when error count increases"
		> Synopsis: "RSVP TE interface statistics analyzer"
		> Rule file name: check-te-rsvp-interface-errors-oc.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 2.1.0
		> Detals:
		 Detects RSVP TE interface error and notifies when error count increases
		 frequently.
		 One inputs control detection
		
		   1) input-te-interface, is a regular expression that matches the interfaces
		      that you would like to monitor.  By default it's '.*', which matches
		      all interfaces. Use something like 'ge.*' to match only gigabit
		      ethernet interfaces.
### Rule name: check-te-rsvp-global-errors-oc 
		> Description: "Collects RSVP TE global error statistics periodically and notifies when error count increases"
		> Synopsis: "RSVP TE global statistics analyzer"
		> Rule file name: check-te-rsvp-global-errors-oc.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];

		> Supported healthbot version: 2.1.0
		> Detals:
		 Detects RSVP TE global error and notifies error and notifies when error count increases
		 frequently.
