# HealthBot CFM KPI rules and playbooks

## CFM playbooks
### Playbook name: cfm-delay-statistics-playbook 
		> Description: "Device playbook to monitor CFM delay"

		> Playbook file name: cfm-delay-statistics.playbook
		> Details:
		 Playbook monitor CFM average and max delay statistics and notify in
		 case delay is more than static threshold limit
		
		 1) Rule check-cfm-delay-statistics-netconf, monitor average, max delay and notifies
		    anomalies when delay exceeds static thresholds.

## CFM rules

### Rule name: check-cfm-delay-statistics-netconf 
		> Description: "Monitors CFM average and max delay to configured destination"
		> Synopsis: "cfm delay statistics KPI"
		> Rule file name: check-cfm-delay-statistics.rule
		> Sensor type: sensor cfm_iAgent 
		> Supported HealthBot version: 4.0.0
		> Supported product:MX, Platforms:A, Junos:18.1R1


		> Helper files: cfm.yml;
		> More details:
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
		 Minimum sample configuration required in Junos MX configuration
		 set interfaces ge-0/3/9 description "Connect to lab-asr9k10-02 gi0/0/1/19"
		 set interfaces ge-0/3/9 unit 0 family inet address 10.3.19.1/30
		 set protocols oam ethernet connectivity-fault-management performance-monitoring enhanced-sla-iterator
		 set protocols oam ethernet connectivity-fault-management performance-monitoring measurement-interval 5
		 set protocols oam ethernet connectivity-fault-management performance-monitoring sla-iterator-profiles PCORE measurement-type two-way-delay
		 set protocols oam ethernet connectivity-fault-management performance-monitoring sla-iterator-profiles PCORE measurement-interval 5
		 set protocols oam ethernet connectivity-fault-management maintenance-domain PCORE level 0
		 set protocols oam ethernet connectivity-fault-management maintenance-domain PCORE maintenance-association PCORE continuity-check interval 100ms
		 set protocols oam ethernet connectivity-fault-management maintenance-domain PCORE maintenance-association PCORE mep 100 interface ge-0/3/9
		 set protocols oam ethernet connectivity-fault-management maintenance-domain PCORE maintenance-association PCORE mep 100 remote-mep 101 sla-iterator-profile PCORE
