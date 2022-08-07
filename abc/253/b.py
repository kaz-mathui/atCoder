def calc_dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
 
H,W = map(int,input().split())
 
grid = [input() for _ in range(H)]
 
find=[]
for h in range(H):
    for w in range(W):
        if grid[h][w] == "o":
            find.append((h,w))
 
 
print(calc_dist(find[0],find[1]))
