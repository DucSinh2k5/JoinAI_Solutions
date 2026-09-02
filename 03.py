import math
def mse(y_true, y_pred):
    s = 0
    for i in range(len(y_true)):
        s+= (y_true[i] - y_pred[i]) ** 2
    return s/len(y_true)
