import math

def attention_weights(query, keys):
    if not keys:
        return []
        
    d = len(query)
    sqrt_d = math.sqrt(d)
    
    
    scores = []
    for key in keys:
        dot_product = sum(q * k for q, k in zip(query, key))
        scores.append(dot_product / sqrt_d)
        
    
    max_score = max(scores)
    exps = [math.exp(score - max_score) for score in scores]
    
    sum_exps = sum(exps)
    
    return [e / sum_exps for e in exps]