def confusion_matrix(y_true, y_pred):
    tn = fp = fn = tp = 0
    
    for true_val, pred_val in zip(y_true, y_pred):
        if true_val == 0 and pred_val == 0:
            tn += 1
        elif true_val == 0 and pred_val == 1:
            fp += 1
        elif true_val == 1 and pred_val == 0:
            fn += 1
        elif true_val == 1 and pred_val == 1:
            tp += 1
            
    return [[tn, fp], [fn, tp]]
