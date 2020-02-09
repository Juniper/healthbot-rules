from __future__ import division
from __future__ import print_function
import requests
import pprint
import sys

'''
This function retrieves the cummulative packet_loss for this particular test (owner, test_name, device-group, device)
'''
def cumm_pkt_loss_from_db(owner, test_name, **kwargs):
    # device-group and device are extracted from kwargs


    dev_grp = kwargs['device_group']
    dev_id  = kwargs['device_id']
    db_name = dev_grp + ":" + dev_id
    url = "http://influxdb:8086/query"
    data_urlencode = "db=" + db_name + "&q=SELECT sum(\"packet_loss\") FROM \"rpm/probe-results\" WHERE \"owner\"='" + owner + "' AND \"test_name\"='" + test_name + "'"
    final_url = url + "?" + data_urlencode

    print("DEBUG DIOGO data: {}" .format(final_url), file=sys.stderr)
    response = requests.get(final_url)
    print("DEBUG DIOGO response", file=sys.stderr)
    pprint.pprint(response.text)

    # response content is something like below:
    #    {"results":[{"statement_id":0,"series":[{"name":"rpm/probe-results","columns":["time","sum"],"values":[["1970-01-01T00:00:00Z",36]]}]}]}

    # print(response.json()['results'][0]['series'][0]['values'][0][1])
    cumm_value = response.json()['results'][0]['series'][0]['values'][0][1]
    print("DEBUG DIOGO result = {}" .format(cumm_value), file=sys.stderr)

    return cumm_value