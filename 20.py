import urllib2
from fastamasta import parse_http_fasta
import re

URL = "http://www.uniprot.org/uniprot/"

if __name__ == "__main__":
    proteins = [i.strip() for i in open("data/20.dat", 'r')]
    expr = re.compile("N(?=([^P][ST][^P]))")

    for protein in proteins:
        seq = parse_http_fasta(URL + protein + ".fasta")[0][1]

        if expr.search(seq) is not None:
            print protein
            for m in expr.finditer(seq):
                print m.start() + 1,
            print ''


