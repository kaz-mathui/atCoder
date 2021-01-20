N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
n=0
cn=0
max_alist=0
max_blist=0
A_max = A_list[0]
for i in range(1,N+1):
    candidates=[]
    if A_max < A_list[i-1]:
        A_max = A_list[i-1]
    candidate = A_max*B_list[i-1]
    
    candidates.append(candidate)
    # for j in range (1,i+1):
    #     if max_alist < A_list[j-1]:
    #         max_alist = A_list[j-1]
    #         candidate = A_list[j-1]*B_list[i-1]
    #         candidates.append(candidate)
    #         print('i:',i,'j:',j)
    # if max_blist < B_list[i-1]:
    #     max_blist = B_list[i-1]
    #     candidates.append(max_alist*B_list[i-1])
    #     print('i:',i,'j:',j)
    candidates.append(cn)
    cn = max(candidates)
    print(cn)
    