# HealthBot kernel-tcpip KPI rules and playbooks

## kernel-tcpip playbooks
### Playbook name: kernel-tcpip-playbook 
		> Description: "Playbook monitors the kernel-tcpip health i.e embryonic connection drop count and ddos attack count"
		> Synopsis: "Kernel tcpip key performance indicators"
		> Playbook file name: kernel-tcpip.playbook
		> Detals:
		 Playbook contains multiple rules which checks the health of kernel tcpip
		 and notifies when anomalies are found.
		 1) Rule "check-tcp-connection-drop-count" detects the TCP embryonic connection
		    drops and notifies the anomalies. Sensor type OpenConfig.
		 2) Rule "check-tcp-connection-drop-count-iagent" detects the TCP embryonic connection
		    drops and notifies the anomalies. Sensor type iAgent.
		 3) Rule "check-tcp-ddos-attack-count" detects the TCP ddos attack breaches
		    and notifies the anomalies. Sensor type OpenConfig.
		 4) Rule "check-tcp-ddos-attack-count-iagent" detects the TCP ddos attack breaches
		    and notifies the anomalies. Sensor type iAgent.



		> Playbook file name: nexthop-count-analyser.playbook
		> Detals:



		> Playbook file name: ndp-iri-cache-count-analyser.playbook
		> Detals:



		> Playbook file name: netisr-queue-analyser.playbook
		> Detals:



		> Playbook file name: arp-mgmt-cache-count-analyser.playbook
		> Detals:



		> Playbook file name: ndp-mgmt-cache-count-analyser.playbook
		> Detals:



		> Playbook file name: arp-iri-cache-count-analyser.playbook
		> Detals:



		> Playbook file name: clone-route-count-analyser.playbook
		> Detals:



		> Playbook file name: arp-public-cache-count-analyser.playbook
		> Detals:



		> Playbook file name: ndp-public-cache-count-analyser.playbook
		> Detals:

## kernel-tcpip rules

### Rule name: check-arp-cache-public-count-iagent 
		> Description: "This rule collects ARP public cache count and notify anomaly if drop count is increasing or if the count is reaching threshold"
		> Synopsis: "Check ARP public cache count"
		> Rule file name: check-arp-cache-public-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour ARP cache count on public interfaces.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name:-properties 
		> Description: "To monitor IP queue statistics in the system and report anomaly if it exceeds threshold size"
		> Synopsis: "IP queue statistics analyser in the system"
		> Rule file name: check-ip-queue-stats-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the IP queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name: check-tcp-ddos-attack-count-iagent 
		> Description: "Check whether the system is under TCP DDoS attack or not"
		> Synopsis: "Detect TCP DDoS Attack"
		> Rule file name: check-tcp-ddos-attack-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the TCP Distributed denial-of-service attack(DDoS) attack count in the system.
		 It shows RED alarm when the count is increased by minimum 1 from its previous value.
		 It's sampling time is 1 minute.
### Rule name:-properties 
		> Description: "To monitor IPv6 queue statistics in the system and report anomaly if it exceeds threshold size"
		> Synopsis: "IPv6 queue statistics analyser in the system"
		> Rule file name: check-ip6-queue-stats-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the IP6 queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name: check-arp-queue-stats 
		> Description: "To monitor ARP queue statistics in the system and report anomaly if it exceeds threshold size"
		> Synopsis: "ARP queue statistics analyser in the system"
		> Rule file name: check-arp-queue-stats.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the ARP queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name:-properties 
		> Description: "This rule monitors ether queue statistics and reports anomaly if it exceeds threshold"
		> Synopsis: "Check ether queue statistics in the system"
		> Rule file name: check-ether-queue-stats-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the ether queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name: check-ndp-cache-iri-count 
		> Description: "This rule monitors NDP IRI cache count and reports anomaly if it exceeds the threshold value"
		> Synopsis: "Check NDP IRI cache count"
		> Rule file name: check-ndp-cache-iri-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour NDP cache count on  IRI(internal routing interface).
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-tcp-connection-drop-count 
		> Description: "Check whether the TCP connection are getting dropped"
		> Synopsis: "Detect TCP embryonic connection drops"
		> Rule file name: check-tcp-connection-drop-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the TCP embryonic connection drop count in the system.
		 TCP embryonic connection is a half-open connection.
		 It shows YELLOW alarm when the count is increased by minimum 10 from its previous value.
		 It's sampling time is 1 minute.
### Rule name: check-arp-cache-mgmt-count 
		> Description: "This rule collects ARP management cache count and notify anomaly if drop count is increasing or if the count is reaching threshold"
		> Synopsis: "Check ARP management cache count"
		> Rule file name: check-arp-cache-mgmt-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour ARP cache count on management interface.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-ndp-cache-iri-count-iagent 
		> Description: "This rule monitors NDP IRI cache count and reports anomaly if it exceeds the threshold value"
		> Synopsis: "Check NDP IRI cache count"
		> Rule file name: check-ndp-cache-iri-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour NDP cache count on  IRI(internal routing interface).
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-tcp-ddos-attack-count 
		> Description: "Check whether the system is under TCP DDoS attack or not"
		> Synopsis: "Detect TCP DDoS Attack"
		> Rule file name: check-tcp-ddos-attack-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the TCP Distributed denial-of-service attack(DDoS) attack count in the system.
		 It shows RED alarm when the count is increased by minimum 1 from its previous value.
		 It's sampling time is 1 minute.
### Rule name: check-public-nh-count 
		> Description: "This rule monitors the  public nexthop count and reports anomaly when it exceeds threshold"
		> Synopsis: "To check the count of public nexthops."
		> Rule file name: check-public-nh-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the public nexthop count in the system.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count.
		 It's sampling time is 1 minute.
### Rule name: check-ether-queue-stats 
		> Description: "This rule monitors ether queue statistics and reports anomaly if it exceeds threshold"
		> Synopsis: "Check ether queue statistics in the system"
		> Rule file name: check-ether-queue-stats.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the ether queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name: check-arp-cache-iri-count 
		> Description: "This rule collects ARP IRI cache count and notify anomaly if drop count is increasing or if the count is reaching threshold"
		> Synopsis: "To check ARP IRI cache count in the system"
		> Rule file name: check-arp-cache-iri-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour ARP cache count on IRI(Internal routing interface).
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It's sampling time is 1 minute.
### Rule name: check-tcp-connection-drop-count-iagent 
		> Description: "Check whether the TCP connection are getting dropped"
		> Synopsis: "Detect TCP embryonic connection drops"
		> Rule file name: check-tcp-connection-drop-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the TCP embryonic connection drop count in the system.
		 TCP embryonic connection is a half-open connection.
		 It shows YELLOW alarm when the count is increased by minimum 10 from its previous value.
		 It's sampling time is 1 minute.
### Rule name: check-ndp-cache-public-count 
		> Description: "This rule monitors NDP public cache count and reports anomaly if it exceeds the threshold value"
		> Synopsis: "Check NDP public cache count "
		> Rule file name: check-ndp-cache-public-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour NDP cache count on  public interfaces.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-clone-route-count-iagent 
		> Description: "This rule monitors clone route count and reports anomaly if it exceeds threshold"
		> Synopsis: "Check clone route"
		> Rule file name: check-clone-route-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the clone route count in the system.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count.
		 It's sampling time is 1 minute.
### Rule name: check-ndp-cache-mgmt-count-iagent 
		> Description: "Check NDP management cache count"
		> Synopsis: "Check NDP management cache count "
		> Rule file name: check-ndp-cache-mgmt-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour NDP cache count on management interface.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-arp-cache-iri-count-iagent 
		> Description: "This rule collects ARP IRI cache count and notify anomaly if drop count is increasing or if the count is reaching threshold"
		> Synopsis: "Check ARP IRI cache count"
		> Rule file name: check-arp-cache-iri-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour ARP cache count on IRI(Internal routing interface).
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-ndp-cache-mgmt-count 
		> Description: "This rule monitors NDP management cache count and reports anomaly if it exceeds the threshold value"
		> Synopsis: "Check NDP management cache count"
		> Rule file name: check-ndp-cache-mgmt-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour NDP cache count on management interface.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-ndp-cache-public-count-iagent 
		> Description: "This rule monitors NDP public cache count and reports anomaly if it exceeds the threshold value"
		> Synopsis: "Check NDP public cache count"
		> Rule file name: check-ndp-cache-public-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour NDP cache count on  public interfaces.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-ip-queue-stats 
		> Description: "To monitor IP queue statistics in the system and report anomaly if it exceeds threshold size"
		> Synopsis: "IP queue statistics analyser in the system"
		> Rule file name: check-ip-queue-stats.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the IP queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name: check-ip6-queue-stats 
		> Description: "To monitor IPv6 queue statistics in the system and report anomaly if it exceeds threshold size"
		> Synopsis: "IPv6 queue statistics analyser in the system"
		> Rule file name: check-ip6-queue-stats.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the IP6 queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name: check-clone-route-count 
		> Description: "This rule monitors clone route count and reports anomaly if it exceeds threshold"
		> Synopsis: "Check clone routes count in the system"
		> Rule file name: check-clone-route-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the clone route count in the system.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count.
		 It's sampling time is 1 minute.
### Rule name:-properties 
		> Description: "To monitor ARP queue statistics in the system and report anomaly if it exceeds threshold size"
		> Synopsis: "ARP queue statistics analyser in the system"
		> Rule file name: check-arp-queue-stats-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the ARP queue statistics in the system.
		 It shows yellow alarm when the difference between packet queued and packet handled exceeds 95 percent of the queue size.
		 It shows red alarm if there is an increase in drop count.
		 It's sampling time is 30 seconds.
### Rule name: check-arp-cache-mgmt-count-iagent 
		> Description: "This rule collects ARP management cache count and notify anomaly if drop count is increasing or if the count is reaching threshold"
		> Synopsis: "Check ARP management cache count"
		> Rule file name: check-arp-cache-mgmt-count-iagent.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour ARP cache count on management interface.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
### Rule name: check-private-nh-count 
		> Description: "This rule monitors the  private nexthop count and reports anomaly when it exceeds threshold"
		> Synopsis: "To check the count of private nexthops"
		> Rule file name: check-private-nh-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the private nexthop count in the system.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count.
		 It's sampling time is 1 minute.
### Rule name: check-arp-cache-public-count 
		> Description: "This rule collects ARP public cache count and notify anomaly if drop count is increasing or if the count is reaching threshold"
		> Synopsis: "Check ARP public cache count"
		> Rule file name: check-arp-cache-public-count.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: PTX 

			> Supported platforms: [ EX9200 EX9251 EX9253 ];
			> Supported platforms: [ MX2010 MX2020 MX240 MX480 MX960 VMX ];
			> Supported platforms: PTX-Series-All;

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks for the neighbour ARP cache count on public interfaces.
		 It shows yellow alarm when the count exceeds 90 percent of the maximum count.
		 It shows red alarm when the count exceeds 95 percent of the maximum count or if there is an increase in drop count.
		 It's sampling time is 1 minute.
