def f1_score(y_true, y_pred):
    tp = fp = fn = 0
    
    for yt, yp in zip(y_true, y_pred):
        if yp == 1 and yt == 1:
            tp += 1
        elif yp == 1 and yt == 0:
            fp += 1
        elif yp == 0 and yt == 1:
            fn += 1
            
    denominator = 2 * tp + fp + fn
    
    if denominator == 0:
        return 0.0
        
    return (2 * tp) / denominator
