def min_max_normalize(xs):
    a = min(xs)
    b = max(xs)
    mang = []
    if(a==b):
        for i in xs:
            mang.append(0)
    else:
        
        for i in xs:
            mang.append(float((i-a)/(b-a)))
    return mang
