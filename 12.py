from aaiter import find_orfs
from fastamasta import FastaReader
from sequence import translate, rev_complement

if __name__ == "__main__":
    reader = FastaReader("data/12.dat")
    seq = reader.readnext()[1]
    rcseq = rev_complement(seq)

    orfs = find_orfs(seq)
    rorfs = find_orfs(rcseq)

    candidates = set()
    for orf in orfs:
        candidates.add(translate(seq[orf[0]:orf[1]]))

    for rorf in rorfs:
        candidates.add(translate(rcseq[rorf[0]:rorf[1]]))

    for candidate in candidates:
        print candidate
