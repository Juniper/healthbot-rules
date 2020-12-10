# HealthBot Vcenter KPI rules and playbooks

## Vcenter playbooks
### Playbook name: vsphere-host-mac-mapping 


		> Playbook file name: vsphere-host-mac-mapping.playbook
		> Detals:
		 Collects vm host information from vcenter
		 Rule get-vsphere-details, collects ESXi host name, VM name, VM mac-address,
		 VM IP, datacenter name, cluster name from vcenter.
		 Collects vm host name from EVPN nodes and map with vcenter ESXi host name,
		 VM name, VM mac-address and shows path in dashboard
		 Rule check-vsphere-host-mac-mapping, Collects vm host name and outgoing
		 interface using LLDP and map with vcenter ESXi host name, VM name, VM
		 mac-address and shows path in dashboard

## EVPN VXLAN rules

### Rule name: get-vsphere-details 
		> Description: "Collects datacenter VMs information from Vmware Vcenter Vsphere  "
		> Synopsis: "Vcenter VMs data collector"
		> Rule file name: get_vsphere_details.rule


		> Helper files: [ split_fqdn.py vsphere_hb.py vsphere_hb.yml ];

		> Detals:
		 Collects ESXi hosts information i.e. VM names, VM IPs, VM mac-addresses,
		 datacenter names and cluster names from vmware vsphere vcenter.
### Rule name: check-vsphere-host-mac-mapping 
		> Description: "Collects datacenter VMs information from Vsphere  and LLDP information from routers and maps \"ESXi-VM-IP-MAC-Leaf Node-Egress Interface\" path by referring rule vmware/get-vsphere-details"
		> Synopsis: "VM path finder in EVPN"
		> Rule file name: check-vsphere-host-mac-mapping.rule

		> Supported products: QFX 

			> Supported platforms: All;
		> Helper files: [ get_vsphere_details.py LldpNbrStatsTable.yml ];

		> Detals:
		 Collects vm host information from EVPN nodes and maps with vcenter ESXi host
		 by querying database of rule vcenter.evpn/get-vsphere-details and displays entire
		 path in dashboard.
		 Four input controls detection
		
		   1) db-server-ip, user need to enter HB DB server ip while deploying
		      playbook.
		   2) db-port, user need to enter HB DB server udp port while deploying
		      playbook.
		   3) vsphere-device-group, user need to enter vcenter device group name
		      i.e. where playbook "get-vsphere-details" deployed.
		   4) vsphere-device, user need to enter vcenter device name which should
		      be part of device group.
