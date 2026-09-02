def mae(y_true, y_pred):
    s=0
    for i in range(len(y_true)):
        s+=abs(y_true[i]-y_pred[i])
    return s/len(y_true)
