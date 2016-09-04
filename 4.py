from functional import partition, frequencies
import operator

if __name__ == '__main__':
    with open('data/4.ini', 'r') as data_file:
        data = data_file.readline()
        k,L,t = data_file.readline().split(' ')
        k,L,t = int(k), int(L), int(t)

        kmers = [i for i in partition(list(data), k, lambda x: reduce(operator.add, x))]
        kmers_count = frequencies(kmers)
        viable_kmers = set(key for key,val in kmers_count.items() if (val >= t))

        viable_kmer_idxs = {}
        for i in range(len(kmers)):
            if kmers[i] in viable_kmers:
                temp_arr = viable_kmer_idxs.get(kmers[i], [])
                temp_arr.append(i)
                viable_kmer_idxs[kmers[i]] = temp_arr

        L_t_clumps = set()
        for (key,val) in viable_kmer_idxs.items():
            for i in range(len(val) - (t-1)):
                if ((val[i+t-1] - val[i]) <= (L - t)):
                    L_t_clumps.add(key)

        print ' '.join(map(str, L_t_clumps))
