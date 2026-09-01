import math

def sigmoid(xs):
    return [1 / (1 + math.exp(-x)) for x in xs]