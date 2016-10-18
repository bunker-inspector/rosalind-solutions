from sequence import hamming_dist

if __name__ == "__main__":
    data_file = open("data/29.dat", 'r')
    A,B = data_file.readline().strip(), data_file.readline().strip()

    print hamming_dist(A, B)
