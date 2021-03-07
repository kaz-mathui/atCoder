import itertools

n,k = map(int,input().split())

data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
# print(data)

l = []
for i in range(n-1):
    l.append(i+2)

p_list = list(itertools.permutations(l, n-1))

# print(p_list)

ans = 0

for j in p_list:
    time = 0
    time += data[0][j[0]-1]
    for m in range(1,n-1):
        time += data[j[m-1]-1][j[m]-1]
    time += data[j[n-2]-1][0]
    # print(time)
    if time == k:
        ans += 1


print(ans)