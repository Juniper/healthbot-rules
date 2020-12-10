from __future__ import division
'''
This function returns used% out of total available
'''
def split_fqdn(host, **kwargs):
    return host.split('.')[0]
    