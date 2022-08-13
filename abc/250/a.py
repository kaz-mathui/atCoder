h, w = map(int, input().split())
r, c = map(int, input().split())
cnt = 4
 
if (c == 1) :
  cnt = cnt -1
if (c == w) :
  cnt = cnt -1
if (r == 1) :
  cnt = cnt -1
if (r == h) :
  cnt = cnt -1
 
 
print(cnt)
