def project_vector(a, b):
    
    dot_ab = sum(x * y for x, y in zip(a, b))
    
    
    dot_bb = sum(x * y for x, y in zip(b, b))
    
    
    scalar = dot_ab / dot_bb
    
    
    return [scalar * x for x in b]