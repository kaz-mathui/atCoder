import collections

str = 'abbccdddefg'

str_list = list(str)

c = collections.Counter(str_list)
print(c)