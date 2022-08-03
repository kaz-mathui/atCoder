n = int(input())
X = []
for i in range(n):
  A = []
  for j in range(i+1):
    if j == 0 or j == i:
      A.append(1)
      continue
    A.append(X[i-1][j-1]+X[i-1][j])
  print(*A,sep=' ')
  X.append(A)