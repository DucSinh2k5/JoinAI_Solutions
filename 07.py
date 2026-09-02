def relu(xs):
    b = []
    for i in xs:
        if(i>0):
            b.append(i)
        else:
            b.append(0)
    return b
