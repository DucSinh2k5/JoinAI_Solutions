def matrix_add(a, b):
    return [[val_a + val_b for val_a, val_b in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]