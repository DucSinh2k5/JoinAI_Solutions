def bag_of_words(token_ids, vocab_size):
    # Bước 1: Khởi tạo mảng đếm với toàn bộ giá trị 0
    counts = [0] * vocab_size
    
    # Bước 2 & 3: Lướt qua từng token và tăng giá trị đếm tại index tương ứng
    for token_id in token_ids:
        counts[token_id] += 1
        
    return counts
