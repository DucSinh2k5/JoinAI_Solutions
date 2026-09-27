def dense_forward(inputs, weights, biases):
    outputs = []
    
    # Lướt qua trọng số và bias của từng nơ-ron đầu ra
    for weight_row, bias in zip(weights, biases):
        
        # Tính tích vô hướng (dot product) giữa inputs và weights của nơ-ron đó
        dot_product = sum(x * w for x, w in zip(inputs, weight_row))
        
        # Cộng thêm bias và đưa vào danh sách kết quả
        outputs.append(dot_product + bias)
        
    return outputs
