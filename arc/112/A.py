T = int(input())
input_list = []
for i in range(T):
    L, R = map(int, input().split())
    input_list.append([L,R])
# print(input_list)


for j in range(T):
    sum = 0
    L,R = input_list[j]
    N = R - L 
    # for i in range(L,N+1):
    #     # print(i)
    #     B = i
    #     C = R - B
        
    #     sum += R - L - i + 1
    if R - 2*L >= 0:
        sum = (N**2-2*N*L+L**2+3*N-3*L+2)/2
        print(int(sum))

    else:    
        print(0)        
    # 6-4=4

    # 4~2

    # (6-2)-2+1