from math import pow

if __name__ == "__main__":
    data = map(lambda s: s.strip(), open("data/46.dat").readlines())
    n = int(data[0])
    s = data[1]
    A = map(float, data[2].split())

    content = [s.count('G') + s.count('C'), s.count('A') + s.count('T')]

    num_possibilities = n - len(s) + 1

    probs = []
    for a in A:
        probs.append((pow(a*0.5, content[0]) * pow((1-a)*0.5, content[1]))*num_possibilities)

    print ' '.join(map(str, probs))


