def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr

n = int(input())
x_list = list(map(int,input().split()))

soinsu = []

# for i in range(1,51):
#     print(i,factorization(i))

for i in range(n):
    add_cal = []
    count = 0
    # print(factorization(x))
    for soin in factorization(x_list[i]):
        # print(soin)
        if not soin in soinsu:
            add_cal.append(soin)
        else:
            count += 1
            break
    if count == 0:
        # print(add_cal)
        add_cal.sort()
        soinsu.append(add_cal[0])
ans = 1

soinsu.sort()
for j in soinsu:
    ans *= j
# print(soinsu)
print(ans)