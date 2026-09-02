def padding_mask(tokens, pad_id):
    return [int(token != pad_id) for token in tokens]