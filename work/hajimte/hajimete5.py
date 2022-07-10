is_divisible = lambda x: 1 if x == 0 else 0
A, B, C, X = (int(input()) for _ in range(4))
# print(lambda parameter_list: expression)
ans = 0
for i in range(A+1):
    Y = X - 500*i
    
    if Y < 0:
        break
    
    for j in range(B+1):
        Z = Y - 100*j
            
        if 0 <= Z <= C*50:
            ans += is_divisible(Z%50)
            
        elif Z <= 0:
            break
                    
print(ans)
            
# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())
# count = 0
# sum = 0
# list = [a,b,c]
# for i in range(a+1):
#     for j in range(b+1):
#         for k in range(c+1):
#             sum += 500*i+100*j+50*k
#             if sum == x:
#                 count+=1
#                 # print(i,j,k)
#                 sum = 0
#             else:
#                 sum = 0
# print(count)
            




# while (sum <= x - 500) and (a > 0):
#     sum += 500
#     a -= 1
#     if sum == x:
#         count =+ 1
#         sum = 0
# while (sum <= x - 100) and (b > 0):
#     sum += 100
#     b -= 1
#     if sum == x:
#         print(100)
#         count =+ 1
#         sum = 0
    
# while (sum <= x - 50) and (c > 0):
#     sum += 50
#     c -= 1
#     if sum == x:
#         print(50)
#         count =+ 1
#         sum = 0
# print(count)