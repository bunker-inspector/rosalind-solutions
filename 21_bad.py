from fastamasta import FastaReader
from functional import partition

if __name__ == "__main__":
    data= []

    for datum in FastaReader("data/21.fas"):
        data.append(datum[1])

    shortest = ' '*1001
    for i in data:
        if len(i) < len(shortest):
            shortest = i

    data.remove(shortest)
    print data

    for i in range(2, len(shortest) + 1)[::-1]:
        parts = [i for i in partition(shortest, i, str)]
        for part in parts:
            in_all = True
            for datum in data:
                if part not in datum:
                    in_all = False
                    break
            if in_all:
                print part