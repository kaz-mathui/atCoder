from collections import Counter
 
n, k = map(int, input().split())
c = Counter(map(int, input().split()))
 
base = min(c[0],k)
prev, ans = 0, 0
while c[prev]:
    print("base", base)
    ans += base
    prev += 1
    base = min(base, c[prev])
print(ans)


# import collections

# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
# sum_box=[0]

# A_list.sort()
# print(A_list)

# c = len(collections.Counter(A_list))
# sum = 0
# count=0
# # count0 = A_list.count(0)
# for i in range(c):
    
#     counti = min(A_list.count(i),K)
#     if A_list.count(i+1) <= count:
#         break
#     if counti > A_list.count(i+1):
#         sum += counti - A_list.count(i+1)
#         count+=1
#         print('i:',i)
#         print('sum:',counti - A_list.count(i+1))
# print(sum)
    
# # count0 = A_list.count(0)
# # for i in range(1,count0+1):
# #     K_box = []
# #     j=0
# #     A_list_num = 0
# #     while A_list_num in A_list: 
        
# #         index = A_list.index(A_list_num)
# #         K_box.append(A_list[index])
# #         A_list[index] = -1
# #         A_list_num += 1
# #     if K_box == []:
# #         sum_box.append(0)
# #     else:
# #         sum_box.append(max(K_box)+1)
# #         # print(K_box)
# # # print(sum_box)
# # print(sum(sum_box))