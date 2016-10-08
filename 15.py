def rabbit_pop(n, k=1):
    if n <= 2:
        return 1
    else:
        return k * rabbit_pop(n-2, k) + rabbit_pop(n-1, k)

if __name__ == "__main__":
    print rabbit_pop(5, 3)