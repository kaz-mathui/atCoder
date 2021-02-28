# N = int(input())

# mikan_list = list(map(int,list(input().split())))
# cand = mikan_list.copy()
# max_list = []
# for i in range(1,N+1):
#     del mikan_list[0:i-1]
#     print('i',mikan_list)
#     cand1 = mikan_list.copy()
#     for j in range(i,N+1):
#         del mikan_list[j:]
#         print('jのなか:mikanlist:',mikan_list)
        
#         eat = min(mikan_list) * len(mikan_list)
#         max_list.append(eat)
#         mikan_list = cand1.copy()
#         print('eat:',eat)
#     mikan_list = cand.copy()
# print(max(max_list))

# N = int(input())

# mikan_list = list(map(int,list(input().split())))
# cand = mikan_list.copy()
# max_list = []
# for i in range(1,N+1):
#     del mikan_list[0:i-1]
#     # print('i',mikan_list)
#     # cand1 = mikan_list.copy()
#     # for j in range(i,N+1):
#     #     del mikan_list[j:]
#         # print('jのなか:mikanlist:',mikan_list)
#     max_table = max(mikan_list)
#     eat = min(mikan_list) * len(mikan_list)
#     max_list.append(eat)
#     # mikan_list = cand.copy()
#     # print('eat:',eat)
#     mikan_list = cand.copy()
# print(max(max_list))


N = int(input())

mikan_list = list(map(int,list(input().split())))
# cand = mikan_list.copy()
max_list = []
ans = 0
for i in range(1,N+1):
    # del mikan_list[0:i-1]
    # print('i',mikan_list)
    x = mikan_list[i-1]
    # cand1 = mikan_list.copy()
    for j in range(i,N+1):
        # del mikan_list[j:]
        x = min(x,mikan_list[j-1])
        eat = x * (j-i+1)
        # max_list.append(eat)
        ans = max(ans,eat)
        # mikan_list = cand1.copy()
        # print('eat:',eat)
    # mikan_list = cand.copy()
print(ans)
