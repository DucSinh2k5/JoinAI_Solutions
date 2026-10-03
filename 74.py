def conv1d_valid(signal, kernel, bias):
    n_sig = len(signal)
    n_ker = len(kernel)
    
    # Tính số lượng đầu ra hợp lệ
    num_outputs = n_sig - n_ker + 1
    outputs = []
    
    # Trượt kernel dọc theo signal
    for i in range(num_outputs):
        # Lấy cửa sổ hiện tại của signal
        window = signal[i : i + n_ker]
        
        # Tính tích vô hướng (dot product) và cộng bias
        dot_product = sum(s * k for s, k in zip(window, kernel))
        outputs.append(dot_product + bias)
        
    return outputs
