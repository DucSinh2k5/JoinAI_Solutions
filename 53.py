import math

def logistic_predict(features, weights, bias):
    probabilities = []
    
    for row in features:
        score = sum(f * w for f, w in zip(row, weights)) + bias
        probability = 1 / (1 + math.exp(-score))
        probabilities.append(probability)
        
    return probabilities
