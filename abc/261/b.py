n = int(input())
g = [list(input()) for _ in range(n)]
a = True
# print(g)
for y in range(n):
  for x in range(n):
    if x==y and g[y][x] != "-":
      a=False
    if g[y][x]=="W" and g[x][y]!="L":
      a=False
    if g[y][x]=="L" and g[x][y]!="W":
      a=False
    if g[y][x]=="D" and g[x][y]!="D":
      a=False
print("correct" if a else "incorrect")