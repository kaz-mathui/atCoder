N,K = map(int, input().split())

def g1(x:int) -> int:
    x_list = sorted(list(str(x)),reverse=True)
    return int(''.join(x_list),10)

def g2(x:int) -> int:
    x_list = sorted(list(str(x)))
    return int(''.join(x_list),10)

def f(x:int) -> int:
    return g1(x)-g2(x)


for i in range(K):
    N = f(N)

print(N)
