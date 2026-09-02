def scaled_dot_products(query, keys):
    
    d_sqrt = len(query) ** 0.5
    
    scores = []
    for key in keys:
        
        dot_product = sum(q * k for q, k in zip(query, key))
        
        scores.append(dot_product / d_sqrt)
        
    return scores