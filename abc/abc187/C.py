N = int(input())

dic = set()
for i in range(N):
    str = input()
    dic.add(str)

# print(dic[0])

for i in dic:
    if i[0] == "!":
        if i[1:] in dic:
            print(i[1:])
            exit()
print("satisfiable")

