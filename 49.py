def histogram_counts(values, bin_edges):
    bins = len(bin_edges) - 1
    counts = [0] * bins
    
    for v in values:
        for j in range(bins):
            if j == bins - 1:
                if bin_edges[j] <= v <= bin_edges[j+1]:
                    counts[j] += 1
                    break
            else:
                if bin_edges[j] <= v < bin_edges[j+1]:
                    counts[j] += 1
                    break
                    
    return counts
