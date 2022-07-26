a, b, c, d = map(int,input().split())
a = max(a, c)
c = min(b, d)
print(c - a if c - a > 0 else 0)