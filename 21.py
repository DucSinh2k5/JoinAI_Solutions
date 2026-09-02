def one_hot(indices, num_classes):
    return [[int(c == i) for c in range(num_classes)] for i in indices]
