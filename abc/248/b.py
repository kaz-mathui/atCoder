a, b, k = map(int, input().split())
ans = 0
while True:
  if a >= b:
    break
  a = a * k
  ans += 1

print(ans)
