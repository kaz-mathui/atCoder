from collections import defaultdict
s = input()
t = input()

dict = defaultdict(int)
dict_t = defaultdict(int)

for i in range(len(s)):
    dict[s[i]] += 1

for i in range(len(t)):
    dict_t[t[i]] += 1


for key,value in dict_t.items():
    if value < dict[key] or value >= 2 and dict[key] < 2:
        print('No')
        exit()

print('Yes')