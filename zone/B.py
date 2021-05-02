n, d, h = map(int, input().split())

maxnum = 0
ans = 0
for i in range(n):
    di, hi = map(int, input().split())
    ans = max(ans,(di * h - d * hi) / (di - d))

print(ans)
