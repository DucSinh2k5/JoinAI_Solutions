def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    
    if n % 2 != 0:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
