# HealthBot CFM KPI rules and playbooks

## CFM playbooks
### Playbook name: cfm-delay-statistics-playbook 
		> Description: "Device playbook to monitor CFM delay"

		> Playbook file name: cfm-delay-statistics.playbook
		> Detals:
		 Playbook monitor CFM average and max delay statistics and notify in
		 case delay is more than static threshold limit
		
		 1) Rule check-cfm-delay-statistics-netconf, monitor average, max delay and notifies
		    anomalies when delay exceeds static thresholds.

## CFM rules

### Rule name: check-cfm-delay-statistics-netconf 


		> Rule file name: check-cfm-delay-statistics.rule

		> Supported products: MX 

			> Supported platforms: All;

		> Supported healthbot version: 4.0.0
		> Detals:
		 Monitors CFM average and max delay to configured destination and notifies anomalies
		 when average and max delay is above static thresholds.
		 Two inputs control detection:
		   1) maximum-delay-avg-threshold, is the threshold that causes the rule to report an
		      anomaly. By default it is 100000 micro seconds. This rule will set a
		      dashboard color to red when CFM average delay time is greater than static
		      threshold 'maximum-delay-avg-threshold-value'.
		   2) maximum-delay-max-threshold, is the threshold that causes the rule to report an
		      anomaly. By default it is 1000000 micro seconds. This rule will set a
		      dashboard color to red when CFM max delay time is greater than static
		      threshold 'maximum-delay-max-threshold-value'.
