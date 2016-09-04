from sequence import bp_counts

if __name__ == '__main__':
    data = None
    with open('data/3.ini', 'r') as data_file:
        data = data_file.readline().strip()

    counts = bp_counts(data)
    print '%d %d %d %d' % (counts['A'], counts['C'],
            counts['G'], counts['T'])
