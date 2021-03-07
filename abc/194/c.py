import itertools
n = int(input())
a = list(map(int,input().split()))

ans = 0
# count = 0

S = sum(a)
S2 = sum(map(lambda x:x*x,a))

kakeru = (S*S -S2)
# print(a)
for e in a:
	ans += e ** 2 * (n-1)
# print(ans)
print(ans -  kakeru)