# n = input()
# keta = len(n)
# watch = 0
# if keta % 2 == 0:
#     watch = keta // 2
# else:
#     watch = keta // 2 + 1

# num = ""
# for i in range(watch):
#     num += n[i]
# if int(num+num) <= int(n):
#     print(int(num))
# else:
#     print(int(num)-1)

n = int(input())
count = 0
for i in range(1,n//2+1):
    if int(str(i)+str(i)) <= n:
        count += 1
    else:
        break
print(count)
