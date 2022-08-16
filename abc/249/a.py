a,b,c,d,e,f,x = map(int, input().split())
Ao = 0
Dr = 0
for i in range(x):
  if i%(a+c) < a:
    Ao += b
  if i%(d+f) < d:
    Dr += e
if Ao == Dr:
  print("Draw")
elif Ao > Dr:
  print("Takahashi")
else:
  print("Aoki")