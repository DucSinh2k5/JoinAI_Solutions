import math

def temperature_scale(logits, temperature):
    scaled_logits = [x / temperature for x in logits]
    max_scaled = max(scaled_logits)
    exps = [math.exp(x - max_scaled) for x in scaled_logits]
    sum_exps = sum(exps)
    return [e / sum_exps for e in exps]