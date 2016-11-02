from fastamasta import FastaReader
from sequence import edit_dist

if __name__ == "__main__":
    data = [i for i in FastaReader("data/30.fas")]
    a, b = data[0][1], data[1][1]

    print edit_distance(a, b)
