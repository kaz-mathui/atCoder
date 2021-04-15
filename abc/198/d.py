s1 = input()
s2 = input()
s3 = input()

len1 = len(s1)
len2 = len(s2)
len3 = len(s3)
minlen = min(len1, len2,len3)
# print(minlen)
for i in range(10 ** (minlen-1),10 ** len(s3) - 1):
    
