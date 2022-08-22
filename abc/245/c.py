N,K,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    m = min(K, A[i]//X)
    A[i] -= X*m
    K -= m
A.sort(reverse=True)
for i in range(N):
    if 0 < K:
        A[i] = 0
        K -= 1
 
print(sum(A))