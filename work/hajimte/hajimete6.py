# N, A, B = map(int, input().split())
# # print(N,A,B)
# list = []

# for num in range(N+1):
#     # print(num)
#     ichi = num % 10
#     # print(ichi)
#     if ichi > B:
#         continue
#     zyu = (num - ichi) % 100
#     # print(zyu)
#     if zyu/10 +ichi > B:
#         continue
#     hyaku = (num - zyu-ichi)%1000
#     # print(hyaku)
#     if zyu/10 + ichi + hyaku/100 > B:
#         continue
#     sen = (num -hyaku- zyu-ichi)%10000
#     # print(sen)
#     if zyu/10 + ichi +sen/1000 +hyaku/100 > B:
#         continue
#     man = (num -sen- hyaku-zyu-ichi)
#     # print(man)
#     if zyu/10 + ichi +sen/1000 +hyaku/100 + man/10000 > B:
#         continue
#     if zyu/10 + ichi +sen/1000 +hyaku/100 + man/10000 < A:
#         continue
#     list.append(num)
# # print(list)
# print(sum(list))

N, A, B = map(int, input().split())
 
ans = 0
for n in range(1, N+1):
    sum = 0
    for x in str(n):
        print(x)
        sum += int(x)
        
    
    if A <= sum <= B:
        ans += n
        
print(ans)