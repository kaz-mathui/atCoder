# # print(pow(10**10,1/4))
# N = int(input())
# count = 0
# hashmap = []

# for a in range(2, 10 ** 5):
#     calc = a**2
#     if calc > N:
#         break
#     if not calc in hashmap:
#         count += 1
#         hashmap.append(calc)

# for a in range(2, 10 ** 4):
#     calc = a**3
#     if calc > N:
#         break
#     if not calc in hashmap:
#         count += 1
#         hashmap.append(calc)


# for b in range(4, 15):

#     for a in range(2, 320):
        
#         calc = a**b
#         if calc > N:
#             break
#         if not calc in hashmap:
#             count += 1
#             hashmap.append(calc)

# print(N-count)


N = int(input())
sq = int(N ** 0.5)
s = set()
count = 0
for a in range(2, 10**5 + 1):
    for b in range(2,10 ** 5+ 1):
        if a ** b > N:
            break
        if not a ** b in s:
            s.add(a ** b)
            count += 1    
        
print(N - len(s))