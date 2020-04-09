from __future__ import division
'''
This function converts memory mem string to integer
'''
def mem_common_form(mem, **kwargs):
        if mem.endswith('M'):
            mem = mem[:-1]
            mem = int(mem)
            mem = mem * 1024
        elif mem.endswith('G'):
            mem = mem[:-1]
            mem = int(mem)
            mem = mem * 1024*1024
        else:
            mem = mem[:-1]
            mem = int(mem)
        return mem
