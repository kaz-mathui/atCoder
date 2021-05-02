from collections import deque

t = deque()
s = input()
tbool = False
for i in range(len(s)):
    if not t:
        if s[i] == "R":
            continue
        else:
            t.append(s[i])
    else:
        if s[i] == "R":
            if tbool:
                tbool = False
            else:
                tbool = True
        else:
            if tbool:
                prev = t.popleft()
                if prev == s[i]:
                    continue
                else:
                    t.appendleft(prev)
                    t.appendleft(s[i])
            else:
                prev = t.pop()
                if prev == s[i]:
                    continue
                else:
                    t.append(prev)
                    t.append(s[i])
    
if tbool:
    t.reverse()


print("".join(t))
