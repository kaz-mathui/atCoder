import numpy as np

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum = a + b

u, counts = np.unique(sum, return_counts=True)
# print(counts,u)

ans = []
for i in range(len(counts)):
    if counts[i] == 1:
        ans.append(str(u[i]))
        # print(u[i])

L=' '.join(ans)
print(L)
