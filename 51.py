import math

def normal_pdf(xs, mean, std):
    norm_const = std * math.sqrt(2 * math.pi)
    var_const = 2 * (std ** 2)
    
    return [math.exp(-((x - mean) ** 2) / var_const) / norm_const for x in xs]
