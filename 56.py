def precision(y_true, y_pred):
    true_positives = 0
    predicted_positives = 0
    
    for yt, yp in zip(y_true, y_pred):
        if yp == 1:
            predicted_positives += 1
            if yt == 1:
                true_positives += 1
                
    return true_positives / predicted_positives
