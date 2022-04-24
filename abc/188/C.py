N = int(input())

match = list(map(int, input().split()))

# for i in range(2 ** N):
#     print(match[i])
curr = match.copy()

while len(curr) > 2:
    tmp = []
    for i in range(len(curr)//2):
        a = curr[2 * i]
        b = curr[2 * i + 1]
        tmp.append(max(a, b))
    curr = tmp
    # print(curr)
print(match.index(min(curr))+1)