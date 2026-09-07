def population_variance(values):
    n = len(values)
    mean = sum(values) / n
    return sum((x - mean) ** 2 for x in values) / n
  
