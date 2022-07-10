# a = int(input())
# s_1 = int(a / 100)
# s_2 = int((a - s_1 * 100) / 10)
# s_3 = a - s_1 * 100 - s_2 * 100

# sum = s_1 + s_2 + s_3

# print(sum)

a = input()
num = 0
 
for b in a:
    if b == '1':
        num += 1
 
print("{}".format(num))