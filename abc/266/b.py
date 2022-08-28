n=int(input())
t=list(input())
s=[0,0]
d=[1,-1,-1,1]
i=0
for tt in t:
  if tt=='S':
    s[i%2]+=d[i%4]
  else:
    i+=1
print(*s)
