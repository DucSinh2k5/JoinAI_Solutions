def chain_gradients(upstream, local):
    return [u * l for u, l in zip(upstream, local)]
