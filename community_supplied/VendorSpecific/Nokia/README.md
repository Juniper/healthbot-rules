# HealthBot Nokia KPI rules and playbooks

## Nokia playbooks

## Nokia rules

### Rule name: fib.statistics_check-nokia-fib-netconf
		> Description: "Monitors FIB statistics per line card"
		> Synopsis: "Monitors FIB statistics per line card"
		> Rule file name: fib.statistics_check-nokia-fib-netconf.rule
		> Helper files: [ NokiaFibOccupancyRateTable.yml alcatel_sros_show_router_fib_all_summary.textfsm ];

### Rule name: vpls-instances_check-total-vpls
		> Description: "Monior the total VPLS instances threshold"
		> Synopsis: "Monior the total VPLS instances threshold"
		> Rule file name: vpls-instances_check-total-vpls.rule
		> Helper files: [ NokiaServiceUsingVPLSTable.yml alcatel_sros_show_service_service-using_vpls.textfsm ];


### Rule name: vprn-instances_check-total-vprn
		> Description: "Monior the total VPRN instances threshold"
		> Synopsis: "Monior the total VPRN instances threshold"
		> Rule file name: vprn-instances_check-total-vprn.rule
		> Helper files: [ NokiaServiceUsingVPRNTable.yml alcatel_sros_show_service_service-using_vprn.textfsm ];