# HealthBot Subscriber-Service KPI rules and playbooks

## Subscriber-Service playbooks
### Playbook name: subscriber-services 
		> Description: "The subscriber-services playbook contains rules for monitoring the health subscriber services KPI"
		> Synopsis: "Subscriber services KPI"
		> Playbook file name: subscriber-service.playbook
		> Detals:
		 Playbook contains multiple rules which checks the health of BRAS system
		 and notifies when anomalies are found.
		
		 1) Rule pppoe-error-statistics, detects the PPPoE error statistics
		    and notifies anomalies.
		 2) Rule chk-addr-pool-util, detects the system pool utilization
		    and notifies anomalies.
		 3) Rule linked-address-pool, detects the system linked pool utilization
		    and notifies anomalies.
		 4) Rule monitor-subscriber-count, detects the system total subscribers
		    count and notifies anomalies .

## Subscriber-Service rules

### Rule name: linked-address-pool 
		> Description: "Monitors linked address pool usage percentage and notifies anomalies"
		> Synopsis: "linked address pool utilization analyzer"
		> Rule file name: address-pool-utilization.rule

		> Supported products: MX 
		> Supported products: MX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];
			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];

		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: monitor-subscriber-count 
		> Description: "This rule collects total subscribers and notifies in case of anomalies"
		> Synopsis: "subscribers count statistics analyzer"
		> Rule file name: monitor-subscriber-count.rule

		> Supported products: MX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];

		> Supported healthbot version: 1.0.1
		> Detals:
### Rule name: pppoe-error-statistics 
		> Description: "Collects the PPPoE error periodically and notifies in case of anomalies"
		> Synopsis: "Monitors PPPoE error statistics"
		> Rule file name: pppoe-error-statistics.rule

		> Supported products: MX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];

		> Supported healthbot version: 1.0.1
		> Detals:
