if __name__ == '__main__':
    with open('data/5.ini') as data_file:
        complements = {
                'A' : 'T',
                'C' : 'G',
                'G' : 'C',
                'T' : 'A'
                }

        data = data_file.readline().strip()

        result = ""

        for char in data[::-1]:
            result += complements[char]

        print result


