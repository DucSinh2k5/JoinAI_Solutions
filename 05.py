def greedy_decode(logits):
    return [row.index(max(row)) for row in logits]
