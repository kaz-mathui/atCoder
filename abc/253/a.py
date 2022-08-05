S=lambda:input().split()
M=lambda:map(int,input().split())
L=lambda:list(map(int,input().split()))
O=lambda:map(int,open(0).read().split())
 
a=L()
b=a[1]
a.sort()
print("Yes" if a[1]==b else "No")
