def percentile(values, p):
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    position = (p / 100) * (n - 1)
    
    lower_idx = int(position)
    upper_idx = min(lower_idx + 1, n - 1)
    fraction = position - lower_idx
    
    return sorted_values[lower_idx] + (sorted_values[upper_idx] - sorted_values[lower_idx]) * fraction
  
