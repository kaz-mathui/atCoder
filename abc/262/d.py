import sys
from operator import itemgetter
from collections import defaultdict, deque
import heapq
from heapq import heapify, heappop, _heapify_max, heappush
from bisect import bisect_left, bisect_right
import math
import itertools
import copy
 
stdin=sys.stdin
#sys.setrecursionlimit(10 ** 7)
## import pypyjit
## pypyjit.set_param('max_unroll_recursion=-1')
 
ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()
Yp=lambda:print('Yes')
Np=lambda:print('No')
inf = 1 << 60
inf = float('inf')
mod = 10 ** 9 + 7
mod = 998244353
eps = 1e-9
sortkey1 = itemgetter(0)
sortkey2 = lambda x: (x[0], x[1])
 
 
 
###############################################################
 
 
 
N = ip()
A = lp()
ans = 0
 
def f(x):
    global ans
    dp = [[0 for _ in range(x)] for _ in range(x + 1)]
    dp[0][0] = 1
    for a in A:
        for i in range(x - 1, -1, -1):
            for j in range(x):
                dp[i + 1][(j + a) % x] += dp[i][j]
                dp[i + 1][(j + a) % x] %= mod
    ans += dp[-1][0]
    ans %= mod
 
for i in range(1,N + 1):
    f(i)
print(ans)