import math

def cross_entropy_from_logits(logits, target_index):
    # Bước 1: Tìm giá trị logit lớn nhất để ổn định số học
    m = max(logits)
    
    # Bước 2: Tính tổng của e^(z - m) cho tất cả các class
    sum_exp = sum(math.exp(z - m) for z in logits)
    
    # Bước 3: Tính toán cross-entropy loss theo công thức
    loss = math.log(sum_exp) - (logits[target_index] - m)
    
    return loss
