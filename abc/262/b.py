n,m = map(int, input().split())
uvlist = [[0 for i in range(n)] for j in range(n)]
# print(uvlist)
for i in range(m):
  u,v = map(int, input().split())
  uvlist[u-1][v-1] = 1
  uvlist[v-1][u-1] = 1
  # print(uvlist)
count = 0

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      ans = 0
      if uvlist[i][j] == 1:
        ans += 1
      if uvlist[j][k] == 1:
        ans += 1
      if uvlist[k][i] == 1:
        ans += 1
      if ans == 3:
        count += 1
        
        # print(i,j,k)
print(count)
