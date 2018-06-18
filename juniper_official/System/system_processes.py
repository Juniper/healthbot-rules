from __future__ import division
'''
This function isExceeding returns 'True' if % of size used out of reserved memory is not exceeding the threshold
'''
def isExceeding(size,res,threshold):
	if size.endswith('M'):
		size = size[:-1]
		size = int(size)
		size = size * 1024
	else:
		size = size[:-1]
                size = int(size)
	if res.endswith('M'):
                res = res[:-1]
                res = int(res)
                res = res * 1024
        else:
                res = res[:-1]
                res = int(res)
	if (res/size)*100 <= threshold :
		return True
	else:
		return False