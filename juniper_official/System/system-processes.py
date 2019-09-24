from __future__ import division
'''
This function isExceeding returns 'True' if % of size used out of resident memory is exceeding the threshold
'''
def isExceeding(size,res,threshold, **kwargs):
        if size.endswith('M'):
            size = size[:-1]
            size = int(size)
            size = size * 1024
        elif size.endswith('G'):
            size = size[:-1]
            size = int(size)
            size = size * 1024*1024
        else:
            size = size[:-1]
            size = int(size)
        print(size)
        if res.endswith('M'):
            res = res[:-1]
            res = int(res)
            res = res * 1024
        elif res.endswith('G'):
            res = res[:-1]
            res = int(res)
            res = res * 1024*1024
        else:
            res = res[:-1]
            res = int(res)
        print(res)
        if (res/size)*100 >= threshold :
            return True
        else:
            return False
