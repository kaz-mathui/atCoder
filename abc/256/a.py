
r, c = map(int, input().split())
a = []
for i in range(2):
    b = list(map(int, input().split()))
    a.append(b)
print(a[r-1][c-1])
