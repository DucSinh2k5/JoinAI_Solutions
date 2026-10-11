def term_frequency(token_ids, vocab_size):
    # Bước 1: Khởi tạo mảng đếm và đếm tần suất các ID
    counts = [0] * vocab_size
    for token_id in token_ids:
        counts[token_id] += 1
        
    # Bước 2: Tính độ dài văn bản (mẫu số)
    doc_length = len(token_ids)
    
    # Bước 3: Chuẩn hóa bằng cách chia từng giá trị đếm cho độ dài văn bản
    return [count / doc_length for count in counts]
