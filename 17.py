from trie import Trie

if __name__ == "__main__":
    with open("data/17.dat", 'r') as data_file:
        data = []
        for line in data_file:
            data.append(line.strip())
        t = Trie(data)
        res = t.adj_list()
        for r in res:
            print r[0], r[1], r[2]
