from jnpr.junos import Device
import requests
 
# script to find label which comes after pattern 8847 in any of the argument line
def getmplslabel(packet0, packet1, packet2, packet3, packet4, **kwargs):
    # (' '.join(i if i is not None else '' for i in args))
    # print (args)
    for item in [packet0, packet1, packet2, packet3, packet4]:
        if '88 47' in item:
            # print ("found it")
            mylabel = item.replace(' ', '')
            # print (mylabel)
            mylabeloc = (mylabel.find('8847'))
            mylabeloc = mylabeloc + 4
            # print (mylabeloc)
            label = (mylabel[mylabeloc:31])
            label=(int(label, 16))
    return (label)