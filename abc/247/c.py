from functools import lru_cache



n = int(input())


@lru_cache(maxsize=None)
def recur(n):
    if n == 1:
        return "1"
    else:
        return recur(n-1)+" "+str(n)+" "+recur(n-1)
    
print(recur(n))
