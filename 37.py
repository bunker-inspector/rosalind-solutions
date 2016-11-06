from cStringIO import StringIO
from fastamasta import parse_fasta
from Bio import Phylo
from phylophile import tree_h_dist, min_int_node_values

if __name__ == "__main__":
    data = open("data/37.dat", 'r').readlines()
    tree = Phylo.parse(StringIO(data[0].strip()), "newick")
    fasta_data = parse_fasta(''.join(data[1:]))

    node_values = {}
    for i in fasta_data:
        node_values[i[0]] = i[1]

    leaves = set([i[0] for i in fasta_data])

    root = [i for i in tree][0].clade

    min_int_node_values(root, node_values)

    print tree_h_dist(root, node_values)

    internal_nodes = set([k for k,v in node_values.iteritems()]) - leaves

    for i in internal_nodes:
        print '>' + i
        print node_values[i]
