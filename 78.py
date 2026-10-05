def build_vocabulary(tokens):
    # set(tokens): Lọc từ trùng lặp
    # sorted(...): Sắp xếp theo thứ tự từ điển
    # enumerate(...): Đánh số ID từ 0
    return {token: i for i, token in enumerate(sorted(set(tokens)))}
