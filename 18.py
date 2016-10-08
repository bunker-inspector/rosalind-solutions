import math

if __name__ == "__main__":
    data_file = open("data/18.dat", 'r')

    s, A = data_file.readline().strip(), map(float, data_file.readline().split())

    B = []
    for val in A:
        m_prob, gc_prob, at_prob = 0.0, math.log10(val/2), math.log10((1.0-val)/2)
        for char in s:
            if char in ['G', 'C']:
                m_prob += gc_prob
            else:
                m_prob += at_prob
        B.append(m_prob)
    for val in B:
        print round(val, 3),