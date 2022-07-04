N, Y = map(int, input().split())
count=0
# if N*10000 == Y:
#     print(N,0,0)
# if N*10000 < Y:
#     print(-1,-1,-1)
for i in range(N+1):
    if i*10000 > Y:
        break
    if count == 1:
        break
    for j in range(N-i+1):
        if i*10000+j*5000 > Y:
            break
        
        if i*10000+j*5000+(N-i-j)*1000 > Y:
            break
        if Y == i*10000+j*5000+(N-i-j)*1000:
            ans = [i,j,N-i-j]
            count +=1
            break
if count != 1:
    print(-1,-1,-1)
else:
    print(ans[0],ans[1],ans[2])

            