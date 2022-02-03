# HealthBot Sflow KPI rules and playbooks

## Sflow playbooks
### Playbook name: Sflow-Mac-Address-Playbook 
		> Description: "The playbook has Sflow rule to identify the traffic based on source/destination mac-addresses"
		> Synopsis: "Sflow analyzer"
		> Playbook file name: Sflow-Mac-Address.playbook
		> Details:
		 Playbook contains a rule which uses sflow to sample traffic and notifies
		 anomalies when sflow traffic rate exceeds threshold value.
		
		 1) Rule check-mac-traffic-tagged, Checks traffic based on mac addresses
		    and notifies anomaly when traffic rate is above threshold.
		 2) Rule check-mac-traffic-untagged, Checks traffic based on mac addresses
		    and notifies anomaly when traffic rate is above threshold.
### Playbook name: Sflow-TCP-Port-Playbook 
		> Description: "The playbook has some Sflow rules to identify the traffic based on their TCP ports."
		> Synopsis: "Sflow analyzer"
		> Playbook file name: Sflow-TCP-Port.playbook
		> Details:
		 Playbook contains a rule which uses sflow to sample traffic and notifies
		 anomalies when sflow traffic rate exceeds threshold value.
		
		 1) Rule check-tcp-traffic-tagged, Check tagged traffic based on TCP port
		    and notifies anomaly when traffic rate is above threshold.
		 2) Rule check-tcp-traffic-untagged, Check untagged traffic based on TCP port
		    and notifies anomaly when traffic rate is above threshold.
### Playbook name: Sflow-Ingest-Playbook 
		> Description: "The playbook has some Sflow rules to identify the traffic based on UDP ports."
		> Synopsis: "Sflow analyzer"
		> Playbook file name: Sflow-UDP-Port.playbook
		> Details:
		 Playbook contains a rule which uses sflow to sample traffic and notifies
		 anomalies when sflow traffic rate exceeds threshold value.
		 1) Rule check-udp-traffic-tagged, Check traffic based on UDP port
		    and notifies anomaly when tagged traffic rate is above threshold.
		 2) Rule check-udp-traffic-untagged, Check traffic based on UDP port
		    and notifies anomaly when untagged traffic rate is above threshold.

## Sflow rules

### Rule name: check-mac-traffic-tagged 
		> Description: "Check traffic based on mac addresses"
		> Synopsis: "sflow KPI"
		> Rule file name: check-mac-traffic-tagged.rule
		> Sensor type: sflow 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
		 Monitors traffic by sampling using sflow ingest and notifies anomaly when
		 traffic rate from source mac addresses is above threshold.
		 Variable inputs controls detection
		
		   1) high-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 800mBps (in Bytes). This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'highthreshold', otherwise color is set to green.
		   2) low-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 500mBps (in Bytes). This rule will set a
		      dashboard color to yellow when traffic rate is greater than
		      'lowthreshold', otherwise color is set to green.
### Rule name: check-mac-traffic-untagged 
		> Description: "Check traffic based on mac addresses"
		> Synopsis: "sflow KPI"
		> Rule file name: check-mac-traffic-untagged.rule
		> Sensor type: sflow 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
		 Monitors traffic by sampling using sflow ingest and notifies anomaly when
		 traffic rate from source mac addresses is above threshold.
		 Variable inputs controls detection
		
		   1) high-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 800mBps (in Bytes). This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'highthreshold', otherwise color is set to green.
		   2) low-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 500mBps (in Bytes). This rule will set a
		      dashboard color to yellow when traffic rate is greater than
		      'lowthreshold', otherwise color is set to green.
### Rule name: check-tcp-traffic-tagged 
		> Description: "Rule to check the tcp traffic in the Sflow sample"
		> Synopsis: "sflow KPI"
		> Rule file name: check-tcp-traffic-tagged.rule
		> Sensor type: sflow 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
		 Monitors traffic by sampling using sflow ingest and notifies anomaly when
		 TCP tagged traffic rate is above threshold.
		 Variable inputs controls detection
		
		   1) high-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 800mBps (in Bytes). This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'highthreshold', otherwise color is set to green.
		   2) low-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 500mBps (in Bytes). This rule will set a
		      dashboard color to yellow when traffic rate is greater than
		      'lowthreshold', otherwise color is set to green.
### Rule name: check-tcp-traffic-untagged 
		> Description: "Rule to check the tcp traffic in the Sflow sample"
		> Synopsis: "sflow KPI"
		> Rule file name: check-tcp-traffic-untagged.rule
		> Sensor type: sflow 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
		 Monitors traffic by sampling using sflow ingest and notifies anomaly when
		 TCP traffic rate is above threshold.
		 Variable inputs controls detection
		
		   1) high-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 800mbps. This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'highthreshold', otherwise color is set to green.
		   2) low-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 500mbps. This rule will set a
		      dashboard color to yellow when traffic rate is greater than
		      'lowthreshold', otherwise color is set to green.
### Rule name: check-udp-traffic-tagged 
		> Description: "Rule to check the udp traffic in the Sflow sample"
		> Synopsis: "sflow KPI"
		> Rule file name: check-udp-traffic-tagged.rule
		> Sensor type: sflow 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
		 Monitors traffic by sampling using sflow ingest and notifies anomaly when
		 UDP traffic rate is above threshold.
		 Variable inputs controls detection
		
		   1) high-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 800mBps (in Bytes). This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'highthreshold', otherwise color is set to green.
		   2) low-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 500mBps (in Bytes). This rule will set a
		      dashboard color to yellow when traffic rate is greater than
		      'lowthreshold', otherwise color is set to green.
### Rule name: check-udp-traffic-untagged 
		> Description: "Rule to check the udp traffic in the Sflow sample"
		> Synopsis: "sflow KPI"
		> Rule file name: check-udp-traffic-untagged.rule
		> Sensor type: sflow 
		> Supported HealthBot version: 3.0.0
		> Supported product:MX, Platforms:MX240, Junos:16.1R1
		> Supported product:MX, Platforms:MX480, Junos:16.1R1
		> Supported product:MX, Platforms:MX960, Junos:16.1R1
		> Supported product:MX, Platforms:MX2010, Junos:16.1R1
		> Supported product:MX, Platforms:MX2020, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX10000, Junos:16.1R1
		> Supported product:QFX, Platforms:QFX5200, Junos:16.1R1



		> More details:
		 Monitors traffic by sampling using sflow ingest and notifies anomaly when
		 UDP traffic rate is above threshold.
		 Variable inputs controls detection
		
		   1) high-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 800mBps (in Bytes). This rule will set a
		      dashboard color to red when traffic rate is greater than
		      'highthreshold', otherwise color is set to green.
		   2) low-threshold variable, is the threshold that causes the rule
		      to report an anomaly. By default it's 500mBps (in Bytes). This rule will set a
		      dashboard color to yellow when traffic rate is greater than
		      'lowthreshold', otherwise color is set to green.
