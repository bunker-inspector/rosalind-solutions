from collections import Counter

def find_last(my_list, term):
    if term in my_list:
        return (len(my_list) - 1) - my_list[::-1].index(term)
    else:
        return -1

def fact(n):
    result = 1
    for i in range (2, n):
        result *= i
    return result


def dist(y, S):
    return Counter(abs(y-s) for s in S)

def contains(a, b):
    return all(a[x] <= b[x] for x in a)
