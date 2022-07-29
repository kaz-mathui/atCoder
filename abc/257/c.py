from collections import defaultdict
 
N = int(input())
S = input()
W = list(map(int, input().split()))
WS = [[w, s] for w, s in zip(W, S)]
WS.sort(key=lambda x: x[0])
one = defaultdict(int)
zero = defaultdict(int)
for w, s in WS:
    if s == "1":
        one[w] += 1
    else:
        zero[w] += 1
ans = S.count("1")
WW = list(sorted(list(set(W))))
o = ans
z = 0
for w in WW:
    z += zero[w]
    o -= one[w]
    ans = max(ans, z + o)
print(ans)
