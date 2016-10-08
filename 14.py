from functional import partition, frequencies
from fastamasta import FastaReader

def alphabet(order, length, string='', arr=None):
    if arr is None:
        arr=[]
    if length == 0:
        arr.append(string)
    else:
        for char in order:
            alphabet(order, length-1, string + char, arr)
    return arr

if __name__ == "__main__":
    with open("data/13.dat", 'r') as data_file:
        reader = FastaReader('data/14.dat')
        data = reader.readnext()

        order, size = ['A', 'C', 'G', 'T'], 4
        alph = alphabet(order, size)

        fourmer_count = frequencies(partition(data[1], size, str))

        output = ''
        for word in alph:
            output += str(fourmer_count.get(word, 0)) + ' '

        print output
