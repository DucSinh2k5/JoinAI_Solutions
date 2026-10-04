def global_average_pool(feature_maps):
    averages = []
    
    # Bước 1: Xử lý từng channel một
    for channel in feature_maps:
        
        # Bước 2: Tính tổng tất cả các phần tử trong channel
        channel_sum = sum(sum(row) for row in channel)
        
        # Bước 3: Đếm tổng số phần tử (số hàng * số cột)
        num_elements = len(channel) * len(channel[0])
        
        # Tính trung bình và thêm vào danh sách kết quả
        averages.append(channel_sum / num_elements)
        
    return averages
