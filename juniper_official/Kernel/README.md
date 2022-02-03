# HealthBot Kernel KPI rules and playbooks

## Kernel playbooks
### Playbook name: kernel-infra-playbook 
		> Description: "This playbooks encapsulates all the junos kernel(ifstate, peer-infra,rtsock) rules which keeps a check on junos-kernel parameters"
		> Synopsis: "Junos-Kernel infra parameters"
		> Playbook file name: kernel-infra-playbook.playbook
		> Details:
### Playbook name: kernel-tcp-ip-playbook 
		> Description: "This playbook encapsulates rules related to kernel tcp ip parameters"
		> Synopsis: "Kernel tcp ip parameters"
		> Playbook file name: kernel-tcp-ip-playbook.playbook
		> Details:
### Playbook name: krt-statistics-kpis 


		> Playbook file name: krt-statistics-kpis.playbook
		> Details:
		 This playbook is used to detect KRT Async queue stuck condition and raise alarm.
		
		 Following are the set of commands and the corresponding RPCs used to detect the problematic state.
		
		 labroot@jtac-mx960> show krt state | display xml rpc
		 <rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.2I0/junos">
		     <rpc>
		         <get-krt-state>
		         </get-krt-state>
		     </rpc>
		     <cli>
		         <banner></banner>
		     </cli>
		 </rpc-reply>
		
		 labroot@jtac-ptx10001-20c-proto-r2001> show krt async io statistics | display xml rpc
		 <rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.2I0/junos">
		     <rpc>
		         <get-async-io-stats>
		         </get-async-io-stats>
		     </rpc>
		     <cli>
		         <banner></banner>
		     </cli>
		 </rpc-reply>
		
		 labroot@jtac-ptx10001-20c-proto-r2001> show krt async correlator statistics | display xml rpc
		 <rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.2I0/junos">
		     <rpc>
		         <get-async-cor-stats>
		         </get-async-cor-stats>
		     </rpc>
		     <cli>
		         <banner></banner>
		     </cli>
		 </rpc-reply>
		
		 labroot@jtac-mx960> show krt state | display xml
		 <rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.2I0/junos">
		     <krt-state-information>
		         <krt-options>IndirectPFE IndirectChangeACK</krt-options>
		         <krt-install-job-not-running/>
		         <krt-queue-state>
		             <krtq-operations-queued>0</krtq-operations-queued>
		             <krtq-rt-table-adds>0</krtq-rt-table-adds>
		             <krtq-interface-routes>0</krtq-interface-routes>
		             <krtq-high-multicast-adds-changes>0</krtq-high-multicast-adds-changes>
		             <krtq-top-indirect-adds-changes>0</krtq-top-indirect-adds-changes>
		             <krtq-indirect-adds-changes>0</krtq-indirect-adds-changes>
		             <krtq-indirect-deletes>0</krtq-indirect-deletes>
		             <krtq-high-mpls-adds>0</krtq-high-mpls-adds>
		             <krtq-high-mpls-changes>0</krtq-high-mpls-changes>
		             <krtq-top-priority-adds>0</krtq-top-priority-adds>
		             <krtq-top-priority-changes>0</krtq-top-priority-changes>
		             <krtq-top-priority-deletes>0</krtq-top-priority-deletes>
		             <krtq-high-priority-adds>0</krtq-high-priority-adds>
		             <krtq-high-priority-changes>0</krtq-high-priority-changes>
		             <krtq-high-priority-deletes>0</krtq-high-priority-deletes>
		             <krtq-normal-priority-indirects>0</krtq-normal-priority-indirects>
		             <krtq-normal-priority-adds>0</krtq-normal-priority-adds>
		             <krtq-normal-priority-changes>0</krtq-normal-priority-changes>
		             <krtq-normal-priority-deletes>0</krtq-normal-priority-deletes>
		             <krtq-least-priority-adds>0</krtq-least-priority-adds>
		             <krtq-least-priority-changes>0</krtq-least-priority-changes>
		             <krtq-least-priority-deletes>0</krtq-least-priority-deletes>
		             <krtq-normal-priority-cnh-deletes>0</krtq-normal-priority-cnh-deletes>
		             <krtq-normal-priority-gmp>0</krtq-normal-priority-gmp>
		             <krtq-rt-table-deletes>0</krtq-rt-table-deletes>
		             <krtq-operations-deferred>0</krtq-operations-deferred>
		             <krtq-operations-canceled>0</krtq-operations-canceled>
		             <krtq-async-count>0</krtq-async-count>
		             <krtq-async-non-q-count>0</krtq-async-non-q-count>
		             <krtq-time-until-next-run>0</krtq-time-until-next-run>
		             <krtq-kernel-rt-learnt>44</krtq-kernel-rt-learnt>
		         </krt-queue-state>
		         <rtsock-time-until-next-scan>38</rtsock-time-until-next-scan>
		     </krt-state-information>
		     <cli>
		         <banner></banner>
		     </cli>
		 </rpc-reply>
		
		 labroot@jtac-mx960> show krt async io statistics | display xml
		 <rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.2I0/junos">
		     <krt-io-statistics xmlns="http://xml.juniper.net/junos/18.2I0/junos-routing">
		         <krt-io-statistics-entry>
		             <krt-io-task-name>KRT IO task</krt-io-task-name>
		             <krt-io-write-count>64</krt-io-write-count>
		             <krt-io-read-count>28</krt-io-read-count>
		         </krt-io-statistics-entry>
		         <krt-io-statistics-entry>
		             <krt-io-task-name>KStat</krt-io-task-name>
		         </krt-io-statistics-entry>
		         <krt-io-statistics-entry>
		             <krt-io-task-name>krt unsolic client</krt-io-task-name>
		         </krt-io-statistics-entry>
		         <krt-io-statistics-entry>
		             <krt-io-task-name>krt solic client JUNOS</krt-io-task-name>
		         </krt-io-statistics-entry>
		     </krt-io-statistics>
		     <cli>
		         <banner></banner>
		     </cli>
		 </rpc-reply>
		
		 labroot@jtac-mx960> show krt async correlator statistics | display xml
		 <rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.2I0/junos">
		     <krt-correlator-statistics junos:style="brief">
		         <krt-tree-statistics>
		             <krt-tree-insert-count>73</krt-tree-insert-count>
		             <krt-tree-delete-count>73</krt-tree-delete-count>
		             <krt-tree-lookup-count>264</krt-tree-lookup-count>
		             <krt-tree-current-count>0</krt-tree-current-count>
		         </krt-tree-statistics>
		     </krt-correlator-statistics>
		     <cli>
		         <banner></banner>
		     </cli>
		 </rpc-reply>
		
		
		 Any one of the following conditions becoming true will cause the alarms to be set to indicate KRT ASYNC stuck condition and user can perform any recovery actions accordingly.
		
		 Polling of the parameters that are part of the commands needed to detect the stuck condition is done every minute and internal databases are populated.
		
		 First Condition :
		 -----------------
		 Previous && Current values of "krtq-operations-queued" is not zero 
		 Previous && Current values of "krtq-async-count" is not zero &&
		 Previous && Current values of "krt-io-write-count" are same
		 then declare KRT stuck/Raise Red Alarm
		
		 (or)
		
		 Second Condition :
		 ------------------
		 "krt-tree-insert-count" is greater than "krt-tree-delete-count" &&
		 Previous and Current values of "krt-tree-delete-count" are same
		 then declare KRT stuck/Raise Red Alarm
		
		 (or)
		
		 Third Condition:
		 ----------------
		 Current value of "krtq-async-count" is greater than 0 and lessthan/equal to 20000 &&
		 Previous value of "krtq-async-count" is greater than 0 and lessthan/equal to 20000 &&
		 Current value of "krtq-async-count" is greater than/equal to previous value of "krtq-async-count" &&
		 Current value of "krt-tree-current-count" is greater than 0 and lessthan/equal to 20000 &&
		 Previous value of "krt-tree-current-count" is greater than 0 and lessthan/equal to 20000 &&
		 Current value of "krt-tree-current-count" is greater than/equal to previous value of "krt-tree-current-count"
		 then declare KRT stuck/Raise Red Alarm

## Kernel rules

### Rule name: check-client-limit-reached 
		> Description: "Monitor the number of Ifstate based routing sockets opened by application"
		> Synopsis: "Client limit reached KPI"
		> Rule file name: check-client-limit-reached.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1



		> More details:
		 This rule checks if any application has opened more than the allowed number
		 of Ifstate based routing sockets.
### Rule name: check-dead-ifstate-client 
		> Description: "Monitors if there are any dead ifstate clients that are not cleaned up"
		> Synopsis: "Dead ifstate client KPI"
		> Rule file name: check-dead-ifstate-client.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1



		> More details:
		 This rule checks if there are any dead ifstate clients not cleaned up in the
		 system for the last 20 minutes.
		 By default, it checks if all the samples collected every 1 minute are
		 non-zero for contiguous 20 minutes.
### Rule name: check-delayed-unrefs-anomaly-iagent 
		> Description: "Monitor delayed unrefs on the system"
		> Synopsis: "Delayed unref anomaly using iagent sensor"
		> Rule file name: check-delayed-unrefs-anomaly-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1


		> Helper files: delayed_unref.yml;
		> More details:
		 This rule checks if there are any delayed unrefs and if they are greater than
		 a particular threshold (sysctl net.rt_nh_max_delayed_unrefs).
		 Transient spikes in delayed unref count is expected in certain catastrophic or
		 major events and is not a cause for worry. But, if this situation persists for
		 significant amount of time (say in minutes), then it can result in traffic loss.
### Rule name: check-delayed-unrefs-anomaly 
		> Description: "Monitor delayed unrefs on the system"
		> Synopsis: "Delayed unref anomaly using open-config sensor"
		> Rule file name: check-delayed-unrefs-anomaly.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1



		> More details:
		 This rule checks if there are any delayed unrefs and if they are greater than
		 a particular threshold (sysctl net.rt_nh_max_delayed_unrefs).
		 Transient spikes in delayed unref count is expected in certain catastrophic or
		 major events and is not a cause for worry. But, if this situation persists for
		 significant amount of time (say in minutes), then it can result in traffic loss.
### Rule name: check-iri-conn-keepalive-dropped 
		> Description: "This rule detects any intra-chassis connection drops because of keep alive expiry"
		> Synopsis: "Detect IRI connection drops because of Keepalive"
		> Rule file name: check-iri-conn-keepalive-dropped.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1


		> Helper files: tcpconn.yml;
		> More details:
		 This rule detects any intra-chassis connection (part of Internal Routing
		 Instance) drops because of keep alive expiry.
### Rule name: check-krt-ack-timeouts 
		> Description: "This rule collects kernel route and next-hop acknowledgement statistics  periodically and notifies anomaly in case of timeout"
		> Synopsis: "Kernel route and next-hop acknowledgements statistics analyzer "
		> Rule file name: check-krt-ack-timeouts.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.0.1
		> Supported product:MX, Platforms:A, Junos:15.1R1


		> Helper files: krt-ack-stats.yml;
		> More details:
		 This rule collects kernel route and next-hop acknowledgement statistics  periodically
		 and notifies anomaly in case of timeout.
		 One input controls detection
		
		  1) error-threshold variable, Number of timeout increase between metrics, before
		     anomaly is reported.
### Rule name: check-krt-tx-bulk-msg-fail 
		> Description: "Collect KRT bulking statistics and notifies when message fail count increases"
		> Synopsis: "KRT bulking statistics analyzer"
		> Rule file name: check-krt-tx-bulk-msg-fail.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.0.1
		> Supported product:MX, Platforms:A, Junos:15.1R1


		> Helper files: krt-tx-bulk-stats.yml;
		> More details:
		 This rule collects KRT bulking statistics and notifies when message fail count increases.
		 One input controls detection
		 1) error-threshold variable, Number of timeout increase between metrics, before
		    anomaly is reported.
### Rule name: check-pfeman-conn-drops 
		> Description: "Monitors if Peer infra module replicates FIB states to the line cards and processes incoming IPCs from them"
		> Synopsis: "pfeman connection drops KPI"
		> Rule file name: check-pfeman-conn-drops.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1



		> More details:
		 Peer infra module is responsible for replicating FIB states to the line cards
		 and also to process incoming IPCs from them. Each line card has a connection
		 with Master Routing Engine Junos Kernel.
		 This rule monitors and ungraceful connection drops in these pfeman connections.
### Rule name: check-spurious-ppt-wkups 
		> Description: "Monitors if peer proxy kernel thread gets woken up spuriously"
		> Synopsis: "spurious ppt wkups KPI"
		> Rule file name: check-spurious-ppt-wkups.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1



		> More details:
		 Peer infra module is responsible for replicating FIB states to the line cards
		 and also to process incoming IPCs from them. Each line card has a connection
		 with Master Routing Engine Junos Kernel, and a peer proxy kernel thread
		 represents this remote line card in the Junos Kernel.
		 If the peer proxy kernel thread gets woken up spuriously (i.e. without any
		 pending events to be processed), it can result in performance issues and
		 should thus be monitored. This rule does exactly that.
### Rule name: check-stuck-ifstate-clients-iagent 
		> Description: "iagent rule to monitor any stuck ifstate client on a network device"
		> Synopsis: "Stuck ifstate client"
		> Rule file name: check-stuck-ifstate-clients-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:15.1R1
		> Supported product:EX, Platforms:EX9251, Junos:15.1R1
		> Supported product:EX, Platforms:EX9253, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1
		> Supported product:MX, Platforms:VMX, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1


		> Helper files: fetch_stuck_client.yml;
		> More details:
		 This rule checks if there are any stuck ifstate clients present in the system.
		 Though rare, but when any Ifstate client (application/FPC peer) gets stuck,
		 it can result in resource accumulation and eventually can lead to traffic loss.
		 It checks if the "slow peers" alarm has been raised on the device.
### Rule name: check-stuck-ifstate-clients 
		> Description: "Open-config rule to monitor any stuck ifstate client on a network device"
		> Synopsis: "Stuck ifstate client"
		> Rule file name: check-stuck-ifstate-clients.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1



		> More details:
		 This rule checks if there are any stuck ifstate clients present in the system.
		 A stuck Ifstate client can cause resource release issues and eventually lead to
		 Kernel to veto incoming routing socket messages from applications, which further
		 can result in traffic loss. Though very rare, if this happens, it is a serious
		 condition and should be mitigated asap by restarting the client. See readme
		 in healthbot rules folder for details.
### Rule name: check-too-many-dead-ifstates-iagent 
		> Description: "Monitor number of dead and alive ifstates on the network device"
		> Synopsis: "Number of dead/alive ifstates"
		> Rule file name: check-too-many-dead-ifstates-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:15.1R1
		> Supported product:EX, Platforms:EX9251, Junos:15.1R1
		> Supported product:EX, Platforms:EX9253, Junos:15.1R1
		> Supported product:MX, Platforms:MX240, Junos:15.1R1
		> Supported product:MX, Platforms:MX480, Junos:15.1R1
		> Supported product:MX, Platforms:MX960, Junos:15.1R1
		> Supported product:MX, Platforms:MX2010, Junos:15.1R1
		> Supported product:MX, Platforms:MX2020, Junos:15.1R1
		> Supported product:MX, Platforms:VMX, Junos:15.1R1
		> Supported product:PTX, Platforms:A, Junos:15.1R1


		> Helper files: deadalive.yml;
		> More details:
		 This rule checks for the number of dead ifstates at any given time in
		 the system. A dead Ifstate gets garbage collected once all the consumers
		 see the corresponding delete message. If these dead ifstates continue to
		 pile up, this indicates a garbage collection problem and can eat up
		 significant resources such as memory and indices.
		 This rule monitors the number of dead Ifstates and raises an alarm if there
		 are too many of these (> 50% of alive ifstates) detected for significant
		 duration of time (1 hour).
### Rule name: check-too-many-dead-ifstates 
		> Description: "Monitor number of dead and alive ifstates on the network device"
		> Synopsis: "Number of dead/alive ifstates"
		> Rule file name: check-too-many-dead-ifstates.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 2.1.0
		> Supported product:EX, Platforms:EX9200, Junos:19.1R1
		> Supported product:EX, Platforms:EX9251, Junos:19.1R1
		> Supported product:EX, Platforms:EX9253, Junos:19.1R1
		> Supported product:MX, Platforms:MX240, Junos:19.1R1
		> Supported product:MX, Platforms:MX480, Junos:19.1R1
		> Supported product:MX, Platforms:MX960, Junos:19.1R1
		> Supported product:MX, Platforms:MX2010, Junos:19.1R1
		> Supported product:MX, Platforms:MX2020, Junos:19.1R1
		> Supported product:MX, Platforms:VMX, Junos:19.1R1
		> Supported product:PTX, Platforms:A, Junos:19.1R1



		> More details:
		 This rule checks for the number of dead ifstates at any given time in
		 the system. A dead Ifstate gets garbage collected once all the consumers
		 see the corresponding delete message. If these dead ifstates continue to
		 pile up, this indicates a garbage collection problem and can eat up
		 significant resources such as memory and indices.
		 This rule monitors the number of dead Ifstates and raises an alarm if there
		 are too many of these (> 50% of alive ifstates) detected for significant
		 duration of time (1 hour).
### Rule name: detect-routing-socket-errors-iagent 
		> Description: "Detect errors in rtsock, veto and mproc layers"
		> Synopsis: "Detect Routing Socket errors in the system"
		> Rule file name: detect-routing-socket-errors-iagent.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX9200, Junos:18.3R3
		> Supported product:EX, Platforms:EX9251, Junos:18.3R3
		> Supported product:EX, Platforms:EX9253, Junos:18.3R3
		> Supported product:MX, Platforms:MX240, Junos:18.3R3
		> Supported product:MX, Platforms:MX480, Junos:18.3R3
		> Supported product:MX, Platforms:MX960, Junos:18.3R3
		> Supported product:MX, Platforms:MX2010, Junos:18.3R3
		> Supported product:MX, Platforms:MX2020, Junos:18.3R3
		> Supported product:MX, Platforms:VMX, Junos:18.3R3
		> Supported product:PTX, Platforms:A, Junos:18.3R3


		> Helper files: rtsock-error-count.yml;
		> More details:
		 This rule checks for the total number of routing socket errors at any given time in the system.
		 Routing socket errors includes errors returned from rtsock, veto and mproc layers.
		 It monitors the total number of routing socket errors and raises an alarm if there are too many of
		 these detected for significant duration of time.
		 This rule checks if the error has benn increased by 100 from its previous value in ALL the samples
		 for the last 70 or 130 seconds and raises the alarm accordingly.
		 One input controls detection
		
		  1) rtsock-error-count-threshold-input variable, is the RTSOCK Error count threshold value.
		     Default value is 100.
### Rule name: detect-routing-socket-errors 
		> Description: "Detect errors in rtsock, veto and mproc layers"
		> Synopsis: "Detect Routing Socket errors in the system"
		> Rule file name: detect-routing-socket-errors.rule
		> Sensor type: open-config 
		> Supported HealthBot version: 1.0.1
		> Supported product:EX, Platforms:EX9200, Junos:19.3R1
		> Supported product:EX, Platforms:EX9251, Junos:19.3R1
		> Supported product:EX, Platforms:EX9253, Junos:19.3R1
		> Supported product:MX, Platforms:MX240, Junos:19.3R1
		> Supported product:MX, Platforms:MX480, Junos:19.3R1
		> Supported product:MX, Platforms:MX960, Junos:19.3R1
		> Supported product:MX, Platforms:MX2010, Junos:19.3R1
		> Supported product:MX, Platforms:MX2020, Junos:19.3R1
		> Supported product:MX, Platforms:VMX, Junos:19.3R1
		> Supported product:PTX, Platforms:A, Junos:19.3R1



		> More details:
		 This rule checks for the total number of routing socket errors at any given time in the system.
		 Routing socket errors includes errors returned from rtsock, veto and mproc layers.
		 It monitors the total number of routing socket errors and raises an alarm if there are too many of
		 these detected for significant duration of time.
		
		 This rule checks if the error has been increased by 100 from its previous value in ALL the samples
		 for the last 70 or 130 seconds and raises the alarm accordingly.
		 One input controls detection
		
		  1) rtsock-error-count-threshold-input variable, is the RTSOCK Error count threshold value.
		     Default value is 100.
### Rule name: check-krt-state 
		> Description: "Collects kernel state fields stats"
		> Synopsis: "KRT Statistics"
		> Rule file name: krtasync.rule
		> Sensor type: iAgent 




		> More details:
		    These rules collect and monitor if kernel is stuck by checking the different
		    fields like krt-tree-current-count,krt-tree-delete-count,krtq-async-count
		    write-count,krtq-operations-queued,etc.
