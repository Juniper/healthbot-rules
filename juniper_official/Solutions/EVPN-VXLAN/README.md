# HealthBot EVPN-VXLAN KPI rules and playbooks

## EVPN-VXLAN playbooks
### Playbook name: spine-evpn-vxlan-kpis 
		> Description: "Playbook to check EVPN-VXLAN spine node health w.r.t. EVPN, VXLAN, Interfaces, VTEP, IRB, BFD"
		> Synopsis: "EVPN-VXLAN key performance indicators for spine node"
		> Playbook file name: spine-evpn-vxlan-kpis.playbook
		> Detals:
		 Playbook contains multiple rules which monitors Data Center Spine
		 nodes and notifies when anomalies are found.
		 1) Rule evpn-advertised-prefix.rule, detects the advertised route count
		    threshold breaches and notify anomalies.
		 2) Rule evpn-received-prefix.rule, detects the received route count
		    threshold breaches and notify anomalies.
		 3) Rule evpn-route-count.rule, detects the route count threshold
		    breaches and notify anomalies.
		 4) Rule evpn-mac-count.rule, detects the evpn mac count threshold
		    breaches and notify anomalies.
		 5) Rule bfd-session-state.rule, detects BFD session state change and
		    notifies anomalies when error count increases.
		 6) Rule vtep-interface-count.rule, detects the vtep interface  count
		    threshold breaches and notify anomalies.
		 7) Rule vtep-interface-status.rule, detects the vtep interface status
		    notify anomalies.
		 8) Rule vtep-interface-traffic.rule,monitors interface traffic and notifies
		 9) Rule vtep-interface-flap.rule, detects interface flaps and notifies
		    anomalies when link flap count increases.
		 10) Rule vtep-interface-error.rule, detects interface errors and notifies
		     anomalies when error count increases.
		 11) Rule vtep-tunnel-statistics.rule, detects logical interface statisticsr
		     and notifies anomalies when error count increases.
		 12) Rule irb-interface-status.rule, monitors irb interface and notify
		     anomaly when irb state is down
		 13) Rule irb-interface-traffic.rule,monitors interface traffic and notifies
		     anomalies when traffic exceeds threshold.
		 14) Rule irb-next-hops.rule, monitors irb interface next-hops and notifies
		     anomalies when exceeds threshold.
		 15) Rule interface-in-errors-iagent.rule, monitors interface input errors
		     and notifies anomalies when exceeds threshold.
		 16) Rule interface-out-errors-netconf.rule, monitors interface output errors
		     and notifies anomalies when exceeds threshold.
		 17) Rule interface-in-traffic-iagent.rule, monitors interface input traffic
		     and notifies anomalies when exceeds threshold.
		 18) Rule interface-out-traffic-iagent.rule, monitors interface output traffic
		     and notifies anomalies when exceeds threshold.
		 19) Rule interface-flaps-iagent.rule, monitors interface flaps and notifies
		     anomalies when exceeds threshold.
		 20) Rule interface-status-iagent.rule, monitors interface status and notifies
		     anomalies when exceeds threshold.
		 21) Rule bgp-neighbor-state-iagent.rule, monitors bgp state and notifies
		     anomaly when neighbor state is down.
		 22) Rule bgp-neighbor-flap-iagent.rule, monitors interface status and notifies
		     anomalies when exceeds threshold.
		 23) Rule vxlan-vport.rule, monitors vport count and notifies anomalies
		     when exceeds threshold.
		 24) Rule evpn-db-state-netconf.rule, Verify evpn database state has duplicate
		     mac entry, which is detected by same vlan and same Active-source
		 25) Rule verify-mac-ip-netconf.rule, collects dynamic MAC address using udf
		     and updates dependent rules sensor table
		 26) Rule check-remote-vtep-count-netconf.rule, Collects remote VTEP counts per
		     VLAN periodically and notifies less than expected
		 27) Rule evpn-vxlan-monitor-count-online-netconf.rule, Check NHCount on fpc
		     below threshold passed as argument, fpc is dynamically derived
		 28) Rule check-flabels-count-netconf.rule, collects flabels token count
		     periodically and notifies anomalies when flabels token count is above
		     static threshold
		 29) Rule check-mac-count-netconf.rule, monitors MAC count in ethernet switching
		     table periodically and notifies anomaly when MAC count is above threshold
		 NOTE: If you don't want to include any of the rule in the list, please create
		 new playbook and include only the required rules for your case.
### Playbook name: evpn-vxlan-kpis 
		> Description: "Playbook to check EVPN-VXLAN health w.r.t. EVPN, VXLAN, Interfaces, VTEP, IRB, BFD"
		> Synopsis: "EVPN-VXLAN key performance indicators"
		> Playbook file name: evpn-vxlan.playbook
		> Detals:
		 Playbook contains multiple rules which monitors Data Center Spine and Leaf
		 nodes and notifies when anomalies are found.
		 1) Rule evpn-advertised-prefix.rule, detects the advertised route count
		    threshold breaches and notify anomalies.
		 2) Rule evpn-received-prefix.rule, detects the received route count
		    threshold breaches and notify anomalies.
		 3) Rule evpn-route-count.rule, detects the route count threshold
		    breaches and notify anomalies.
		 4) Rule evpn-mac-count.rule, detects the evpn mac count threshold
		    breaches and notify anomalies.
		 5) Rule bfd-session-state.rule, detects BFD session state change and
		    notifies anomalies when error count increases.
		 6) Rule vtep-interface-count.rule, detects the vtep interface  count
		    threshold breaches and notify anomalies.
		 7) Rule vtep-interface-status.rule, detects the vtep interface status
		    notify anomalies.
		 8) Rule vtep-interface-traffic.rule,monitors interface traffic and notifies
		 9) Rule vtep-interface-flap.rule, detects interface flaps and notifies
		    anomalies when link flap count increases.
		 10) Rule vtep-interface-error.rule, detects interface errors and notifies
		     anomalies when error count increases.
		 11) Rule vtep-tunnel-statistics.rule, detects logical interface statisticsr
		     and notifies anomalies when error count increases.
		 12) Rule irb-interface-status.rule, monitors irb interface and notify
		     anomaly when irb state is down.
		 13) Rule irb-interface-traffic.rule,monitors interface traffic and notifies
		     anomalies when traffic exceeds threshold.
		 14) Rule irb-next-hops.rule, monitors irb interface next-hops and notifies
		     anomalies when exceeds threshold.
		 15) Rule interface-in-errors-iagent.rule, monitors interface input errors
		     and notifies anomalies when exceeds threshold.
		 16) Rule interface-out-errors-netconf.rule, monitors interface output errors
		     and notifies anomalies when exceeds threshold.
		 17) Rule interface-in-traffic-iagent.rule, monitors interface input traffic
		     and notifies anomalies when exceeds threshold.
		 18) Rule interface-out-traffic-iagent.rule, monitors interface output traffic
		     and notifies anomalies when exceeds threshold.
		 19) Rule interface-flaps-iagent.rule, monitors interface flaps and notifies
		     anomalies when exceeds threshold.
		 20) Rule interface-status-iagent.rule, monitors interface status and notifies
		     anomalies when exceeds threshold.
		 21) Rule bgp-neighbor-state-iagent.rule, monitors bgp state and notifies
		     anomaly when neighbor state is down.
		 22) Rule bgp-neighbor-flap-iagent.rule, monitors interface status and notifies
		     anomalies when exceeds threshold.
		 23) Rule vxlan-vport.rule, monitors vport count and notifies anomalies
		     when exceeds threshold.
		 24) Rule evpn-db-state-netconf.rule, Verify evpn database state has duplicate
		     mac entry, which is detected by same vlan and same Active-source
		 25) Rule verify-mac-ip-netconf.rule, collects dynamic MAC address using udf
		     and updates dependent rules sensor table
		 26) Rule check-remote-vtep-count-netconf.rule, Collects remote VTEP counts per
		     VLAN periodically and notifies less than expected
		 27) Rule evpn-vxlan-monitor-count-online-netconf.rule, Check NHCount on fpc
		     below threshold passed as argument, fpc is dynamically derived
		 28) Rule check-flabels-count-netconf.rule, collects flabels token count
		     periodically and notifies anomalies when flabels token count is above
		     static threshold
		 29) Rule check-mac-count-netconf.rule, monitors MAC count in ethernet switching
		     table periodically and notifies anomaly when MAC count is above threshold.
		 NOTE: If you don't want to include any of the rule in the list, please create
		 new playbook and include only the required rules for your case.
### Playbook name: evpn-irb-icmp-probe 
		> Description: "Playbook to check EVPN-VXLAN rvi reachability"
		> Synopsis: "EVPN-VXLAN rvi key performance indicators"
		> Playbook file name: evpn-irb-icmp-probe.playbook
		> Detals:
		 Playbook contains rule which monitors Data Center EVPN VXLAN
		 remote rvi and notifies when anomalies are found.
		 1) Rule check-rvi-reachability-netconf.rule, pings remote IRB interfaces
		    and notifies incase RVI is unreachable
		 NOTE: If you don't want to include any of the rule in the list, please create
		 new playbook and include only the required rules for your case.
### Playbook name: leaf-evpn-vxlan-kpis 
		> Description: "Playbook to check EVPN-VXLAN leaf node health w.r.t. EVPN, VXLAN, Interfaces, VTEP, IRB, BFD, STP, LACP"
		> Synopsis: "EVPN-VXLAN key performance indicators for leaf node"
		> Playbook file name: leaf-evpn-vxlan-kpis.playbook
		> Detals:
		 Playbook contains multiple rules which monitors Data Center Leaf
		 nodes and notifies when anomalies are found.
		 1) Rule evpn-advertised-prefix.rule, detects the advertised route count
		    threshold breaches and notify anomalies.
		 2) Rule evpn-received-prefix.rule, detects the received route count
		    threshold breaches and notify anomalies.
		 3) Rule evpn-route-count.rule, detects the route count threshold
		    breaches and notify anomalies.
		 4) Rule evpn-mac-count.rule, detects the evpn mac count threshold
		    breaches and notify anomalies.
		 5) Rule bfd-session-state.rule, detects BFD session state change and
		    notifies anomalies when error count increases.
		 6) Rule vtep-interface-count.rule, detects the vtep interface  count
		    threshold breaches and notify anomalies.
		 7) Rule vtep-interface-status.rule, detects the vtep interface status
		    notify anomalies.
		 8) Rule vtep-interface-traffic.rule,monitors interface traffic and notifies
		 9) Rule vtep-interface-flap.rule, detects interface flaps and notifies
		    anomalies when link flap count increases.
		 10) Rule vtep-interface-error.rule, detects interface errors and notifies
		     anomalies when error count increases.
		 11) Rule vtep-tunnel-statistics.rule, detects logical interface statisticsr
		     and notifies anomalies when error count increases.
		 12) Rule irb-interface-status.rule, monitors irb interface and notify
		     anomaly when irb state is down.
		 13) Rule irb-interface-traffic.rule,monitors interface traffic and notifies
		     anomalies when traffic exceeds threshold.
		 14) Rule irb-next-hops.rule, monitors irb interface next-hops and notifies
		     anomalies when exceeds threshold.
		 15) Rule interface-in-errors-iagent.rule, monitors interface input errors
		     and notifies anomalies when exceeds threshold.
		 16) Rule interface-out-errors-netconf.rule, monitors interface output errors
		     and notifies anomalies when exceeds threshold.
		 17) Rule interface-in-traffic-iagent.rule, monitors interface input traffic
		     and notifies anomalies when exceeds threshold.
		 18) Rule interface-out-traffic-iagent.rule, monitors interface output traffic
		     and notifies anomalies when exceeds threshold.
		 19) Rule interface-flaps-iagent.rule, monitors interface flaps and notifies
		     anomalies when exceeds threshold.
		 20) Rule interface-status-iagent.rule, monitors interface status and notifies
		     anomalies when exceeds threshold.
		 21) Rule bgp-neighbor-state-iagent.rule, monitors bgp state and notifies
		     anomaly when neighbor state is down.
		 22) Rule bgp-neighbor-flap-iagent.rule, monitors interface status and notifies
		     anomalies when exceeds threshold.
		 23) Rule vxlan-vport.rule, monitors vport count and notifies anomalies
		     when exceeds threshold.
		 24) Rule evpn-db-state-netconf.rule, Verify evpn database state has duplicate
		     mac entry, which is detected by same vlan and same Active-source
		 25) Rule verify-mac-ip-netconf.rule, collects dynamic MAC address using udf
		     and updates dependent rules sensor table
		 26) Rule check-remote-vtep-count-netconf.rule, Collects remote VTEP counts per
		     VLAN periodically and notifies less than expected
		 27) Rule evpn-vxlan-monitor-count-online-netconf.rule, Check NHCount on fpc
		     below threshold passed as argument, fpc is dynamically derived
		 28) Rule check-flabels-count-netconf.rule, collects flabels token count
		     periodically and notifies anomalies when flabels token count is above
		     static threshold
		 29) Rule check-mac-count-netconf.rule, monitors MAC count in ethernet switching
		     table periodically and notifies anomaly when MAC count is above threshold
		 30) Rule check-stp-state-netconf.rule, Monitors member vlan's STP state
		     periodically and notifies anomalies when stp is not in forwarding state
		 31) Rule check-df-correlation-netconf.rule, evpn esi desinated forwarder
		     information periodically and notifies anomaly when df id changes
		 32) Rule check-multihomed-state-netconf.rule, evpn multihome status periodically
		     and notifies anomaly when state if not forwarding
		 33) Rule check-lacp-state-netconf.rule, collects LACP interfaces status
		     periodically and notifies when distribution status is false
		 34) Rule check-bpdu-errors-netconf.rule, Collects aggregate ethernet BPDU
		     statistics and notify anomalies when error count increases
		 NOTE: If you don't want to include any of the rule in the list, please create
		 new playbook and include only the required rules for your case.

## EVPN-VXLAN rules

### Rule name: check-evpn-routes 
		> Description: "Collects active EVPN routes count periodically and displays the routes"
		> Synopsis: "Active EVPN  routes analyzer"
		> Rule file name: evpn-route-count.rule

		> Supported products: QFX 
		> Supported products: QFX 

			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: EvpnTable.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Detects total number of active routes in bgp.evpn.0  table and notifies
		 when anomalies are found.
		 inputs control detection
		   1) "route-count-variable"  is the threshold that causes the
		      rule to report an anomaly. By default it's 100. This rule will set
		      a dashboard color to red when received route count exceed threshold
### Rule name: check-vport 
		> Description: "This rule collects vport used percentage periodically and notifies in case of anomalies"
		> Synopsis: "vport analyzer"
		> Rule file name: vxlan-vport.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: [ subtract.py used-percentage.py vport.yml ];
		> Supported healthbot version: 2.1.0
		> Detals:
		   This rule monitors vports used percentage and notify in case any of the health monitored field crosses threshold
### Rule name: check-vtep-interface-flap 
		> Description: "Collects statistics periodically and notifies in case of any anomaly"
		> Synopsis: "VTEP interface statistics analyzer"
		> Rule file name: vtep-interface-flap.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: vtep-statistics.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors VTEP interface flaps and notifies when anomalies are found.
		 One inputs control detection
		   1) flaps-threshold, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the flap-increases are greater than
		      'flaps-threshold' for 180s. If it sees any flaps increase for a
		      period of less than 180s, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: check-evpn-advertised-prefix 
		> Description: "Collects BGP EVPN session advertised routes count periodically and notifies anomaly when advertised route count exceed threshold"
		> Synopsis: "BGP EVPN advertised routes analyzer"
		> Rule file name: evpn-advertised-prefix.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: bgp_neighbor.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Detects BGP neighbor advertised route count threshold breaches and notifies
		 when anomalies are found.
		 Two inputs control detection
		   1) "addr-table" is a regular expression that matches the BGP evpn table
		      that you would like to monitor.By default it's 'default-switch.evpn.0'
		   2) "max-route-threshold"  is the threshold that causes the
		      rule to report an anomaly. By default it's 10000. This rule will set
		      a dashboard color to red when advertised route count exceed threshold
### Rule name: check-vtep-interface-traffic 
		> Description: "Collects statistics periodically and notifies in case of any anomaly"
		> Synopsis: "VTEP interface statistics analyzer"
		> Rule file name: vtep-interface-traffic.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: vtep-statistics.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors VTEP interface interface input traffic, output traffic and
		 notifies when anomalies are found.
		 Two inputs control detection
		   1) high-threshold,  is the threshold that causes the rule to
		      report an anomaly.  By default it's 800000000 octets. This rule will
		      set a dashboard color to red when *all* the input traffic is above
		      threshold for 180 seconds period. Use 8000000000 octets for 10G &
		      80000000000 for 100G interface.
		   2) low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 500000000 octets . This rule will
		      set a dashboard color to yellow when *all* the input traffic is above
		      threshold for 180 seconds period, otherwise color is set to green.
		      Use 5000000000 octets for 10G & 50000000000 for 100G interface.
### Rule name: check-irb-next-hops 
		> Description: "This rule collects IRB next hop periodically and notifies in case of anomalies"
		> Synopsis: "IRB next hop analyzer"
		> Rule file name: irb-next-hops.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: [ IrbIntefaceStatsTable.yml generic_functions.py ];
		> Supported healthbot version: 2.1.0
		> Detals:
		   This rule monitors IRB next hop count and notify in case any of the health monitored field crosses threshold
### Rule name: check-irb-mac-count-netconf 
		> Description: "This rule collects IRB unique mac address count periodically and notifies in case of anomalies when mac count exceeds count 512"
		> Synopsis: " Irb unique mac identifier"
		> Rule file name: check-irb-mac-count-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: IrbMacTable.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Collects IRB unique MAC address count periodically and notifies anomalies
		 when MAC count is above static threshold.
		 One input controls detection
		
		   1) threshold variable, is the threshold that causes the rule to report an anomaly.
		      By default default it's 512. This rule will set a dashboard color to
		      red when mac address count is greater than token-threshold. Otherwise
		      color is set to green.
### Rule name: verify-duplicate-mac-netconf 
		> Description: "Verify evpn database state has duplicate mac entry"
		> Synopsis: "Rule to determine evpn database state has duplicate mac entry using iagent sensor uses command \"show evpn database state duplicate\", if command returns output then duplicate entries found and Red Alert. Health state will show grey which means no duplicate"
		> Rule file name: evpn-db-state-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: evpndbstate.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Rule 'verify-duplicate-mac' determine evpn database state has duplicate mac entry
		
		 One input controls detection
		  1) status variable, Enter state based on allowed/possible entries
		     Possible entries are default-gateway, pinned, static, duplicate.
### Rule name: check-mac-count-netconf 
		> Description: "This rule checks health of MAC count in ethernet switching table and notify in case any of the health monitored field crosses threshold"
		> Synopsis: "MAC count in ethernet switching table analyzer"
		> Rule file name: check-mac-count-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: mac-count.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		   This rule checks health of MAC count in ethernet switching table and notify in case any of the health monitored field crosses threshold
### Rule name: check-irb-status 
		> Description: "This rule collects IRB admin and operational status periodically and notifies in case of anomalies"
		> Synopsis: "IRB admin and operational status analyzer"
		> Rule file name: irb-interface-status.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: IrbIntefaceStatusTable.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		   This rule monitors IRB admin and operational status and notify in case any of any anomalies
### Rule name: check-evpn-received-prefix 
		> Description: "Collects BGP EVPN session received routes count periodically and notifies anomaly when received route count exceeds threshold"
		> Synopsis: "BGP EVPN received routes analyzer"
		> Rule file name: evpn-received-prefix.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: bgp_neighbor.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Detects BGP neighbor received route count threshold breaches and notifies
		 when anomalies are found.
		 Two inputs control detection
		   1) "addr-table" is a regular expression that matches the BGP evpn table
		      that you would like to monitor.By default it's 'default-switch.evpn.0'
		   2) "max-route-threshold"  is the threshold that causes the
		      rule to report an anomaly. By default it's 10000. This rule will set
		      a dashboard color to red when received route count exceeds threshold
### Rule name: check-remote-vtep-interfaces-netconf 
		> Description: "Monitor the remote VTEP interfaces for provided VLAN name"
		> Synopsis: "Monitor the remote VTEPs"
		> Rule file name: check-remote-vtep-count-netconf.rule

		> Supported products: QFX 
		> Supported products: QFX 

			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: vlantable.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Collects remote VTEP counts per VLAN and notifies anomalies when vtep count
		 is less than threshold
		 Two inputs control detection
		  1) vlan-name-variable, is the vlan name to monitor. By default monitors
		     all vlans. For specific vlan to monitor, provide the vlan name
		  2) remote-count-variable, is the minimum threshold value of remote
		     VTEP counts
### Rule name: check-bfd-session-state 
		> Description: "This rule collects bfd session state periodically and notifies in case of anomalies"
		> Synopsis: "bfd session state analyzer"
		> Rule file name: bfd-session-state.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 
		> Supported products: QFX 

			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: bfd-session-state.yml;
		> Supported healthbot version: 1.0.1
		> Detals:
		   This rule checks health of each bfd session state and notify in case any of the health monitored field crosses threshold
### Rule name: check-stp-state-netconf 
		> Description: "Monitors member vlan's STP state periodically and notifies in case of anomalies"
		> Synopsis: "STP state analyzer"
		> Rule file name: check-stp-state-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: vlan-member-stp-state.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Collects each member vlan STP state periodically and notifies anomalies
		 when STP state is discarding.
		 One input controls detection
		
		   1) input-vlan-id variable, is a regular expression that matches the vlan id that you would
		      like to monitor.  By default it's '.*', which matches all interfaces.
		      Use something like '100|107' to match only vlan IDs 100 and 107.
### Rule name: verify-mac-ip-netconf 
		> Description: "This rule retrieves IP address for dynamic MAC address and triggers an alert if IP address not present."
		> Synopsis: "This rule retrieves IP address for dynamic MAC address and triggers an alert if IP address not present."
		> Rule file name: verify-mac-ip-netconf.rule

		> Supported products: QFX 
		> Supported products: QFX 

			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: ethswitchevpnarp.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Retrieves IP address for dynamic MAC address and triggers an alert
		 if IP address not present
### Rule name: check-flabel-count-netconf 
		> Description: "Collects flabel token count periodically and notifies in case of anomalies"
		> Synopsis: "Flabel count analyzer"
		> Rule file name: check-flabels-count-netconf.rule

		> Supported products: QFX 

			> Supported platforms: QFX10k;
		> Helper files: flables.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Collects flabels token count periodically and notifies anomalies when flabels token
		 count is above static threshold.
		 One input controls detection
		
		   1) token-threshold variable, is the threshold that causes the rule to report an anomaly. By
		      default it's 94000. This rule will set a dashboard color to red when flabels token
		      count is greater than token-threshold. Otherwise color is set to green.
### Rule name: check-vport-count-netconf 
		> Description: "EVPN VXLAN Rules for leaf QFX5110/QFX5120/QFX5100"
		> Synopsis: "Check vport on fpc below threshold passed as argument, fpc is dynamically derived."
		> Rule file name: evpn-vxlan-monitor-count-online-netconf.rule

		> Supported products: QFX 
		> Supported products: QFX 

			> Supported platforms: QFX5k;
			> Supported platforms: QFX5k;
		> Helper files: evpn-vport.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Collects NHCount of fpc and notifies anomalies when NHCount is more then
		 provided threshold. Also check-vport-count monitor vport count and notifies
		 anomalies when vport count is more then provided threshold value.
		 One input controls detection
		  1) high-threshold-count variable, is the NHCount maximum threshold value.
### Rule name: check-irb-traffic 
		> Description: "This rule collects IRB input and output traffic periodically and notifies in case of anomalies"
		> Synopsis: "IRB input and output traffic analyzer"
		> Rule file name: irb-interface-traffic.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: IrbIntefaceTrafficTable.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		   This rule monitors IRB input and output traffic and notify in case any of the health monitored field crosses threshold
### Rule name: check-df-correlation-netconf 
		> Description: "Collects evpn esi desinated forwarder information periodically and notifies anomaly when df id changes"
		> Synopsis: "Evpn esi df correlator"
		> Rule file name: check-df-correlation-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: DfInfoTable.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 THis rule collects esi designated forwarder information periodically and
		 notifies anomalies when there is a change in DF ID.
### Rule name: check-bpdu-errors-netconf 
		> Description: "Collects aggregate ethernet BPDU statistics and notify anomalies when error count increases"
		> Synopsis: "BPDU error detector"
		> Rule file name: check-bpdu-errors-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: BpduStats.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Collects lacp statistics periodically and notifies anomalies when lacp
		 distribution status is false.
		 One input controls detection
		
		  1) ae-name variable, is the interface name to monitor. By default monitors all AE
		     interfaces. For specific interfaces to monitor, use regular expression
		     for e.g. ae1 or ae1|ae1.
### Rule name: check-vtep-interface-status 
		> Description: "Collects VTEP status periodically and notifies in case of any anomaly"
		> Synopsis: "VTEP interface status analyzer"
		> Rule file name: vtep-interface-status.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: vtep-statistics.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors VTEP interface admin status, operations status and
		 notifies when anomalies are found.
### Rule name: check-vtep-tunnel-statistics 
		> Description: "Collects statistics periodically and notifies in case of any anomaly"
		> Synopsis: "VTEP logical interface statistics analyzer"
		> Rule file name: vtep-tunnel-statistics.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: VtepCountTable.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors VTEP logical interface status, input traffic, output traffic and
		 notifies when anomalies are found.
		 Two inputs control detection
		   1) high-threshold,  is the threshold that causes the rule to
		      report an anomaly.  By default it's 800000000 octets. This rule will
		      set a dashboard color to red when *all* the input traffic is above
		      threshold for 180 seconds period. Use 8000000000 octets for 10G &
		      800000000 for 100G interface.
		   2) low-threshold, is the threshold that causes the rule to
		      report an anomaly.  By default it's 500000000 octets . This rule will
		      set a dashboard color to yellow when *all* the input traffic is above
		      threshold for 180 seconds period, otherwise color is set to green.
		      Use 5000000000 octets for 10G & 500000000 for 100G interface.
### Rule name: check-vtep-interface-errors 
		> Description: "Collects statistics periodically and notifies in case of any anomaly"
		> Synopsis: "VTEP interface statistics analyzer"
		> Rule file name: vtep-interface-error.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: vtep-statistics.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Monitors VTEP interface interface input errors, output errors and
		 notifies when anomalies are found.
		 inputs control detection
		   1) errors-threshold, is the threshold that causes the rule to report
		      an anomaly.  By default it's 1. This rule will set a dashboard
		      color to red when *all* the error increases are greater than
		      'errors-threshold-variable' for 180s. If it sees any errors increase for a
		      period of less than 180s, it'll turn the color to yellow,
		      otherwise color is set to green.
### Rule name: check-multihomed-state-netconf 
		> Description: "Collects evpn multihome status periodically and notifies anomaly when state if not forwarding"
		> Synopsis: "Evpn multihome status analyzer"
		> Rule file name: check-multihomed-state-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: EvpnMultihomedTable.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 This rule checks multi-home status of AE interfaces and notify in case
		 state is not forwarding
### Rule name: fetch-irb-data-netconf 
		> Description: "This rule collects al IRB interafce details of all routing instances.  And also maps local and remote devices data based on IRB, IP and routing instance"
		> Synopsis: "IRB collector"
		> Rule file name: check-rvi-reachability-netconf.rule

		> Supported products: QFX 
		> Supported products: QFX 

			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: get_irb_data.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Rule 'fetch-irb-data' collects IRB interface names, IP and routing-instance
		 name from all routers and maps remote router IRB details with local router.
		 Rule 'check-rvi-reachability' checks RVI reachability across the network and
		 notify in case any of the remote IRB interface IP is not reachable.
### Rule name: check-lacp-state-netconf 
		> Description: "Collects LACP interfaces status  periodically and notifies when distribution status is false"
		> Synopsis: "Lacp state analyzer"
		> Rule file name: check-lacp-state-netconf.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: lacp-statistcs.yml;
		> Supported healthbot version: 3.0.0
		> Detals:
		 Collects lacp statistics periodically and notifies anomalies when lacp
		 distribution status is false.
		 One input controls detection
		
		  1) ae-name variable, is the interface name to monitor. By default monitors all lacp
		     interfaces. For specific interfaces to monitor, use regular expression
		     for e.g. ae1 or ae1|ae1.
### Rule name: check-vtep-interface-count 
		> Description: "Collects VTEP interfaces count periodically and notifies anomaly when count exceed threshold"
		> Synopsis: "VTEP interface count analyzer"
		> Rule file name: vtep-interface-count.rule

		> Supported products: QFX 
		> Supported products: QFX 

			> Supported platforms: All;
			> Supported platforms: All;
		> Helper files: VtepCountTable.yml;
		> Supported healthbot version: 2.1.0
		> Detals:
		 Detects VTEP interfaces count and notifies when anomalies are found.
		 Input control detection
		   1) "vtep-count-static-threshold"  is the threshold that causes the
		      rule to report an anomaly. By default it's 10. This rule will set
		      a dashboard color to red when advertised route count exceed threshold
