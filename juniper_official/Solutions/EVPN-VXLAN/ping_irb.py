import yamlordereddictloader
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import json
 
yaml_data = """
---
IrbPingTable:
    rpc: ping
    args:
        count: Null
        host: Null
        routing-instance: Null
    key: ../target-host
    item: probe-results-summary
    view: IrbPingView
IrbPingView:
    fields:
        host-ip: ../target-host
        probes-sent: probes-sent
        responses-received: responses-received
        packet-loss: packet-loss
        rtt-minimum: rtt-minimum
        rtt-maximum: rtt-maximum
        rtt-average: rtt-average
        rtt-stddev: rtt-stddev
"""
modules = FactoryLoader().load(yaml.load(yaml_data, Loader=yamlordereddictloader.Loader))
 
def run():
    data = __salt__['mine.get']('*', 'get_irb_data.get_irbs')
    self_dev = __salt__['grains.get']('id')
    self_dev_data = data[self_dev]
    req = []
    for dev, dev_data in data.items():
        if dev!= self_dev:
            for key, item in self_dev_data.items():
                if key in dev_data:
                    temp = dev_data[key]
                    args = {'count': '1', 'host': temp['ip_address'], 'routing-instance': temp['vrfname']}
                    stats = modules['IrbPingTable'](dev = __proxy__['junos.conn']())
                    stats.get(args=args)
                    data = json.loads(stats.to_json())
                    fields = data[temp['ip_address']]
                    fields['vrfname'] = temp['vrfname']
                    req.append({'fields': fields, 'tags': {'irb': key, 'remote_host': dev}})
    return req