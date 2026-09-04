def matrix_multiply(a, b):
    b_t = [list(col) for col in zip(*b)]
    
    return [[sum(val_a * val_b for val_a, val_b in zip(row_a, col_b)) for col_b in b_t] for row_a in a]