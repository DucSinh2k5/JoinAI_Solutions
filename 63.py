def gini_impurity(labels):
    if not labels:
        return 0.0
    
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
        
    impurity = 1.0
    total = len(labels)
    for count in counts.values():
        prob = count / total
        impurity -= prob ** 2
        
    return impurity

def best_gini_split(feature_values, labels):
    # Ghép cặp và sắp xếp theo feature_values
    sorted_pairs = sorted(zip(feature_values, labels), key=lambda x: x[0])
    sorted_features = [p[0] for p in sorted_pairs]
    sorted_labels = [p[1] for p in sorted_pairs]
    
    n = len(sorted_labels)
    best_threshold = None
    best_gini = float('inf')
    
    # Duyệt qua để tìm các điểm chia giữa các giá trị liền kề
    for i in range(n - 1):
        if sorted_features[i] != sorted_features[i+1]:
            # Ngưỡng là điểm chính giữa 2 giá trị khác biệt
            threshold = (sorted_features[i] + sorted_features[i+1]) / 2.0
            
            # Chia tách nhãn thành 2 nhánh (Left và Right)
            left_labels = sorted_labels[:i+1]
            right_labels = sorted_labels[i+1:]
            
            # Tính Gini của từng nhánh
            gini_left = gini_impurity(left_labels)
            gini_right = gini_impurity(right_labels)
            
            # Tính Gini có trọng số
            weight_left = len(left_labels) / n
            weight_right = len(right_labels) / n
            weighted_gini = weight_left * gini_left + weight_right * gini_right
            
            # Cập nhật ngưỡng tốt nhất
            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_threshold = threshold
            elif weighted_gini == best_gini:
                # Phá vỡ thế hòa: Chọn ngưỡng nhỏ hơn
                if best_threshold is None or threshold < best_threshold:
                    best_threshold = threshold
                    
    return [best_threshold, best_gini]
