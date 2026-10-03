def apply_dropout(values, mask, drop_probability):
    keep_probability = 1 - drop_probability
    
    return [(v * m) / keep_probability for v, m in zip(values, mask)]
