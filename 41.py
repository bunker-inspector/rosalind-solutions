from tree import *

def tree_perms(leaves):
    if len(leaves) <= 2:
        return [Tree(values=leaves)]

    trees = tree_perms(leaves[:-1])
    name = leaves[-1]
    new_trees = []

    for tree in trees:
        for i in range(len(tree.edges)):
            copy = tree.copy()
            s_edge = copy.edges[i]
            node1, node2 = s_edge.nodes

            copy.edges.remove(s_edge)

            internal = Node()
            copy.nodes.append(internal)

            new_leaf = Node(name)
            copy.nodes.append(new_leaf)

            copy.edges.append(Edge(node1, internal))
            copy.edges.append(Edge(node2, internal))
            copy.edges.append(Edge(new_leaf, internal))

            new_trees.append(copy)

    return new_trees

if __name__ == '__main__':
    data = open('data/41.dat').read().split()
    trees = tree_perms(data)

    for tree in [newick(tree) for tree in trees]:
        print tree
