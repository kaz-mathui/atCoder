
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out


X = input()
M = int(input())



x_max = max(map(int,list(X)))
n = x_max+1

if len(X) == 1:
    print(int(int(X) <= M))
    exit()

#二分探索

r = 10**18
while n <= r:
	mid = (n+r) // 2
	if Base_n_to_10(X,mid) <= M:
		n = mid + 1
	else:
		r = mid - 1

print(max(0,r - x_max))

