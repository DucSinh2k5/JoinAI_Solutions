import math

def single_head_attention(queries, keys, values):
    d = len(queries[0])
    d_sqrt = math.sqrt(d)
    value_dim = len(values[0])
    
    result = []
    
    for query in queries:
        scores = []
        for key in keys:
            dot_product = sum(q * k for q, k in zip(query, key))
            scores.append(dot_product / d_sqrt)
            
        max_score = max(scores)
        exps = [math.exp(score - max_score) for score in scores]
        sum_exps = sum(exps)
        attention_weights = [e / sum_exps for e in exps]
        
        context_vector = [0.0] * value_dim
        for weight, value in zip(attention_weights, values):
            for i in range(value_dim):
                context_vector[i] += weight * value[i]
                
        result.append(context_vector)
        
    return result