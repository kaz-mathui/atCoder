from collections import deque
q = int(input())
d = deque([])
# for i in range(2):
#     d.append([1,2])
# # print(d)
# i, j = d.popleft()
# print(i,j)
# # d.extend([1]*1000000000)

for i in range(q):
    s = input()
    if s[0] == '1':
        a, x, c = map(int, s.split())
        d.append([x,c])
            
    if s[0] == '2':
        a, c = map(int, s.split())
        sum = 0
        while True:
            # print(d)
            x,c_1 = d.popleft()
            if c_1 < c:
                c = c - c_1
                sum += x * c_1
                continue
            elif c_1 == c:
                sum += x * c_1
                break
            elif c_1 > c:
                sum += x * c
                c_1 = c_1 - c
                d.appendleft([x,c_1])
                break
        print(sum)
        
