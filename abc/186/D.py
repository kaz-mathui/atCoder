n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
ans = 0
for i in range(n):
  ans += (n-i-1) * a[i]
  ans -= i * a[i]
  print(i,n-i-1,a[i],ans)
print(ans)