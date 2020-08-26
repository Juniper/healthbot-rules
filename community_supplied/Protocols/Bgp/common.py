def common(list1, list2, **kwargs):
    list3 = []
    for element in list1:
        a = str(element)
        b = "/32"
        list3.append(a+b)
    peerset = set (list3)
    routeset = set (list2)
    commonset = peerset.intersection(routeset)
    joincomma = ','.join(commonset)
    return(joincomma)