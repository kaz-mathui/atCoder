n = int(input())
myoji_list = []
name_list =[]

for i in range(n):
  s,t = input().split()
  myoji_list.append(s)
  name_list.append(t)
ans_1 = 0
for i in range(n):
  ans = 0
  for j in range(n):
    if i == j:
      continue
    # print(myoji_list[i],name_list[i],myoji_list[j],name_list[j])
    if (myoji_list[i] == myoji_list[j] or myoji_list[i] == name_list[j]):
      ans += 1
    if (name_list[i] == name_list[j] or name_list[i] == myoji_list[j]):
      ans += 1
  if ans == 2:
    ans_1 += 1
    break

if ans == 0:
  print("Yes")
else:
  print("No")
