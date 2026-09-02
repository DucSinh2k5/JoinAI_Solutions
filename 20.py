def mean_reciprocal_rank(relevant_sets, rankings):
    if not relevant_sets:
        return 0.0
        
    total_rr = 0.0
    num_queries = len(relevant_sets)
    
    for i in range(num_queries):
        rel_set = set(relevant_sets[i])
        
        for rank, item in enumerate(rankings[i], start=1):
            if item in rel_set:
                total_rr += 1.0 / rank
                break
                
    return total_rr / num_queries