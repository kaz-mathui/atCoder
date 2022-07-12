
S = list(input())
T = list(input())
 
S_count = []
count = -1
str = ''
for i in S:
    if str != i:
        str = i
        S_count.append([str, 1])
        count += 1
    else:
        S_count[count][1] += 1
 
T_count = []
count = -1
str = ''
for i in T:
    if str != i:
        str = i
        T_count.append([str, 1])
        count += 1
    else:
        T_count[count][1] += 1
 
ans = 'Yes'
count = 0
for j in S_count:
    if j[0] != T_count[count][0]:
        ans = 'No'
        break
    elif j[1] == 1 and T_count[count][1] != 1:
        ans = 'No'
        break
    elif j[1] > T_count[count][1]:
        ans = 'No'
        break
    count += 1
 
if len(S_count) == len(T_count):
    print(ans)
else:
    print('No')
