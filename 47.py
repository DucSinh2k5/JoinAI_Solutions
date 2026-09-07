def covariance(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    return sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y)) / n
