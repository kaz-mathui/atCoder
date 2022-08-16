n, q = map(int, input().split())
data = [int(input()) for _ in range(q)] 
A = list(range(n+1))
index = list(range(n+1))

for i in data:
  p1 = index[i]
  if p1 != n:
    p2 = p1 + 1
  else:
    p2 = p1 - 1
  y = A[p2]
  A[p1],A[p2] = A[p2],A[p1]
  index[i] = p2
  index[y] = p1
  

print(*A[1:])