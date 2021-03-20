n,m,q = map(int,input().split())
baggage = []
for _ in range(n):
    w,v = map(int,input().split())
    baggage.append([w,v])

print(baggage[1][0])

boxes= list(map(int,input().split()))

ans = []

for _ in range(q):
    l , r = map(int,input().split())
    for i in range(m):
        if l-1 <= i <= r-1:
            continue
        else:
            
