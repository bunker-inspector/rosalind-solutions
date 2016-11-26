from sequence import rev_complement
from fastamasta import FastaReader
from functional import partition


if __name__ == "__main__":
    seq = [i for i in FastaReader("data/44.fas")][0][1]

    rev_palindromes = []
    for i in range(4, 13):
        parts = [''.join(x) for x in partition(seq, i, list)]
        for j in range(len(parts)):
            if parts[j] == rev_complement(parts[j]):
                rev_palindromes.append((j+1, i))

    for tup in rev_palindromes:
        print tup[0], tup[1]
