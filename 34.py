import math

def normalize_vector(x):
    l2_norm = math.sqrt(sum(i**2 for i in x))
    return [i / l2_norm for i in x]