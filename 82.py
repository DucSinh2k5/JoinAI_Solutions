import math

def inverse_document_frequency(documents, vocab_size):
    N = len(documents)
    
    # Khởi tạo mảng đếm Document Frequency (DF)
    df = [0] * vocab_size
    
    # Bước 1 & 2: Chuyển mỗi document thành set và đếm số lượng văn bản chứa mỗi từ
    for doc in documents:
        unique_words = set(doc)
        for word in unique_words:
            df[word] += 1
            
    # Bước 3: Áp dụng công thức IDF cho từng từ vựng
    return [math.log((N + 1) / (count + 1)) + 1 for count in df]
