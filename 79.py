def encode_tokens(tokens, vocabulary, unknown_id):
    return [vocabulary.get(token, unknown_id) for token in tokens]
