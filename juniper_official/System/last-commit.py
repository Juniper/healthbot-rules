import time

def check_commit_time(datetime, **kwargs):
    curr_time = kwargs['point_time']
    print(curr_time)
    print(datetime)
    date_time = datetime.replace(' UTC','')
    print(date_time)
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    print(epoch)
    timediff = (curr_time - epoch) / 60
    print(timediff)
    return timediff


