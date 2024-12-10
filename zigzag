def zig_zag(A):
    n = len(A)
    high = [0]*n
    low = [0]*n
    high[0] = 1
    low[0] = 1
    max_len = 1
    for k in range(1, n):
        for j in range(k):
            if A[j] > A[k]:
                low[k] = max(low[k], high[j] + 1)
            if A[j] < A[k]:
                high[k] = max(high[k], low[j] + 1)
    for k in range(n):
        if max_len < max(low[k],high[k]):
            max_len = max(low[k], high[k])
    return max_len

A = [1, 7, 4, 9, 2, 5]
B = [1, 17, 5, 10, 13, 15, 5, 16, 8]
C = [1,2,3,4,5,6,7,8]
D = [2, 1, 5, 3, 4, 7, 6, 8, 3, 9, 10, 4, 5]

print(zig_zag(A))
print(zig_zag(B))
print(zig_zag(C))
print(zig_zag(D))
