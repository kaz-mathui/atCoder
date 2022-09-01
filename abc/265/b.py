N, M, T = map(int, input().split())
A = list(map(int, input().split()))
  
XY = []
for m in range(M):
  XY.append(map(int, input().split()))
XY = dict(XY)
  
for (x, a) in enumerate(A):
  T -= a
  if T <= 0:
    print("No")
    exit()
  T += XY.get(x+2, 0)
print("Yes")
