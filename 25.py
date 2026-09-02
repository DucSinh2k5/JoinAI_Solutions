import math

def masked_softmax(logits, mask):
    valid_logits = [logits[i] for i in range(len(logits)) if mask[i] == 1]
    
    if not valid_logits:
        return [0] * len(logits)
        
    m = max(valid_logits)
    
    exps = [math.exp(logits[i] - m) if mask[i] == 1 else 0 for i in range(len(logits))]
    sum_exps = sum(exps)
    
    return [e / sum_exps for e in exps]