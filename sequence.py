def bp_counts(sequence):
    sequence = sequence.upper()

    counts = {
            'A' : 0,
            'C' : 0,
            'G' : 0,
            'T' : 0
            }

    for character in sequence:
        counts[character] += 1

    return counts

def rev_complement(sequence):
    complements = {
        'A' : 'T',
        'C' : 'G',
        'G' : 'C',
        'T' : 'A'
        }

    return ''.join([complements[i] for i in sequence[::-1]])
