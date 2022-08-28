N = int(input())
permutation = set(list(range(1, 2 * N + 1 + 1)))
while True:
    print(permutation.pop())
    
    n = int(input())
    if n == 0:
        break
    permutation.remove(n)