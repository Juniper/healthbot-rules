from __future__ import division

def diff_percentage(max_count, min_count, **kwargs):
    difference_count = int(max_count) - int(min_count)
    if difference_count == 0:
         return 0
    variation = int(difference_count/int(min_count))*100
    return variation
