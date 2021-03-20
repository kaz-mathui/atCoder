n = input()
n_len = len(n)

if n_len < 4:
    print(0)
    exit()
ans = 0

i = (n_len-1)//3
while i > 1:
    ans += 999 * (1000 ** (i-1)) * (i-1)
    i -= 1
# print(ans)

i = (n_len-1)//3

ans += (int(n) - (1000 ** i) + 1) * (i)

print(ans)