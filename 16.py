def rabbit_pop(n, m, k=1):
    cache = [1, 1, 1, 2]
    if n < 4:
        return cache[n]

    for i in xrange(4, n+1):
        nxt = cache[i - 1] + cache[i - 2]
        if (i - m) > 0:
            nxt -= cache[i - (m+1)]
        cache.append(nxt)
    return cache[len(cache) - 1]

if __name__ == "__main__":
    print rabbit_pop( ??? , ??? )