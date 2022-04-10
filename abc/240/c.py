n = int(input())

A = list(map(int,input().split()))
ans = 0
dic = {}
for i in reversed(range(n)):
    if A[i] in dic:
        ans += n - 1 - i - dic[A[i]]
        dic[A[i]] += 1
    else:
        ans += n - 1 - i
        dic[A[i]] = 1
print(ans)