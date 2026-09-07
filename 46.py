import math

def z_scores(values):
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    std_dev = math.sqrt(variance)
    
    return [(x - mean) / std_dev for x in values]
