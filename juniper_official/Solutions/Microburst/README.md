# HealthBot Microburst KPI rules and playbooks

## Microburst playbooks
### Playbook name: microburst-open-config-playbook 
		> Description: "Playbook detects microbursts on interface egress queues using open-config qmon-sw sensor"
		> Synopsis: "Microburst detector"
		> Playbook file name: microburst-oc.playbook
		> Detals:
		 Detects microburst in all monitored interface egress queues using open-config
		 qmon-sw sensor.
		 Rule check-queue, detects microbursts and notfies anomalies.
### Playbook name: microburst-playbook 
		> Description: "Playbook detects microbursts on interface egress queues"
		> Synopsis: "Microburst detector"
		> Playbook file name: microburst.playbook
		> Detals:
		 Detects microburst in all monitored interface egress queues.
		 Rule check-queue, detects microbursts and notfies anomalies.

## Microburst rules

### Rule name: check-queue 
		> Description: "Collects all interfaces egress queues data using gpb sensor and detects microbursts"
		> Synopsis: " Microbust detector"
		> Rule file name: microburst.rule

		> Supported products: MX 

			> Supported platforms: [ MX240 MX480 MX960 MX2010 MX2020 ];

		> Supported healthbot version: 1.0.1
		> Detals:
		 Detects microburst in all monitored interface egress queues.
### Rule name: check-queue-oc 
		> Description: "Collects all interfaces egress queues data using open-config qmon-sw sensor and detects microbursts"
		> Synopsis: " Microbust detector"
		> Rule file name: microburst-oc.rule

		> Supported products: QFX 

			> Supported platforms: [ QFX5100 QFX5200 ];

		> Supported healthbot version: 2.1.1
		> Detals:
		 Detects microburst in all monitored interface egress queues.
