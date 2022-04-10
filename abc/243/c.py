import sys

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]


n = int(input())
X = [0] * n
Y = [0] * n
for i in range(n):
    X[i], Y[i] = map(int, input().split())

S = input()

# for i in range(n):
    
#     if(my_index_multi(Y, Y[i]) == [i]):
#         continue
#     # print(S[my_index_multi(Y, Y[i])[0]])
#     if S[my_index_multi(Y, Y[i])[0]] != S[my_index_multi(Y, Y[i])[1]]:
#         print("Yes")
#         sys.exit(0)
# print("No")
for i in range(n-1):
    for j in range(i+1,n):
        # print(i,j)
        if Y[i] == Y[j] and S[i] == "R" and S[j] == "L" and X[i] < X[j]:
            print("Yes")
            sys.exit(0)
        if Y[i] == Y[j] and S[i] == "L" and S[j] == "R" and X[i] > X[j]:
            print("Yes")
            sys.exit(0)
print("No")
