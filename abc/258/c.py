n, q = map(int,input().split())
S = input()
 
x = 0
for _ in range(q):
    i, j = map(int, input().split())
    if i == 1:
        x += j
    else:
        print(S[(j-x-1)%n])