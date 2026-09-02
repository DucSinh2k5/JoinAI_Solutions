import math

def softmax(logits):
    if not logits:
        return []
    max_logit = max(logits)
    exps = [math.exp(x - max_logit) for x in logits]
    sum_exps = sum(exps)
    return [ex / sum_exps for ex in exps]