if __name__ == "__main__":
    data_file = open("data/29.dat", 'r')
    A,B = data_file.readline().strip(), data_file.readline().strip()

    dist = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            dist += 1
    print dist