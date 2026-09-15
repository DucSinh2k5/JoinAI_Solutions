def gradient_step(parameters, gradients, learning_rate):
    return [p - (learning_rate * g) for p, g in zip(parameters, gradients)]
