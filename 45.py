from collections import Counter
from util import dist, contains

def derive_dl(distances):
    distances = Counter(distances)

    X = set([0])
    width = max(distances)

    while len(distances) > 0:
        y = max(distances)
        if contains(dist(y, X), distances):
            X |= frozenset([y])
            distances -= dist(y, X)
        else:
            X |= frozenset([width - y])
            distances -= dist(width - y, X)
    return sorted(X)

if __name__ == '__main__':
    data = map (int, open("data/45.dat").read().strip().split())

    for i in list(derive_dl(data)):
        print i,
