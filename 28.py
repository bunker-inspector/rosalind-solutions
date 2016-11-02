if __name__ == "__main__":
    data = open("data/28.fastq", 'r').readlines()

    for ln in ['>' + data[i][1:] + data[i+1] for i in range(0, len(data), 4)]: print ln
