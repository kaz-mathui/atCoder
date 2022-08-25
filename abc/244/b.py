n = input()
a = list(map(int, input().split()))
 
a.sort()
ans = 0
 
if a[0] != 0:
    print(0)
    exit()
 
for i in a:
    if i - ans == 1:
        ans += 1
    elif i - ans > 1 :
        print(ans+1)
        exit()
 
print(ans+1)