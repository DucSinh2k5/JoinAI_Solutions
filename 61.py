def knn_classify(train_points, labels, query, k):
    # Bước 1: Tính khoảng cách bình phương từ mỗi điểm train đến điểm query
    distances = []
    for point, label in zip(train_points, labels):
        # sum((p - q)^2) cho mọi chiều d
        sq_dist = sum((p_val - q_val) ** 2 for p_val, q_val in zip(point, query))
        distances.append((sq_dist, label))
        
    # Bước 2: Sắp xếp theo khoảng cách (tăng dần)
    distances.sort(key=lambda x: x[0])
    
    # Bước 3: Lấy nhãn của k láng giềng gần nhất
    nearest_labels = [label for _, label in distances[:k]]
    
    # Bước 4: Đếm số phiếu bầu cho mỗi nhãn
    counts = {}
    for label in nearest_labels:
        counts[label] = counts.get(label, 0) + 1
        
    # Bước 5: Trả về nhãn có số phiếu cao nhất (giải quyết hòa bằng nhãn nhỏ hơn)
    return max(counts.keys(), key=lambda l: (counts[l], -l))
