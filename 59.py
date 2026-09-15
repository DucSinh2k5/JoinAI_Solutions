def linear_gradient(xs, ys, weight, bias):
    n = len(xs)
    dw_sum = 0
    db_sum = 0
    
    for x, y in zip(xs, ys):
        y_hat = weight * x + bias
        error = y_hat - y
        
        dw_sum += error * x
        db_sum += error
        
    return [(2 * dw_sum) / n, (2 * db_sum) / n]
