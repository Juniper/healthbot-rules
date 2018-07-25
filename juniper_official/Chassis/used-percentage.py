from __future__ import division
'''
This function returns used% out of total available
'''
def used_percentage(total, used, **kwargs):
        return int(float(used)/float(total)*100)
