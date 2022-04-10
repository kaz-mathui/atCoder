n = int(input())

tyokin = 0
for i in range(1,n+1):
  tyokin += i
  if tyokin >= n:
    print(i)
    break