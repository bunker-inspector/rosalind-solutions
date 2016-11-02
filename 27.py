from Bio import Entrez
from fastamasta import parse_fasta

if __name__ == "__main__":
    data_file = open("data/27.dat", 'r')
    data = data_file.readline().strip().split()

    Entrez.email = "realdonaldtrump@twitter.com"
    handle = Entrez.efetch(db="nucleotide", id=data, rettype="fasta")
    records = handle.read()

    fasta = parse_fasta(records)
    min_idx, min_len = -1, lambda: None

    for i in range(len(fasta)):
        if len(fasta[i][1]) < min_len:
            min_idx, min_len = i, len(fasta[i][1])

    print '>' + fasta[min_idx][0]
    print fasta[min_idx][1]
