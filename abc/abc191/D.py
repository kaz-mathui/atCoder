X,Y,R = map(float, input().split())
# [(x, y) for x in range(X, R) for y in range(Y, R) if x**2 + y**2 < R**2]
print(len([(x, y) for x in range(int(X), int(R)) for y in range(int(Y), int(R)) if (x-X)**2 + (y-Y)**2 <= R**2]))
