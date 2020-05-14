# HealthBot System-blackhole-detection KPI rules and playbooks

## System-blackhole-detection playbooks
### Playbook name: system-blackhole-detection-playbook 
		> Description: "Playbook detects blackhole based on difference between input and output traffic and notifies anomalies"
		> Synopsis: "System blackhole detection key performance indicators"
		> Playbook file name: system-blackhole-detection.playbook
		> Detals:
		 Playbook monitor system total input and output packets usage and notify in
		 case difference in io traffic is above static and dynamic threshold
		
		 1) Rule check-system-traffic, monitor input and output traffic and notifies
		    anomalies io traffic difference exceeds dynamic and static thresholds.

## System-blackhole-detection rules

### Rule name: check-system-traffic 
		> Description: "Collects system total io packets and notifies in case of anomalies when io traffic difference is above static and dynamic threshold"
		> Synopsis: "system traffic statistics analyzer"
		> Rule file name: system-traffic.rule

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
		> Helper files: [ traffic_diff.py traffic-statistics.yml ];
		> Supported healthbot version: 1.0.1
		> Detals:
		 Checks system total input and output packets count periodically and
		 notifies anomaly when total input and output packets count is abnormal.
		 Two dynamic inputs control detection
		
		   1) traffic-diff-threshold, is the threshold that causes the rule to
		      report a anomaly. This rule will set a dashboard color to red when
		      system input($pfe-in-packets) and output ($pfe-out-packets)
		      traffic difference exceeds static threshold 'traffic-diff-threshold'.
		
