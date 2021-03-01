n, m, t = map(int, input().split())
charge = n
pre = 0
for i in range(m):
    a, b = map(int, input().split())
    # print(charge)
    charge -= a - pre
    if charge <= 0:
        print("No")
        exit()
    # print(charge)
    charge = min(charge + b - a, n)
    
    pre = b
    # print(charge)
if charge - t + pre <= 0:
    print("No")
    exit()


print("Yes")
