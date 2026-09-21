def svm_hinge_gradient(features, labels, weights, bias, regularization):
    n = len(features)
    num_features = len(weights)
    
    # Hint 1: Initialize dw with regularization * weights
    dw = [regularization * w for w in weights]
    db = 0.0
    
    for x, y in zip(features, labels):
        # Tính điểm tuyến tính: dot(w, x) + b
        score = sum(w * f for w, f in zip(weights, x)) + bias
        
        # Hint 2: Compute label * score before checking the margin
        margin = y * score
        
        # Chỉ cập nhật gradient nếu vi phạm lề (margin < 1)
        if margin < 1:
            for j in range(num_features):
                dw[j] -= (y * x[j]) / n
            db -= y / n
            
    # Hint 3: Append db after all weight components
    dw.append(db)
    
    return dw
