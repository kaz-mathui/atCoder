
x, a, d, n = map(int, input().split())

fir_dis = x - a
sec_dis = x - (a + d)
max_dis = x - (a + d * (n-1))

if fir_dis <= sec_dis:
    print(abs(fir_dis))
    exit()
if fir_dis * max_dis > 0:
    print(abs(max_dis))
    exit()
ans = 20000000
for i in range(-d, d + 1):
    can = 0
    if (x + i - a) % d == 0:
        can = abs(i)
        ans = min(ans,can)

print(ans)