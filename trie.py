class Trie():
    class Node():
        def __init__(self, val):
            self.val = val
            self.children = []

    def __init__(self, str_coll):
        self._root = self.Node(None)
        for string in str_coll:
            self.insert(string)

    def insert(self, new_str):
        curr_node = self._root
        for char in new_str:
            add = True
            for child in curr_node.children:
                if char == child.val:
                    curr_node = child
                    add = False
            if add:
                new_node = self.Node(char)
                curr_node.children.append(new_node)
                curr_node = new_node

    def print_traverse(self, node=None):
        if node == None:
            node = self._root
        for child in node.children:
            print child.val
            self.print_traverse(child)

    def adj_list(self, node=None, l=None, edge=[1]):
        if node == None:
            node = self._root
        if l == None:
            l = []
        orig = [edge[0]]
        for child in node.children:
            edge[0] += 1
            l.append((orig[0], edge[0], child.val))
            self.adj_list(child, l, edge)
        return l


