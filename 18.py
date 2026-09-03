def pairwise_similarity(vectors):
    n = len(vectors)
    norms = [sum(x**2 for x in v) ** 0.5 for v in vectors]

    
    similarity_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            dot_product = sum(a * b for a, b in zip(vectors[i], vectors[j]))
            similarity = dot_product / (norms[i] * norms[j])
            row.append(similarity)
        similarity_matrix.append(row)
        
    return similarity_matrix