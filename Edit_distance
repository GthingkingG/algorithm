def EDIT(X, Y): #삭제, 삽입만 고려 횟수
    n = len(X)
    m = len(Y)
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        DP[i+1][0] = i+1
    for j in range(m):
        DP[0][j+1] = j+1
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                    DP[i+1][j+1] = DP[i][j]
            else:
                DP[i+1][j+1] = min(DP[i][j+1], DP[i+1][j]) + 1
    return DP[n][m]
def EDIT_sub(X, Y):
    del_cost = 2
    ins_cost = 2
    sub_cost = 3
    n = len(X)
    m = len(Y)
    DP = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        DP[i+1][0] = (i+1) * del_cost
    for j in range(m):
        DP[0][j+1] = (j+1) * ins_cost
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                DP[i+1][j+1] = DP[i][j]
            else:
                DP[i+1][j+1] = min(DP[i][j+1] + del_cost, DP[i+1][j] + ins_cost, DP[i][j] + sub_cost)
    return DP[n][m]

A = ['h','u','m','a','n']
B = ['c','h','i','m','p','a','n','z','e','e'] 
print(EDIT(A,B)) #7

C = ['k','i','t','t','e','n']
D = ['s','i','t','t','i','n','g']
print(EDIT(C,D)) #5

E = ['a', 'b', 'c']
F = ['a', 'b', 'c']
print(EDIT(E, F))  # 예상 결과: 0 (두 문자열이 동일함)

G = ['a', 'b', 'c']
H = ['a', 'b', 'd']
print(EDIT(G, H))  # 예상 결과: 2 -> 삽입, 삭제

I = ['a', 'b', 'c']
J = ['a', 'c', 'b']
print(EDIT(I, J))  # 예상 결과: 2 -< 삭제, 삽입

K = []
L = ['a', 'b', 'c']
print(EDIT(K, L))  # 예상 결과: 3 (빈 문자열에서 세 문자를 추가해야 함)

M = ['a', 'b', 'c']
N = []
print(EDIT(M, N))  # 예상 결과: 3 (세 문자를 삭제해야 함)

O = ['a', 'b', 'c']
P = ['a', 'b', 'c', 'd', 'e']
print(EDIT(O, P))  # 예상 결과: 2 (두 문자를 추가해야 함)

Q = ['a', 'b', 'c', 'd', 'e']
R = ['a', 'b', 'c']
print(EDIT(Q, R))  # 예상 결과: 2 (두 문자를 삭제해야 함)

S = ['x', 'y', 'z']
T = ['a', 'b', 'c', 'x', 'y', 'z']
print(EDIT(S, T))  # 예상 결과: 3 (세 문자를 앞에 추가해야 함)


U = ['a', 'b', 'c', 'x', 'y', 'z']
V = ['x', 'y', 'z']
print(EDIT(U, V))  # 예상 결과: 3 (세 문자를 앞에서 삭제해야 함)

print('word')
Y = list("flaw")
Z = list("lawn")
print(EDIT(Y, Z))  # 예상 결과: 2 (f 삭제, n 추가)

AA = list("intention")
BB = list("execution")
print(EDIT(AA, BB))           #8

CC = list("apple")
DD = list("aple")
print(EDIT(CC, DD))  # 예상 결과: 1 (p 삭제)

EE = list("sunday")
FF = list("saturday")
print(EDIT(EE, FF))  # 예상 결과: 4

print(EDIT_sub(A, B)) #13
