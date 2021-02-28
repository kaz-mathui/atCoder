N,X = map(int, input().split())
A_list = list(map(int, list(input().split())))
remove_list = [A for A in A_list if A != X]
for i in remove_list:
    print(i,end=' ')
print()