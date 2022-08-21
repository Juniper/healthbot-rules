'''
math_functions.py - This library contains methods for simple math functions:

    deviationPercent()  - This function produces a float percent of the difference between a supplied base and new value
    vector_sum() - This function produces sum of elements in List/Vector    
    absolute() - This function returns absolute value of a number
    
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
        

'''-----------------------------------------------------------------------------
    vector_sum() - This function produces sum of elements in List/Vector
    
    Input: 
         vector - vector/list
    Output:
         Sum of elements in List/Vector
-----------------------------------------------------------------------------'''


def vector_sum(vector, **kwargs):
    return sum(vector)

'''-----------------------------------------------------------------------------
    absolute() - This function returns absolute value of a number
    
    Input: 
         value - postive/negative number
    Output:
         Absolute value of a number passed
-----------------------------------------------------------------------------'''

def absolute(value, **kwargs):
    return abs(value)
