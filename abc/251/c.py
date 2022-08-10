 
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = []
 
for i in range(k):
    b = []
    for j in range(i, n, k):
        b.append(a[j])
    b.sort()
    for j in range(i, n, k):
        a[j] = b[int(j/k)]
 
k=a[0]
for i in range(n):
    if k > a[i]:
        print("No")
        exit()
    else:
        k = a[i]
print("Yes")
