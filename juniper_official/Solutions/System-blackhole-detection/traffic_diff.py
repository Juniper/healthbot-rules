from __future__ import division
'''
This function returns used% out of total available
'''
def traffic_diff(inpkts, outpkts, **kwargs):
    inpkts = int(inpkts)
    outpkts = int(outpkts)
    if inpkts == 0:
        return 0
    res = (float(inpkts-outpkts)/inpkts)*100
    diff = abs(float(res))
    return diff
