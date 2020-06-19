# HealthBot Icmp-outlier KPI rules and playbooks

## Icmp-outlier playbooks
### Playbook name: icmp-outlier 
		> Description: "Detects network group outlier w.r.t RTT average response across devices"
		> Synopsis: "ICMP outlier detector"
		> Playbook file name: icmp.playbook
		> Detals:

## Icmp-outlier rules

### Rule name: check-outlier 
		> Description: "Detects ICMP outlier response time and notify anomalies"
		> Synopsis: "ICMP outlier analyzer"
		> Rule file name: icmp.rule

		> Supported products: MX 
		> Supported products: MX 

			> Supported platforms: All;
			> Supported platforms: All;

		> Supported healthbot version: 2.0.0
		> Detals:
		 Sends ICMP probes to user specified destination host and notifies anomalies
		 when round trip time average response is above static or dynamic thresholds.
		 And also detects outlier across the devices in device group ML algorithms.
		 Three inputs control detection
		
		   1) host-var, is a destination IP or host name where ICMP probes send
		      periodically.
		   2) count-var, is a ICMP ping count. By default count is set to 1.
		   3) rtt-threshold-var, is the threshold that causes the rule to report an
		      anomaly. By default it is 1000 micro seconds. This rule will set a
		      dashboard color to red when ICMP response time is greater than static
		      threshold 'rtt-threshold-var'.
