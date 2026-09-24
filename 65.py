def decision_tree_predict(nodes, query):
    current_idx = 0
    
    while True:
        feature, threshold, left, right, prediction = nodes[current_idx]
        
        # Nếu feature == -1, đây là nút lá, trả về kết quả dự đoán
        if feature == -1:
            return prediction
            
        # Nếu không, so sánh giá trị query với ngưỡng để chọn nhánh
        if query[feature] <= threshold:
            current_idx = left
        else:
            current_idx = right
