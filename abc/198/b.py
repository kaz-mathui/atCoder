x = input()
ans = ""
for e in x:
    if e == ".":
        break
    else:
        ans += e
print(int(ans))
