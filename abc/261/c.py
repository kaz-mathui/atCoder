n = int(input())
s_list = [input() for _ in range(n)]
dictionary = {}
for s in s_list:
    if s not in dictionary:
        print(s)
        dictionary[s] = 1
    else:
        print(f'{s}({dictionary[s]})')
        dictionary[s] += 1