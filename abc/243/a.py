
v, a, b, c = map(int, input().split())

while v >= 0:
    v = v-a
    if v < 0:
        print("F")
        break
    v = v-b
    if v < 0:
        print("M")
        break
    v = v-c
    if v < 0:
        print("T")
        break
