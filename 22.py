from fastamasta import FastaReader

if __name__ == "__main__":
    seq = FastaReader("data/22.fas").readnext()[1]


    fail_arr = [0] * len(seq)

    for i in range(1, len(seq)):
        j = fail_arr[i-1]
        while (j > 0) and seq[i] != seq[j]:
            j = fail_arr[j-1]
        if (seq[i] == seq[j]):
            j += 1
        fail_arr[i] = j


    for i in fail_arr:
        print i,


