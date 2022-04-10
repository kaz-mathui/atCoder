n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

eat = 0
bite = 0
for i in range(n):
  if(A[i] == B[i]):
    eat += 1
  else:
    if A[i] in B:
      bite += 1

print(eat)
print(bite)