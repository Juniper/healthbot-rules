from jnpr.junos import Device
from jnpr.junos.utils.config import Config

"""
This function returns the final value of alive/dead ifstates
0 : All is normal
1 : Dead ifstates are more than the threshold, 50% of alive ifstates
"""


def get_dead_alive_ratio(alive_ifstates_cnt, dead_ifstates_cnt, **kwargs):
	ratio = 0
	a = int(alive_ifstates_cnt/2)
	if (int(dead_ifstates_cnt) > a):
		ratio = 1
	return ratio
