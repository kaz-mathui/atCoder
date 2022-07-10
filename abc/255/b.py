import math
n, k = map(int, input().split())
A = list(map(int, input().split()))
men = []
for i in range(n):
  x,y = map(int, input().split())
  men.append([x,y])
ans = 0
for i in range(n):
  m = 20000000
  ser_x = men[i][0]
  ser_y = men[i][1]  
  for a in A: 
    tar_x = men[a-1][0]
    tar_y = men[a-1][1]
    dis = math.sqrt(abs(tar_x - ser_x) ** 2 + abs(tar_y - ser_y) ** 2)
    m = min(m,dis)
  ans = max(ans,m)
  
print(ans)
