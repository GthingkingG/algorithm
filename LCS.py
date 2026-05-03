def LCS(X, Y):
    n = len(X)
    m = len(Y)
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                DP[i+1][j+1] = DP[i][j] + 1
            else:
                DP[i+1][j+1] = max(DP[i][j+1],DP[i+1][j])
    return DP[i+1][j+1]

def LCS_print(X, Y):
    n = len(X)
    m = len(Y)
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                DP[i+1][j+1] = DP[i][j] + 1
            else:
                DP[i+1][j+1] = max(DP[i][j+1],DP[i+1][j])
    str = []
    i = n-1
    j = m-1
    while i >= 0 and j >= 0:
        if X[i] == Y[j]:
            str.append(X[i])
            i += -1
            j += -1
        else:
            if DP[i][j+1] > DP [i+1][j]:
                i += -1
            else:
                j += -1
    str.reverse()
    return str



A = ['a', 'b', 'c', 'b', 'd', 'a', 'b']
B = ['b', 'd', 'c', 'a', 'b', 'a']
print(LCS(A, B))
print(LCS_print(A, B))

