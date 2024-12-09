def find_max_sum(A):
    S = [0]*len(A)
    S[0] = A[0]
    for i in range(1, len(A)):
        S[i] = max(S[i-1] + A[i], A[i])
    return max(S)


def prefix_sum(A):
    n = len(A)
    P = [0] * n
    P[0] = A[0]
    for i in range(1, n):
        P[i] = P[i-1] + A[i]
    max_sum = A[0]
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                current_sum = P[i]
            else:
                current_sum = P[i] - P[j-1]
            if max_sum < current_sum:
                max_sum = current_sum
    return max_sum

def max_interval(A,l,r):
    if l>=r : return A[l]
    m = (l + r)//2
    L = max_interval(A,l,m)
    R = max_interval(A,m+1,r)
    M = A[m] + A[m+1]
    left_sum = 0
    right_sum = 0
    current_sum = 0
    for i in range(m-1,-1,-1):
        current_sum += A[i]
        if left_sum < current_sum:
            left_sum = current_sum
    current_sum = 0
    for j in range(m+2, len(A)):
        current_sum += A[j]
        if right_sum < current_sum:
            right_sum = current_sum
    M += (left_sum + right_sum)
    return max(L, R, M)
    

A = [-41, 77, -12, -4, 2, 31,-11, -2]
B = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
C = [1, 2, 3, 4, 5]
D = [-7, -2, -3, -4, -5]
E = [42]
F = [-2, 0, -1, 3]
G = [-1, 2, 3, -2, 5, -3] 
print(find_max_sum(A))
print(prefix_sum(A))
print(max_interval(A,0,len(A)-1))
print(find_max_sum(B))
print(prefix_sum(B))
print(max_interval(B,0,len(B)-1))
print(find_max_sum(C))
print(prefix_sum(C))
print(max_interval(C,0,len(C)-1))
print(find_max_sum(D))
print(prefix_sum(D))
print(max_interval(D,0,len(D)-1))
print(find_max_sum(E))
print(prefix_sum(E))
print(max_interval(E,0,len(E)-1))
print(find_max_sum(F))
print(prefix_sum(F))
print(max_interval(F,0,len(F)-1))
print(find_max_sum(G))
print(prefix_sum(G))
print(max_interval(G,0,len(G)-1))
