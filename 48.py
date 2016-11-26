from Bio.SubsMat import MatrixInfo
from fastamasta import parse_fasta
from Bio import pairwise2


if __name__ == "__main__":
    data = [x[1] for x in parse_fasta(open("data/48.fas").read())]

    pen_mat = MatrixInfo.blosum62

    alignment = pairwise2.align.localds(data[0], data[1], pen_mat, -11, -1)
    formatted =  pairwise2.format_alignment(*alignment[0]).split('\n')

    align_st, align_ed = formatted[1].find('|'), formatted[1].rfind('|')+1

    print int(alignment[0][2])
    print formatted[0][align_st:align_ed]
    print formatted[2][align_st:align_ed]
