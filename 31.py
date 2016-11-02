from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, GlobalSequenceAligner
from fastamasta import FastaReader
from sequence import hamming_dist

if __name__ == "__main__"
    data = [i for i in FastaReader("data/31.fas")]
    a, b = data[0][1], data[1][1]

    if len(a) > len(b):
        b += '-'* ((len(a) - len(b))+1)
    if len(b) > len(a):
        a += '-'* ((len(b) - len(a))+1)



    # Create sequences to be aligned.
    a = Sequence([i for i in a])
    b = Sequence([i for i in b])

    # Create a vocabulary and encode the sequences.
    v = Vocabulary()
    aEncoded = v.encodeSequence(a)
    bEncoded = v.encodeSequence(b)

    # Create a scoring and align the sequences using global aligner.
    scoring = SimpleScoring(3, -1)
    aligner = GlobalSequenceAligner(scoring, -2)
    score, encodeds = aligner.align(aEncoded, bEncoded, backtrace=True)

    # Iterate over optimal alignments and print them.
    for encoded in encodeds:
        alignment = v.decodeSequenceAlignment(encoded)
        orig, to = [], []
        for i in xrange(len(alignment)):
            orig.append(alignment[i][0])
            to.append(alignment[i][1])

        orig = ''.join(orig)
        to = ''.join(to)
        print hamming_dist(orig, to)
        print orig
        print to
