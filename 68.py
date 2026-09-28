def relu_derivative(xs):
    return [1 if x > 0 else 0 for x in xs]
