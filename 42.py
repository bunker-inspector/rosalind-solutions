from cStringIO import StringIO
from Bio import Phylo

if __name__ == "__main__":
    data = map(lambda s: s.strip(), open("data/42.dat").readlines())

    pairs = []
    for i in range(0, len(data), 3):
        pairs.append((data[i], data[i+1]))

    pairs = map(lambda tup: ([i for i in Phylo.parse(StringIO(tup[0]), "newick")][0], tup[1]) , pairs)
    for pair in pairs:
        endpts = pair[1].split()
        ancestor = pair[0].common_ancestor(endpts[0], endpts[1])
        print int(ancestor.distance(endpts[0]) + ancestor.distance(endpts[1])),
