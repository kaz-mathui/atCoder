S = input()
num = 0
flag = 0
for s in S:
    num += 1
    if s.islower() and num % 2 == 1:
        continue
    if not s.islower() and num % 2 == 0:
        continue
    else:
        print("No")
        flag = 1
        break
if flag == 0:
    print("Yes")
