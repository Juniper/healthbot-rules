# HealthBot Microburst KPI rules and playbooks

## Microburst playbooks
### Playbook name: microburst-open-config-playbook 
		> Description: "Playbook detects microbursts on interface egress queues using open-config qmon-sw sensor"
		> Synopsis: "Microburst detector"
		> Playbook file name: microburst-oc.playbook
		> Details:
		 Detects microburst in all monitored interface egress queues using open-config
		 qmon-sw sensor.
		 Rule check-queue, detects microbursts and notfies anomalies.
### Playbook name: microburst-playbook 
		> Description: "Playbook detects microbursts on interface egress queues"
		> Synopsis: "Microburst detector"
		> Playbook file name: microburst.playbook
		> Details:
		 Detects microburst in all monitored interface egress queues.
		 Rule check-queue, detects microbursts and notfies anomalies.

## Microburst rules

### Rule name: check-queue-oc 
		> Description: "Collects all interfaces egress queues data using open-config qmon-sw sensor and detects microbursts"
		> Synopsis: " Microbust detector"
		> Rule file name: microburst-oc.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.1
		> Supported product:QFX, Platforms:QFX5100, Junos:18.2
		> Supported product:QFX, Platforms:QFX5200, Junos:18.2



		> More details:
		 Detects microburst in all monitored interface egress queues.
### Rule name: check-queue 
		> Description: "Collects all interfaces egress queues data using gpb sensor and detects microbursts"
		> Synopsis: " Microbust detector"
		> Rule file name: microburst.rule
		> Sensor type: native-gpb 
		> Supported HealthBot version: 1.0.1
		> Supported product:MX, Platforms:MX240, Junos:17.2
		> Supported product:MX, Platforms:MX480, Junos:17.2
		> Supported product:MX, Platforms:MX960, Junos:17.2
		> Supported product:MX, Platforms:MX2010, Junos:17.2
		> Supported product:MX, Platforms:MX2020, Junos:17.2



		> More details:
		 Detects microburst in all monitored interface egress queues.
