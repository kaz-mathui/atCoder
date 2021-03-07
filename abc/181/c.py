n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]

def on_line(a,b,c):
    a[0] -= c[0]
    b[0] -= c[0]
    a[1] -= c[1]
    b[1] -= c[1]
    return a[0]*b[1] == a[1]*b[0]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if on_line(points[i][:],points[j][:],points[k][:]):
                print("Yes")
                exit()
print("No")