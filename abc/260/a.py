n,m,x,t,d = map(int,input().split())

if x <= m <= n:
    print(t)
if m < x:
    print(t-((x-m)*d))