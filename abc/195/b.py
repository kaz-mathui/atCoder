a,b,w = map(int,input().split())

w *= 1000
# min_loop = w//a
# max_loop = w//b
# print(min_loop,max_loop)

# maxを求めに行く

left = w - (a * (w // a))
# print(left)
if left == 0:
    max = w // a
flag = 0
for i in range(1,(w//a)+1):
    left += a
    for j in range(1,(w//b)+1):
        # print(i,j)
        if a * j <= left <= b*j:
            max = (w // a) - i + j
            flag += 1
            break
        if a * j > left:
            break
    if flag == 1:
        break
# print(max)


# minを求めに行く

left = w - (b * (w // b))
# print(left)
if left == 0:
    min = w // b
flag = 0
for i in range(1,(w//b)+1):
    left += b
    for j in range(1,(w//a)+1):
        # print(i,j)
        if a * j <= left <= b*j:
            min = (w // b) - i + j
            flag += 1
            break
        if a * j > left:
            break
    if flag == 1:
        break
if flag == 0:
    print("UNSATISFIABLE")
    exit()
print(min,max)