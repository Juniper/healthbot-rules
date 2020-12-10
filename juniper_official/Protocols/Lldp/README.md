# HealthBot Lldp KPI rules and playbooks

## Lldp playbooks
### Playbook name: lldp-kpis-playbook 
		> Description: "Playbook checks health of each lldp session and notify anomalies"
		> Synopsis: "LLDP session statistics KPI playbook"
		> Playbook file name: lldp-session-stats.playbook
		> Detals:
		 Playbook contains multiple rules which checks the health of system and
		 notifies when anomalies are found.
		 1) Rule "check-lldp-session-statistics" detects the LLDP session satistics threshold
		    breaches and notify anomalies.
		 2) Rule "get-lldp-state" collects the LLDP neighbor state.
		    and notify anomalies.
		 3) Rule "check-lldp-session" refers neighbor state information from rule
		    "get-lld-state" and detects the LLDP neighbor session state changes and
		    notify anomalies.

## Lldp rules

### Rule name: get-lldp-state 
		> Description: "Collects lldp session state periodically"
		> Synopsis: "LLDP neighbor state collector"
		> Rule file name: lldp-session-state.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5110;
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;
			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects LLDP (session) state changes and notifies when anomalies are found.
		 One input control detection
		
		   1) if-name, is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
### Rule name: check-lldp-session-statistics 
		> Description: "Collects LLDP session statistics(frame& TLV discards, frame-in&out errors and unknown TLVs) periodically and notify anomaly when breaches threshold"
		> Synopsis: "LLDP session statistics analyzer"
		> Rule file name: lldp-session-statistics.rule

		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: EX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ PTX5000 PTX1000 PTX10000 ];
			> Supported platforms: [ QFX10000 QFX5200 ];
			> Supported platforms: QFX5110;
			> Supported platforms: QFX5100;
			> Supported platforms: QFX5120-48Y;
			> Supported platforms: EX9200;
			> Supported platforms: EX4650;
			> Supported platforms: EX4600;

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects LLDP (session) state changes and notifies when anomalies are found.
		 Six inputs control detection
		
		   1) "if-name" is a regular expression that matches the
		      interfaces that you would like to monitor.  By default it's
		      '.*', which matches all interfaces. Use something like 'ge.*' to
		      match only gigabit ethernet interfaces.
		   2) "frame-discards-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 1. This rule will set a dashboard
		      color to red when LLDP frame discards are greater than
		      'frame-discards-threshold' for 3 minutes period, otherwise color is set
		      to green.
		   3) "frame-error-in-threshold" is the threshold that causes the rule to
		      report an anomaly. By default it's 1. This rule will set a dashboard
		      color to red when LLDP frame in errors are greater than
		      'frame-error-in-threshold' for 3 minutes period, otherwise color is set
		      to green.
		   4) "frame-error-out-threshold"is the threshold that causes the rule to
		      report an anomaly. By default it's 1. This rule will set a dashboard
		      color to red when LLDP frame out errors are greater than
		      'frame-error-out-threshold' for 3 minutes period, otherwise color is
		      set to green.
		   5) "tlv-discards-threshold" is the threshold that causes the rule to report
		      an anomaly. By default it's 1. This rule will set a dashboard color
		      to red when TLV discards are greater than 'tlv-discards-threshold'
		       for 3 minutes period, otherwise color is set to green.
		   6) "unknown-tlvs-threshold" is the threshold that causes the rule to report
		      an anomaly. By default it's 1. This rule will set a dashboard color to
		      red when unknown TLV count is greater than 'unknown-tlvs-threshold'
		      for 3 minutes period, otherwise color is set to green.
