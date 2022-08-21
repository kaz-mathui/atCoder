import math
x, y = map(int, input().split())
a = math.sqrt(x ** 2 + y ** 2)
print(x / a, y / a)