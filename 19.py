if __name__ == "__main__":
    data_file = open("data/19.dat", 'r')
    seq, to_find = data_file.readline().strip(), data_file.readline().strip()

    results = []
    chunk_size = len(to_find)
    for i in range(len(seq) - len(to_find)):
        if seq[i : i + chunk_size] == to_find:
            results.append(i + 1)

    for idx in results:
        print idx,