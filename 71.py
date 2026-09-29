def dense_input_gradient(weights, output_gradient):
    # Lấy số lượng đặc trưng đầu vào (số cột của hàng đầu tiên)
    num_inputs = len(weights[0])
    
    # Tạo danh sách chứa các gradient đầu vào, ban đầu bằng 0
    input_gradients = [0.0] * num_inputs
    
    # Lướt qua từng nơ-ron đầu ra: hàng trọng số và gradient của nó
    for weight_row, out_grad in zip(weights, output_gradient):
        
        # Cộng dồn đóng góp của nơ-ron này cho từng gradient đầu vào
        for i in range(num_inputs):
            input_gradients[i] += weight_row[i] * out_grad
            
    return input_gradients
