import itertools
N,M = map(int,input().split())
L = [i for i in range(1,M+1)]
for l in itertools.combinations(L,N):
  print(*list(l))