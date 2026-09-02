def top_k(scores, k):
   
    indices = range(len(scores))
    
   
    sorted_indices = sorted(indices, key=lambda i: (-scores[i], i))
    
    
    return sorted_indices[:k]