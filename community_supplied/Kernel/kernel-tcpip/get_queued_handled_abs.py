'''
This function returns absolute difference between pkt_handled_arg  and pkt_queued_arg
'''
def get_queued_handled_pkt_abs_value(pkt_handled_arg, pkt_queued_arg,**kwargs):
        return abs(int(pkt_queued_arg) - int(pkt_handled_arg))
