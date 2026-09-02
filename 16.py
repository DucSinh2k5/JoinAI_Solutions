import math

def l2_norm(x):
    s = 0
    for i in x:
        s += i * i          
    return math.sqrt(s)    