import math

def LIS(X, N):
	P = [None] * N
	M = [None] * (N+1)

	L = 0
	for i in range(N):
	    lo = 1
	    hi = L
	    while lo <= hi:
		mid = int(math.ceil((lo+hi)/2))
		if X[M[mid]] < X[i]:
		    lo = mid+1
		else:
		    hi = mid-1

	    newL = lo

	    P[i] = M[newL-1]
	    M[newL] = i

	    if newL > L:
		L = newL

	S = [0] * L
	k = M[L]
	for i in range(L-1, -1, -1):
	    S[i] = X[k]
	    k = P[k]

	return S

if __name__ == "__main__":
	df = open("data/23.dat", 'r')

	N = int(df.readline().strip())
	X = map(int, df.readline().strip().split(' '))

        for i in LIS(X, N):
            print i,

        print ""

        for i in LIS(map(lambda x: -x, X), N):
            print abs(i),


