#specify vsphere IP 
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import atexit
import ssl
from junossecure.junos_secure import junos_decode

def getVMinfoFromVimVM(item):
    vm = {"tags":{}, 
          "fields": {}}
    name = item.name
    print("vm name", item.name)
    ip = "None"
    mac = "None"
    if item.summary.guest != None:
        ip = item.summary.guest.ipAddress
        print("ip", ip)
    if item.config != None:
        #print("########vm config name######")
        #print(vm.config)
        #print("########end of vm config######")
        for device in item.config.hardware.device:
            #print("########device######")
            #print(type(device))
            #print(device)
            #print("########end of device######")
            if hasattr(device, 'macAddress'):
                mac = device.macAddress
                print("mac", mac)
    vm["tags"]["name"] = name
    vm["fields"]["ip"] = ip
    vm["fields"]["mac"] = mac
    return vm

def getListOfVMFromVimFolder(item):
    vm_list = []
    if hasattr(item, 'childEntity'):
        hosts = item.childEntity
        #print("hosts", hosts)
        for host in hosts:
            print("host ", host)
            print("host name", host.name)
            if isinstance(host, vim.ClusterComputeResource):
                vm_list_from_cluster = getListOfVMFromVimCluster(host)
                vm_list = vm_list + vm_list_from_cluster
            elif isinstance(host, vim.ComputeResource):
                hosts2 = host.host
                print("host2.host", host.host)
                for host2 in hosts2:
                    host_name = host2.name
                    #print("host2",host2, host2.name)
                    print("vm", host2.vm)
                    vm2 = host2.vm
                    for vm in vm2:
                        vm = getVMinfoFromVimVM(vm)
                        #vm["fields"]["cluster"] = "none"
                        vm["fields"]["host"] = host_name
                        vm_list.append(vm)
    return vm_list  

def getListOfVMFromVimCluster(item):
    vm_list = []
    print("cluster type")
    print("cluster", item)
    print("cluster name", item.name)
    cluster_name = item.name
    #if hasattr(cluster, 'childEntity'):
    hosts = item.host
    print("hosts", hosts)
    for host in hosts:
        host_name = host.name
        print("host ", host.name)
        #hosts2 = host.host
        vms = host.vm
        for vm in vms:
            vm = getVMinfoFromVimVM(vm)
            vm["fields"]["cluster"] = cluster_name
            vm["fields"]["host"] = host_name
            vm_list.append(vm)
    return vm_list  


def run():

    host = __pillar__["proxy"]["vcenter"]
    user= __pillar__["proxy"]["username"]
    pwd = junos_decode(__pillar__["proxy"]["encoded_password"])
    port = __pillar__["proxy"]["port"]

    context = None
    if hasattr(ssl, '_create_unverified_context'):
       context = ssl._create_unverified_context()
    si = __salt__["vsphere.get_service_instance_via_proxy"]()

#    si = SmartConnect(host=host,
#                      user=user,
#                      pwd=pwd,
#                      port=port,
#                      sslContext=context)

    if not si:
        print("Could not connect to the specified host using specified "
              "username and password")
        return -1

    atexit.register(Disconnect, si)
    content = si.RetrieveContent()
    datacenter_view = content.viewManager.CreateContainerView(content.rootFolder, 
                                                                     [vim.Datacenter], 
                                                                     True)
    datacenters = datacenter_view.view

    vm_list = []

    for datacenter in datacenters:
        print("datacenter", datacenter)
        if hasattr(datacenter.hostFolder, 'childEntity'):
            items = datacenter.hostFolder.childEntity
            datacenter_name = datacenter.name
            #print(datacenter.hostFolder.childEntity)
            for item in items:   
                if isinstance(item, vim.Folder):
                    vm_list_from_vim_folder = getListOfVMFromVimFolder(item)
                    #print("############## folder", item.name)
                    for vm in vm_list_from_vim_folder:
                        vm["fields"]["datacenter"] = datacenter_name
                    vm_list = vm_list + vm_list_from_vim_folder
                if isinstance(item, vim.ClusterComputeResource):
                    vm_list_from_cluster = getListOfVMFromVimCluster(item)
                    #print("############## cluster", item.name)
                    for vm in vm_list_from_cluster:
                        vm["fields"]["datacenter"] = datacenter_name
                    vm_list = vm_list + vm_list_from_cluster

    #for vm in vm_list: print(vm)
    return vm_list