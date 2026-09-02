def threshold_predictions(probabilities, threshold):
    a =[]
    for i in range(len(probabilities)):
        if(probabilities[i]>=threshold):
            a.append(1)
        else:
            a.append(0)
    return a
