N = int(input())
A = [list(map(int, list(input()))) for _ in range(N)]
 
max_li = []
max_v = -1
 
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == l == 0:
                    continue
                r = 0
                for m in range(N):
                    r = r * 10 + A[(i + k * m) % N][(j + l * m) % N]
                ans = max(ans, r)
print(ans)
