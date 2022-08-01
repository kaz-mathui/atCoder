def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


n = int(input())
a_list = list(map(int,input().split()))
conv = 0
ans = 0
for i in range(n):
    if a_list[i] == i+1:
        conv += 1
        continue
    if a_list[a_list[i]-1] == i+1:
        ans += 1
# print(ans,conv)
ans = ans // 2
if conv <= 1:
    print(ans)
else:
    ans = ans + cmb(conv,2)
    print(ans)