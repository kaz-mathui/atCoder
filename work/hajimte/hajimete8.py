# N = int(input())
# mochi_list = list(int(input()) for _ in range(N))
# # print(mochi_list)
# unique_mochi_list = list(set(mochi_list))
# # print(unique_mochi_list)
        
# print(len(unique_mochi_list))

N = int(input())
D = []

for di in range(1, N+1):
    D.append(int(input()))
D = sorted(D)
D2 = [D[0]]

for i in range(1, len(D)):
    if D[i] == D[i-1]:
        continue
    else:
        D2.append(D[i])

print(len(D2))