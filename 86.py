import math

def perplexity(probabilities):
    n = len(probabilities)
    
    # Bước 1 & 2: Tính giá trị trung bình của negative log probabilities
    avg_neg_log = -sum(math.log(p) for p in probabilities) / n
    
    # Bước 3: Áp dụng hàm exp một lần duy nhất
    return math.exp(avg_neg_log)
