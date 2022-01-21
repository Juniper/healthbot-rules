# HealthBot Vcenter KPI rules and playbooks

## Vcenter playbooks
### Playbook name: vcenter-evpn-host-mapping 


		> Playbook file name: vcenter-evpn-host-mapping.playbook
		> Details:
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
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.2.0
		> Supported product:QFX, Platforms:A, Junos:18.1R1

		> Other vendor product support: vmware 
		> Helper files: [ get_vcenter_details.py LldpNbrStatsTable.yml ];
		> More details:
		 Collects vm host information from EVPN nodes and maps with vcenter ESXi host
		 by querying database of rule vcenter.evpn/get-vcenter-details and displays entire
		 path in dashboard.
		 This rule to work, users need to create tagging profile and apply to device group.
		 Tagging profile will create fields "vcenter-device" and "vcenter-device-group".
		 Below is a sample tagging profile
		 data-enrichment 
		    tagging-profile <tagging-profile-name> 
		        policy <tagging-policy-name> 
		            rules vcenter.evpn/check-vcenter-host-mac-mapping
		            term <term-name> 
		                then 
		                    add-field vcenter-device 
		                        value <vcenter device name which is part of vcenter-device-group>
		                        type string
		                        in-memory false
		                    }
		                    add-field vcenter-device-group 
		                        value <vcenter-device-group where playbook "get-vcenter-details" deployed>
		                        type string
		                        in-memory false
		                    }
		                }
		            }
		        }
		    }
		 }
### Rule name: get-vcenter-details 
		> Description: "Collects datacenter VMs information from Vmware Vcenter Vsphere"
		> Synopsis: "Vcenter VMs data collector"
		> Rule file name: get-vcenter-details.rule
		> Sensor type: iAgent 
		> Supported HealthBot version: 3.2.0

		> Other vendor product support: vmware 
		> Helper files: [ split_fqdn.py vsphere_hb.py vsphere_hb.yml ];
		> More details:
		 Collects ESXi hosts information i.e. VM names, VM IPs, VM mac-addresses,
		 datacenter names and cluster names from vmware vsphere vcenter.
