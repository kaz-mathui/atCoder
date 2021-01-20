S = input()
T = ''
# print(S[-7:])
# print(S[-5:])
# print(S[:-5])
for i in range(100000):
    # print(i)
    if 'dreamer' in S[-7:]:
        # print(S[-7:])
        S = S[:-7]
        T = S[-7:] + T
    elif 'eraser' in S[-6:]:
        S = S[:-6]
        T = S[-6:] + T
    elif 'dream' in S[-5:] or 'erase' in S[-5:]:
        S = S[:-5]
        T = S[-5:] + T
    else:
        break
 
 
if S == '':
    print('YES')
else:
    print('NO')