N, M, D, K = map(int, input().split())
roads = []
vertex = []
for _ in range(M):
    u, v, w = map(int, input().split())
    roads.append((u, v, w))
for _ in range(N):
    x, y = map(int, input().split())
    vertex.append((x, y))
ans = []
i = 1
j = 1
for _ in range(1, M+1):
    if j <= K:
        ans.append(i)
    else:
        i += 1
        j = 1
        ans.append(i)
    j += 1

print(*ans, sep=" ")
