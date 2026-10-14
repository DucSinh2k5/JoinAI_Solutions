def bigram_counts(token_ids, vocab_size):
    # Bước 1: Khởi tạo ma trận vuông kích thước vocab_size x vocab_size gồm toàn số 0
    counts = [[0] * vocab_size for _ in range(vocab_size)]
    
    # Bước 2 & 3: Duyệt qua từng cặp token liền kề và tăng bộ đếm tương ứng
    for curr_id, next_id in zip(token_ids[:-1], token_ids[1:]):
        counts[curr_id][next_id] += 1
        
    return counts
