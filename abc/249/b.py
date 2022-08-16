n, a, b = map(int, input().split())
for i in range(n * a):
    ans = ''
    if (i // a) % 2 == 0:
        
        for j in range(n * b):
            if (j // b) % 2 == 0:
                ans += '.'
            else:
                ans += '#'
    else:
        for j in range(n * b):
            if (j // b) % 2 == 0:
                ans += '#'
            else:
                ans += '.'
    print(ans)