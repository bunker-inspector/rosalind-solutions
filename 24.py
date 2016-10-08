class Node:
    def __init__(self, _value):
        self.value = _value
        self.children = []

    def occurs(self):
        if len(self.children) == 0:
            return 1
        else:
            result = 0
            for child in self.children:
                result += child.occurs()
            return result

    def print_traverse(self):
        print self.value
        for child in self.children:
            child.print_traverse()

    def LRS(self, n):
        if len(self.children) == 0:
            return "", 0
        else:
            lrs_vals = []
            for child in self.children:
                if child.occurs() >= n:
                    curr_lrs = child.LRS(n)
                    lrs_vals.append((curr_lrs[0], curr_lrs[1]))

            max_lrs, max_idx = -1, -1
            for i in range(len(lrs_vals)):
                if lrs_vals[i][1] > max_lrs:
                    max_lrs, max_idx = lrs_vals[i][1], i

            if max_lrs == -1: return (self.value, len(self.value))

            return (self.value + lrs_vals[max_idx][0],
                    len(self.value) + lrs_vals[max_idx][1])

class SuffixTreeBuilder:
    def __init__(self, s, edges):
        self._s = s
        self._tree = self._build_tree(edges)

    def _build_tree(self, edges):
        edge_map = {}
        for edge in edges:
            if edge[0] in edge_map:
                edge_map[edge[0]].append(edge[1])
            else:
                edge_map[edge[0]] = [edge[1]]

        edge_nodes = {"node1" : Node('')}
        for edge in edges:
            edge_nodes[edge[1]] = Node(s[edge[2]:edge[2]+edge[3]])

        for edge, children in edge_map.iteritems():
            for child in children:
                edge_nodes[edge].children.append(edge_nodes[child])

        return edge_nodes["node1"]

    def get_tree(self):
        return self._tree

if __name__ == "__main__":
    data_file = open("data/24.dat", 'r')
    s,n = data_file.readline().strip(), int(data_file.readline().strip())

    tree_data = []
    for line in data_file:
        edge = line.strip().split(' ')
        tree_data.append([edge[0], edge[1], int(edge[2])-1, int(edge[3])])

    stb = SuffixTreeBuilder(s, tree_data).get_tree()
    print stb.LRS(n)[0]

