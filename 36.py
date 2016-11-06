class Node:
    def __init__(self):
        self.left = None
        self.right = None

    def add_leaf(self, species, characters):
        node = self
        for character in characters[:-1]:
            if character:
                if node.right is None:
                    node.right = Node()
                node = node.right
            else:
                if node.left is None:
                    node.left = Node()
                node = node.left
        last = characters[-1]
        if last:
            if node.right is None:
                node.right = Leaf()
            leaf = node.right
        else:
            if node.left is None:
                node.left = Leaf()
            leaf = node.left
        leaf.add_species(species)

    def newick(self):
        result = []
        ln = rn = None
        if self.right:
            rn = self.right._newick()
        if self.left:
            ln = self.left._newick()
        if ln is not None:
            if rn is not None:
                result = ln + rn
        elif rn is not None:
            result = rn
        return self._compress(result)

    def _newick(self):
        ln = rn = None
        if self.right:
            rn = self.right._newick()
        if self.left:
            ln = self.left._newick()
        if ln is not None:
            if rn is not None:
                return [ln, rn]
            return [ln]
        elif rn is not None:
            return [rn]
        return None

    def _compress(self, result):
        if isinstance(result, list):
            if len(result) == 1:
                return self._compress(result[0])
            return [self._compress(sub) for sub in result]
        else:
            return result

class Leaf:
    def __init__(self):
        self.species = None

    def add_species(self, species):
        if self.species is None:
            self.species = [species]
        else:
            self.species.append(species)

    def newick(self):
        return self.species or []

    def _newick(self):
        return self.species

if __name__ == '__main__':
    root = Node()

    data = map(lambda s: s.strip(), open("data/36.dat", 'r').readlines())
    species = data[0].split()
    characters = map(list,(map(lambda *xs: map(int, xs),  *data[1:])))

    for sp, ch in zip(species, characters):
        root.add_leaf(sp, ch)
    print(root.newick())
