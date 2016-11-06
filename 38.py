if __name__ == "__main__":
    data = open("data/38.dat", 'r').readlines()
    n = int(data[0])
    edges = map(lambda tup: (int(tup[0]), int(tup[1])), map(lambda s: s.split(), data[1:]))

    included = [False] * n
    for edge in edges:
        included[edge[0]-1] = True
        included[edge[1]-1] = True

    needed = len(filter(lambda x: not x, included))
    if needed > (n - len(edges)):
        print n - needed - 1
    else:
        print n - len(edges) - 1
