from Bio import Entrez
from fastamasta import parse_fasta

if __name__ == "__main__":
    data_file = open("data/32.dat", 'r')
    data = data_file.readline().strip().split()

    Entrez.email = "realdonaldtrump@twitter.com"
    handle = Entrez.efetch(db="nucleotide", id=data, rettype="fasta")
    records = handle.read()

    print records

    #fasta = parse_fasta(records)
