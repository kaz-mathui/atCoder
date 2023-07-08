n, k = map(int, input().split())
AB = {}
for i in range(n):
    ai, bi = map(int, input().split())
    if ai in AB.keys():
        AB[ai] += bi
    else:
        AB[ai] = bi
# print(AB)

# for i in range(n):
sort_ab = sorted(AB.items(), reverse=True)
# print(sort_ab[0][1])
sum = 0
for i in range(n):
    sum += sort_ab[i][1]
    # if sum == k:
    #     print(sort_ab[i][0])
    #     exit(0)
    if sum > k:
        print(sort_ab[i][0]+1)
        exit(0)

print(1)
