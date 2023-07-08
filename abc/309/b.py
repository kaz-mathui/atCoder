N = int(input())
A = []
for _ in range(N):
    A.append(input())
# print(A)
# print(A[0][3])
B = [['0' for i in range(N)] for j in range(N)]

for j in range(N-1):
    B[0][j+1] = A[0][j]
    B[j+1][N-1] = A[j][N-1]
    B[N-1][N-2-j] = A[N-1][N-1-j]
    B[N-2-j][0] = A[N-1-j][0]
for i in range(1, N-1):
    for j in range(1, N-1):
        B[i][j] = A[i][j]

for s in B:
    print(''.join(s))
# print(B)
