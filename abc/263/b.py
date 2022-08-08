n = int(input())
P = list(map(int,input().split()))

cnt = 0
pre_num = P[-1]

while pre_num!=1:
    cnt+=1
    pre_num = P[pre_num-2]

print(cnt+1)