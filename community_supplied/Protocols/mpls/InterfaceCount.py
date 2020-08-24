Count=0
def count(intCount, **kwargs):
    global Count
    a=intCount.split(',')
    Count = len(a)
    return Count