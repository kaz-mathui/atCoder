
def is_palindrome(n):
    flag = True
    for i in range(len(n)):
        if n[i] != n[len(n)-i-1]:
            flag = False
    return flag

n = input()
lenn = len(n)
ans = False
for i in range(lenn):
    ans = is_palindrome(n)
    if ans == True:
        break
    n = '0' + n
if ans == False:
    print('No')
else:
    print('Yes')
    