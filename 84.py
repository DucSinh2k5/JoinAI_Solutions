def embedding_lookup(token_ids, embedding_table):
    # Dùng List Comprehension để duyệt qua các ID
    # Lấy ra hàng tương ứng và dùng list() để tạo một bản sao độc lập (new row list)
    return [list(embedding_table[token_id]) for token_id in token_ids]
