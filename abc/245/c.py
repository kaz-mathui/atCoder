n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = [a[0], b[0]]
for i in range(1, n):
    t = [0, 0]
    for item in s:
        if item == 0: continue
        if abs(item - a[i]) <= k:
            t[0] = a[i]
        if abs(item - b[i]) <= k:
            t[1] = b[i]
    if sum(t) == 0:
        print('No')
        exit()
    s[0], s[1] = t[0], t[1]
print('Yes')
