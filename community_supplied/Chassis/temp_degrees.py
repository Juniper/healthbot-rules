import re

def temp_degrees(temperature, **kwargs):
    temp = re.search(r'(\d+) deg.*',temperature)
    temp_value = int(temp.group(1))
    return temp_value