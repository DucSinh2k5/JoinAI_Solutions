def beam_search(step_probabilities, beam_width):
    beams = [(1.0, [])]
    
    for step_probs in step_probabilities:
        new_candidates = []
        for score, seq in beams:
            for token_idx, token_prob in enumerate(step_probs):
                new_score = score * token_prob
                new_seq = seq + [token_idx]
                new_candidates.append((new_score, new_seq))
        
        new_candidates.sort(key=lambda x: (-x[0], x[1]))
        beams = new_candidates[:beam_width]
        
    return [seq for score, seq in beams]