import math

def pearson_correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    cov_sum = 0
    var_sum_x = 0
    var_sum_y = 0
    
    for x_i, y_i in zip(x, y):
        dx = x_i - mean_x
        dy = y_i - mean_y
        
        cov_sum += dx * dy
        var_sum_x += dx ** 2
        var_sum_y += dy ** 2
        
    return cov_sum / math.sqrt(var_sum_x * var_sum_y)
