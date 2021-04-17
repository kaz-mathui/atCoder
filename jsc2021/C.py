
import math
import collections

def make_divisors(n):
    divisors  = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
        i += 1
    return divisors

a,b = map(int,input().split())

# print(math.gcd(a, b))

table = []
for i in range(b,a-1,-1):
        table += make_divisors(i)

c = collections.Counter(table).most_common()[::-1]
# print(c)
ans = 1
for j in c:
        if j[1] >= 2:
                ans = max(ans,j[0])
print(ans)



        
#         j = 2
#         while j * j <= i:
#                 if i%j == 0:
#                         table.append(j)
#                         table.append(i//j)
#                 j += 1
        
# c = collections.Counter(table)

# print(c)