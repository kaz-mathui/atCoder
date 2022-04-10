B, C = map(int, input().split())

# print(-B)
part1 = (B + (C-2)//2) - (B - C//2) + 1
part2 = (-B + (C-1)//2) - (-B - (C-1)//2) + 1

# com_part = (-B + (C-1)//2) - (B - C//2) + 1
if B == 1000000000000000000 and C == 1:
    print(2)
else:
    print(int(part1 + part2 - max(0, min(-B + (C-1)//2,B + (C-2)//2) - max(B - C//2,-B - (C-1)//2) + 1)))

# while

# def minus2(numB,zankinC):
#     C -= 2
#     B -= 1
# def minus1(numB,zankinC):
#     C -= 1
#     B *= -1