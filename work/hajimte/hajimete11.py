import numpy as np

N = int(input())

t = [0] * (N + 1)
x = [0] * (N + 1)
y = [0] * (N + 1)
# print(t)
# [list(i) for i in zip(*xy)]

# 初期状態
t[0], x[0], y[0] = 0, 0, 0

for i in range(N):
    t[i + 1], x[i + 1], y[i + 1] = map(int, input().split())

can = True
for i in range(N):
    dt = t[i + 1] - t[i]
    dist = np.abs(x[i + 1] - x[i]) + np.abs(y[i + 1] - y[i])
    if dt < dist:
        can = False
    if dist % 2 != dt % 2:
        can = False

if can:
    print("Yes")
else:
    print("No")


# import sys
 
# def main():
#     n = input()
#     plans = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
#     plans = [[0, 0, 0], *plans]
#     # print(plans)
#     i = len(plans) - 1
#     while i > 0:
#         current_t, current_x, current_y = plans[i]
#         pre_t, pre_x, pre_y = plans[i-1]
#         diff_t = current_t - pre_t
#         diff_x = current_x - pre_x
#         diff_y = current_y - pre_y
#         if (diff_x + diff_y) % 2 != diff_t % 2:
#             print("No")
#             return
#         if abs(diff_x) + abs(diff_y) > diff_t:
#             print("No")
#             return
 
#         i -= 1
#     print("Yes")
 
 
 
# if __name__ == "__main__":
#     main()