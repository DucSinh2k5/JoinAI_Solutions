import math

def top_k_distribution(logits, k):
    if k <= 0 or not logits:
        return [0.0] * len(logits)
        
    indexed_logits = list(enumerate(logits))
    indexed_logits.sort(key=lambda x: (-x[1], x[0]))
    
    top_k = indexed_logits[:k]
    top_indices = {idx for idx, val in top_k}
    
    max_logit = top_k[0][1]
    
    probs = [0.0] * len(logits)
    sum_exp = 0.0
    
    for idx in top_indices:
        exp_val = math.exp(logits[idx] - max_logit)
        probs[idx] = exp_val
        sum_exp += exp_val
        
    for idx in top_indices:
        probs[idx] /= sum_exp
        
    return probs