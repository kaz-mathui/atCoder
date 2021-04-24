# from collections import deque

n = int(input())
s = list(input())
q = int(input())
# d = deque(s)
# print(d)
tbool = False
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1:
        if tbool:
            if a <= n:
                if b <= n:
                    sa = s[a+n-1]
                    s[a+n-1] = s[b+n-1]
                    s[b+n-1] = sa     
                else:
                    sa = s[a+n-1]
                    s[a+n-1] = s[b-n-1]
                    s[b-n-1] = sa     
            else:
                sa = s[a-n-1]
                s[a-n-1] = s[b-n-1]
                s[b-n-1] = sa
        else:
            sa = s[a-1]
            s[a-1] = s[b-1]
            s[b-1] = sa
    else:
        if tbool:
            tbool = False
        else:
            tbool = True
if tbool:
    s = s[n:] + s[:n]
print("".join(s))