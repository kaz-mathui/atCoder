X,Y,N = map(int,input().split())
m = N//3
n = N%3
ans = min(X*m*3, Y*m)
ans += X*n
print(ans)
