n,w = map(int,input().split())
A = [0,0,0] + list(map(int,input().split()))
 
n += 3
S = set()
 
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if A[i] + A[j] + A[k] <= w:
                S.add(A[i] + A[j] + A[k])
print(len(S) - 1)