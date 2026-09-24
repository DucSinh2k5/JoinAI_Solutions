import math

def adaboost_weight_update(sample_weights, labels, predictions, alpha):
    unnormalized_weights = []
    total_weight = 0.0
    
    for w, y, h in zip(sample_weights, labels, predictions):
        # Tính trọng số mới theo công thức
        new_w = w * math.exp(-alpha * y * h)
        unnormalized_weights.append(new_w)
        total_weight += new_w
        
    # Chuẩn hóa để tổng các trọng số bằng 1
    return [nw / total_weight for nw in unnormalized_weights]
