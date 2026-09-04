def matrix_vector_multiply(matrix, vector):
    return [sum(m_val * v_val for m_val, v_val in zip(row, vector)) for row in matrix]