import math
from collections import Counter

def bleu_1(candidate, reference):
    c = len(candidate)
    r = len(reference)
    
    # Bước 1: Đếm tần suất xuất hiện của các từ trong cả hai câu
    cand_counts = Counter(candidate)
    ref_counts = Counter(reference)
    
    # Bước 2: Tính tổng các từ khớp có giới hạn (clipped matches)
    clipped_matches = sum(
        min(count, ref_counts[token]) 
        for token, count in cand_counts.items()
    )
    
    # Bước 3: Tính unigram precision
    precision = clipped_matches / c
    
    # Bước 4: Tính hệ số phạt câu ngắn (Brevity Penalty)
    if c < r:
        bp = math.exp(1 - r / c)
    else:
        bp = 1.0
        
    return bp * precision
