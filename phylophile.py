import operator
from sequence import hamming_dist

def tree_h_dist(node, vals):
    if len(node.clades) is 0:
        return 0
    else:
        dist = 0
        for i in node.clades:
            dist += tree_h_dist(i, vals)
        for i in node.clades:
            dist += hamming_dist(vals[node.name], vals[i.name])
        return dist

def min_int_node_values(node, vals):
    if len(node.clades) is 0:
        pass
    else:
        for i in node.clades:
            min_int_node_values(i, vals)
        vals[node.name] = _consensus(node.clades, vals)

def _consensus(l, vals):
    sz = len(vals[vals.keys()[0]])
    counts = []
    for elem in l:
        for i in range(sz):
            counts.append({})
            char =  vals[elem.name][i]
            counts[i][char] = counts[i].get(char, 0) + 1
    result = ""
    for i in range(sz):
       result +=  max(counts[i].iteritems(), key=operator.itemgetter(1))[0]

    return result


