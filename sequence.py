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

def edit_dist(s, t):
    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in xrange(cols)] for x in xrange(rows)]
    for i in xrange(1, rows):
        dist[i][0] = i
    for i in xrange(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,
                                 dist[row][col-1] + 1,
                                 dist[row-1][col-1] + cost)
    return dist[row][col]



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
