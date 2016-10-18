from codontab import STD_DNA_CODON_TAB

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

def hamming_dist(a, b):
    if len(a) != len(b):
        return -1
    else:
        result = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                result += 1
        return result

def translate(seq):
    translated = ''

    for i in range(0, len(seq), 3):
        translated += STD_DNA_CODON_TAB[seq[i:i+3]]

    return translated[:-1]
