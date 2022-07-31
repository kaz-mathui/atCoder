N=int(input())
A=list(map(int,input().split()))
base=[0,0,0,0]
P=0
for i in range(N):
    base[0]=1
    for j in [3,2,1,0]:
        if base[j]==1:
            if j+A[i]>3:
                P+=1
                base[j]=0
            else:
                base[A[i]+j]=1
                base[j]=0
        else:
            pass
print(P)