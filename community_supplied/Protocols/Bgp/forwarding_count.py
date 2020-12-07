def forwarding_count(destination, to, **kwargs):
    """
    Pleae fill in the comments
 
    :param destination:
    :param to:
    :param kwargs:
    :return:
    """
    if 'hb_store' not in kwargs:
        kwargs['hb_store'] = {
            'count': dict(),
            'dict': dict()
        }
    else:
        if 'count' not in kwargs['hb_store']:
            kwargs['hb_store']['count'] = dict()
        if 'dict' not in kwargs['hb_store']:
            kwargs['hb_store']['dict'] = dict()
 
    count = kwargs['hb_store']['count']
    destination_dict = kwargs['hb_store']['dict']
 
    if destination in destination_dict:
        if to not in destination_dict[destination]:
            if to != "to":
                destination_dict[destination].append(to)
                count[destination] = len(destination_dict[destination])
                return count[destination]
            else:
                return 0
        else:
            return count[destination]
    else:
        if to != "to":
            destination_dict[destination] = [to]
            count[destination] = len(destination_dict[destination])
            return count[destination]
        else:
            return 0
