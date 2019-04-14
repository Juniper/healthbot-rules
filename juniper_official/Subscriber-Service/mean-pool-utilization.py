from __future__ import division
'''
This function returns used% out of total available
'''
def mean_pool_utilization(list_pool_vector, **kwargs):
    utilization = 0
    if len(list_pool_vector) > 0:
         utilization = sum(list_pool_vector)/len(list_pool_vector)
    return utilization
