from codontab import STD_RNA_CODON_TAB

if __name__ == '__main__':
    with open('data/9.dat', 'r') as data_file:
        seq = data_file.readline().strip()
        translated = ''

        for i in range(0, len(seq), 3):
            translated += STD_RNA_CODON_TAB[seq[i:i+3]]

        print translated[:-1]
