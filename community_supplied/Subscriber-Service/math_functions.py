'''
math_functions.py - This library contains methods for simple math functions:

    deviationPercent()  - This function produces a float percent of the difference between a supplied base and new value
    
'''

'''-----------------------------------------------------------------------------
    deviationPercent() - This function produces a float percent of the difference between a supplied base and new value
    
    Input: 
         base - Name of address pool
         newValue - count of addresses used in pool
    Output:
         A float percent of the difference between a supplied base and new value
-----------------------------------------------------------------------------'''
def deviationPercent(base, newValue, **kwargs):
    if base == 0.0:
        return 0.0
    else:
        return 100*(abs(float(base)-float(newValue))/float(base))
