count=dict()
dict=dict()
def forwarding_count(destination, to, **kwargs):
    global count
    global dict
    if destination in dict:
        if to not in dict[destination]:
            if to != "to":
                dict[destination].append(to)
                count[destination]=len(dict[destination])
                return count[destination]
            else:
                return 0
        else:
            return count[destination]
    else:
        if to != "to":
            dict[destination]=[to]
            count[destination]=len(dict[destination])
            return count[destination]
        else:
            return 0
