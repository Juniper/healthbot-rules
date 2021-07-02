def threshold_adjustment(threshold, highlow, **kwargs):
    if (threshold <= -10000) or (threshold == 0):
        output = highlow
    else:
        output = threshold
    return output
