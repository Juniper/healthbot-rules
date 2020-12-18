# HealthBot Vcenter KPI rules and playbooks

## Vcenter playbooks
### Playbook name: vcenter-evpn-host-mapping 


		> Playbook file name: vcenter-evpn-host-mapping.playbook
		> Detals:
		 Collects vm host information from vcenter
		 Rule get-vcenter-details, collects ESXi host name, VM name, VM mac-address,
		 VM IP, datacenter name, cluster name from vcenter.
		 Collects vm host name from EVPN nodes and map with vcenter ESXi host name,
		 VM name, VM mac-address and shows path in dashboard
		 Rule check-vcenter-host-mac-mapping, Collects vm host name and outgoing
		 interface using LLDP and map with vcenter ESXi host name, VM name, VM
		 mac-address and shows path in dashboard

## Vcenter rules

### Rule name: check-vcenter-host-mac-mapping 
		> Description: "Collects datacenter VMs information from vcenter and LLDP information from routers then maps \"ESXi-VM-IP-MAC-Leaf Node-Egress Interface\" path by referring rule vmware/get-vcenter-details"
		> Synopsis: "VM path finder in EVPN"
		> Rule file name: check-vcenter-host-mac-mapping.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: [ get_vcenter_details.py LldpNbrStatsTable.yml ];
		> Supported healthbot version: 3.2.0
		> Detals:
		 Collects vm host information from EVPN nodes and maps with vcenter ESXi host
		 by querying database of rule vcenter.evpn/get-vcenter-details and displays entire
		 path in dashboard.
		 Four input controls detection
		
		   1) db-server-ip, user need to enter HB DB server ip while deploying
		      playbook.
		   2) db-port, user need to enter HB DB server udp port while deploying
		      playbook.
		   3) vcenter-device-group, user need to enter vcenter device group name
		      i.e. where playbook "get-vsphere-details" deployed.
		   4) vcenter-device, user need to enter vcenter device name which should
		      be part of device group.
### Rule name: get-vcenter-details 
		> Description: "Collects datacenter VMs information from Vmware Vcenter Vsphere"
		> Synopsis: "Vcenter VMs data collector"
		> Rule file name: get-vcenter-details.rule


		> Helper files: [ split_fqdn.py vsphere_hb.py vsphere_hb.yml ];
		> Supported healthbot version: 3.2.0
		> Detals:
		 Collects ESXi hosts information i.e. VM names, VM IPs, VM mac-addresses,
		 datacenter names and cluster names from vmware vsphere vcenter.
