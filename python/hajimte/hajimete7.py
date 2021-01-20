N = int(input())
num_list = list(map(int,input().split()))
# print(num_list)
list.sort(num_list, reverse=True)

for i, j in enumerate(num_list):
    # print('{0}:{1}'.format(i, j))
    if i % 2 != 0:
        num_list[i] = - j
print(sum(num_list))


# import numpy as np
# N = int(input())
# i = list(map(int, input().split()))
# a = np.array(i)

# alice_point = 0
# bob_point = 0

# for i in range(0, N):
#     if(a.size != 0):
#         alice_point += np.amax(a)
#         # print(np.where(a == np.amax(a))[0])
#         a = np.delete(a, np.where(a == np.amax(a))[0][0])
#         # print(a)
#     else:
#         break
#     if(a.size != 0):
#         bob_point += np.amax(a)
#         # print(np.where(a == np.amax(a))[0][0])
#         a = np.delete(a, np.where(a == np.amax(a))[0][0])
#         # print(a)
#     else:
#         break
# diff_point = alice_point - bob_point
# print(diff_point)