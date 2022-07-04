import numpy as np
N = input()
A_list = np.array(list(map(int, input().split())))
B_list = np.array(list(map(int, input().split())))

if np.dot(A_list,B_list) == 0:
    print('Yes')
else:
    print('No')