from codontab import STANDARD_CODON_TABLE, TABLE_DIFFS

if __name__ == "__main__":
    with open('data/7.dat', 'r') as data_file:
        seq = data_file.readline().strip()
        translated = data_file.readline().strip() + '*'

        non_standard_transs = set([])
        for i in range(0, len(seq), 3):
            curr_subseq = STANDARD_CODON_TABLE[seq[i:i+3]]
            if not curr_subseq == translated[i/3]:
                non_standard_transs.add((seq[i:i+3], translated[i/3]))

        if non_standard_transs.issubset(set([])):
            print 1
        else:

            answer = None
            for i in range(len(TABLE_DIFFS)):
                if non_standard_transs.issubset(TABLE_DIFFS[i]):
                    answer = i
                    break

            if answer is None:
                print 11
            else:
                print answer

