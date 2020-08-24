def notcommon(list1, list2, **kwargs):
    list3 = []
    for element in list1:
        a = str(element)
        b = "/32"
        list3.append(a+b)
    peerset = set (list3)
    routeset = set (list2)
    commonset = peerset.intersection(routeset)
    commonlist = list(commonset)
    list4 = []
    for item in list3: 
        if item not in commonlist: 
            list4.append(item)
    joincomma = ','.join(list4)
    return(joincomma)