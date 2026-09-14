def recall(y_true, y_pred):
    true_positives = 0
    actual_positives = 0
    
    for yt, yp in zip(y_true, y_pred):
        if yt == 1:
            actual_positives += 1
            if yp == 1:
                true_positives += 1
                
    return true_positives / actual_positives
