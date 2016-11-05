from Bio import pairwise2
from Bio.SubsMat.MatrixInfo import blosum62
from fastamasta import FastaReader

if __name__ == "__main__":
    data = [i[1] for i in FastaReader("data/35.fas")]

    for i in pairwise2.align.globalds(data[0],data[1], blosum62, -11, -1):
        print int(i[2])
        print i[0]
        print i[1]
        break
