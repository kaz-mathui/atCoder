# S = list(input())
# count = 0
# while True:
#     cnt = 0
#     i = 1
#     for i in range(len(S)-2,0,-1):
#         # print(i)
#         if S[i-1] == S[i] and S[i-1] != S[i+1]:
#             S[i+1] = S[i-1]
#             count += 1
#             cnt += 1
#     # print(S)
#     if cnt == 0:
#         break
# print(count)

# from typing import List
# # str = ['a','g','f']
# # str[3:] = ['a','g','f'][2:]

# # print(str)
# arr = 0
# def changeRight(s:str, i:int,S:List[str]):
#     arr = 0
    
#     # print(S)
#     return S

# S = list(input())
# count = 0

# for i in range(len(S)-2,0,-1):
#     # print(i)
#     if S[i-1] == S[i]:
#         for j in range(i+1,len(S)):
#             if S[j] != S[i]:
#                 arr += 1
#                 S[j] = S[i]
#                 # print(S[i+1:])
#     # print(S)
# # print(S)

# print(arr)





S = input()

alphabet_cnt = [0] * 26

ans = 0

for i in range(len(S)-1,0,-1):
    c_id = ord(S[i]) - ord('a')
    if S[i] == S[i-1]:
        so_far = sum(alphabet_cnt)
        ans += so_far-alphabet_cnt[c_id]
        for j in range(26):alphabet_cnt[j] = 0
        alphabet_cnt[c_id] = so_far

    alphabet_cnt[c_id] += 1
print(ans)
