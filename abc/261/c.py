n, x, y = map(int, input().split())

def red(n):
    if n == 1:
        return 0
    else:
        return red(n-1) + x * blue(n)
 
def blue(n):
    if n == 1:
        return 1
    else:
        return y * blue(n-1) + red(n-1)
 
print(red(n))
