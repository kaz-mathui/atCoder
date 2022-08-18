from itertools import combinations
 
 
N, K = map(int, input().split())
 
S = [input() for _ in range(N)]
 
ans = 0
for r in range(N):
    for comb in combinations(S, r+1):
        cnt = [0]*26
        for s in comb:
            for c in s:
                cnt[ord(c) - ord('a')] += 1
        ans = max(ans, cnt.count(K))
 
print(ans)