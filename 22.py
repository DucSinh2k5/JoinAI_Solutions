def pad_sequences(sequences, max_length, pad_value):
    return [seq[:max_length] + [pad_value] * max(0, max_length - len(seq)) for seq in sequences]