H,W = map(int, input().split())
masu_list = []
# count = 0
start = 0
choten = 0
for i in range(H):
    masu = list(input())
    masu_list.append(masu)
    # if count == 0:
    #     for j in range(len(masu)):
    #         if masu[j] == '#':
    #             count += 1
    #             start = [i,j+1]
    #             break
# print(masu_list)
# print(start)
for i in range(H-1):
    for j in range(W-1):
        # print(masu_list[i][j])
        # print(i,j)
        count = 0
        if masu_list[i][j] == "#":
            count += 1
        if masu_list[i+1][j] == "#":
                count += 1
        if masu_list[i][j+1] == "#":
            count += 1
        if masu_list[i+1][j+1] == "#":
            count += 1
        if count == 1 or count == 3:
            choten += 1
print(choten)

# # #visit each "1" in the adjacent area using a stack
# # while len(stack) != 0:
    
# #     [p,q] = stack.pop()
    
    
        
# #     if p < H -1 and masu_list[p+1][q] == "#":
# #         stack.append([p+1,q])
        
# #     if q < W - 1 and masu_list[p][q + 1] == "#":
# #         stack.append([p,q+1])
    
# #     #mark as visited
# #     grid[p][q] = "0"


# m, n = map(int, input().split())
# A = [input() for _ in range(m)]
# ans = 0
# for i in range(m - 1):
#   for j in range(n - 1):
#     a, b = 0, 0
#     for x, y in [(i, j), (i + 1, j), (i, j + 1),  (i + 1, j + 1)]:
#       if A[x][y] == '#':
#         a += 1
#       else:
#         b += 1
#     if abs(a - b) == 2:
#       print(i,j)
#       ans += 1
# print(ans)