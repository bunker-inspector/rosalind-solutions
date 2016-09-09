if __name__ == '__main__':
    with open('data/8.dat', 'r') as data_file:
        seq = data_file.readline().strip()
        print seq.replace('T', 'U')
