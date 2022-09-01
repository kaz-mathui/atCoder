N = int(input())
x = N
 
i = N // 998244353
 
x -= 998244353 * i
 
if x >= 998244353:
        x -= 998244353
elif x < 0:
        x += 998244353
 
print(x)