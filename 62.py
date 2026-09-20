import math

def gaussian_naive_bayes(query, means, variances, priors):
    best_class = -1
    best_score = -float('inf')
    
    for c, (class_means, class_vars, prior) in enumerate(zip(means, variances, priors)):
        # Hint 1: Khởi tạo điểm bằng log(prior)
        score = math.log(prior)
        
        # Hint 2: Cộng dồn log-likelihood của từng đặc trưng
        for x, mu, var in zip(query, class_means, class_vars):
            # Công thức Log của phân phối chuẩn (Gaussian PDF in log space)
            log_prob = -0.5 * math.log(2 * math.pi * var) - ((x - mu) ** 2) / (2 * var)
            score += log_prob
            
        # Hint 3: Chỉ cập nhật khi điểm lớn hơn nghiêm ngặt (ưu tiên index nhỏ khi hòa)
        if score > best_score:
            best_score = score
            best_class = c
            
    return best_class
