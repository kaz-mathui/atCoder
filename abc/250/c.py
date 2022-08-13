
n = int(input())
ST = [list(input().split()) for _ in range(n)]
 
ans_t = 0
 
already_shown = set()
 
for i, st in enumerate(ST):
    s, t = st
    if s in already_shown:
        continue
    if ans_t < int(t):
        ans_t = int(t)
        ans = i + 1
    already_shown.add(s)
 
print(ans)