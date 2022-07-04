def memoize(f): #メモ化関数
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func

@memoize
def memFib(n):
    if ( n<=1 ):
        return 1
    else:
        return memFib(n-2) + memFib(n-1)

print(memFib(100))


# import numpy as np
# def matFib(n):
#     m = np.matrix('1 1 ; 1 0') ** n
#     print(m)
#     return m.item(0)

# print(matFib(10))


# def endFib(n, a1 = 1, a2 = 0):
#     if (n < 1): 
#         return a1
#     else:
#         return endFib(n-1, a1 + a2, a1)

# print(endFib(3))



# #単純な再帰
# def simFib(n):
#     if ( n<=1 ):
#         return 1
#     else:
#         return simFib(n-2) + simFib(n-1)
# print(simFib(10))




# #最大公約数
# def gcd(a,b):
#     if ( b==0 ):
#         return a
#     else:
#         print(a,b)
#         return (gcd(b, a%b))
        

# #結果
# print(gcd(324322323,43254213))





# カイじょー

# def easyFact(n):
#     if ( n==0 ): 
#         return 1
#     else: 
#         return n*easyFact(n-1)

# #結果
# print([easyFact(i) for i in range(10)])

