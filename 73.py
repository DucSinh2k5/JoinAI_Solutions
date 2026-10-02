import math

def batch_normalize(values, gamma, beta, epsilon):
    n = len(values)
    
    # Bước 1: Tính trung bình (mean)
    mean = sum(values) / n
    
    # Bước 2: Tính phương sai quần thể (population variance)
    variance = sum((x - mean) ** 2 for x in values) / n
    
    # Bước 3: Tính mẫu số chuẩn hóa
    std_inv = 1.0 / math.sqrt(variance + epsilon)
    
    # Bước 4: Áp dụng công thức chuẩn hóa, co giãn và dịch chuyển
    return [gamma * (x - mean) * std_inv + beta for x in values]
