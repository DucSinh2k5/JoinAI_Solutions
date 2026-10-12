def extract_ngrams(tokens, n):
    return [tokens[i : i + n] for i in range(len(tokens) - n + 1)]
