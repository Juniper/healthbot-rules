import re

def get_spu_performace(performance_info, **kwargs):
    temp = re.search(r'30:.*(\d+).*31:', performance_info)
    temp_value = int(temp.group(1))
    return temp_value