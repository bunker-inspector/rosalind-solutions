from Bio.SubsMat import MatrixInfo
from fastamasta import parse_fasta
from Bio import pairwise2


if __name__ == "__main__":
    data = [x[1] for x in parse_fasta(open("data/47.fas").read())]

    pen_mat = MatrixInfo.pam250

    alignment = pairwise2.align.localds(data[0], data[1], pen_mat, -5, -5)
    print alignment
