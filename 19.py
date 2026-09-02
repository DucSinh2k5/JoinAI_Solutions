def precision_at_k(relevant, ranked, k):
    if k == 0:
        return 0.0
    relevant_set = set(relevant)
    hits = sum(1 for item in ranked[:k] if item in relevant_set)
    return hits / k