rc = list(map(int, input().split()))
ans = 0
 
for a in range(1, 31):
    for b in range(1, 31):
        for d in range(1, 31):
            for e in range(1, 31):
                c = rc[0] - a - b
                f = rc[1] - d - e
                g = rc[3] - a - d
                h = rc[4] - b - e
                ir = rc[2] - g - h
                ic = rc[5] - c - f
                if min(c, f, g, h, ir, ic) > 0 and ir == ic:
                    ans += 1
print(ans)