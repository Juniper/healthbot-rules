# HealthBot Nexus KPI rules and playbooks

## Nexus playbooks

## Nexus rules

### Rule name: check-nexus-interface-stats-netconf 
		> Description: "Monitors and notify interface statistics i.e. link state, input errors and  output errors"
		> Synopsis: "Interface statistics analyzer"
		> Rule file name: check-nexus-interface-stats-netconf.rule


		> Helper files: CiscoNexusInterfaceTable.yml;

		> Detals:
### Rule name: check-nexus-temperature-netconf 
		> Description: "Monitors the chassis temperatures of chassis"
		> Synopsis: "Chassis environment analyzer"
		> Rule file name: check-nexus-temperature-netconf.rule


		> Helper files: CiscoNexusEnvironmentTemperatureTable.yml;

		> Detals:
		 Detects chassis temperature threshold breaches and notifies when anomalies
		 are found.
### Rule name: check-nexus-fan-netconf 
		> Description: "Monitors the chassis fan status and notifies anomalies"
		> Synopsis: "Chassis environment analyzer\""
		> Rule file name: check-nexus-fan-netconf.rule


		> Helper files: [ CiscoNexusEnvironmentFanTable.yml cisco_nxos_show_environment_fan.textfsm];

		> Detals:
		 Monitors chassis fan health status and notifies when anomalies are found.
