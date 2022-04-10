from itertools import combinations



n = int(input())
a_list = list(map(int, input().split()))

a = set(combinations(range(n), 2))

results = {}
for a in a_list:
    results.setdefault(str(a)[len(str(a))-2:len(str(a))], []).append(a)
# print(results)
ans = 0

for result in results.values():
    if len(result) == 1:
        continue
    # print(result)
    for i in list(combinations(result, 2)):
        # print(i)
        if (i[0] - i[1]) % 200 == 0:
            ans += 1

print(ans)

# ans = 0
# for i in a:
#     if (a_list[i[0]] - a_list[i[1]]) % 200 == 0:
#         ans += 1
# print(ans)


n = int(input())
a_list = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        # print(i,j)
        if ((a_list[i] - a_list[j]) % 200 == 0):
            ans += 1
print(ans)