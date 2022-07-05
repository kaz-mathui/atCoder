
k = int(input())
if 0 <= k < 10:
    print("21:0" + str(k))
if 10 <= k < 60:
    print("21:" + str(k))
if 60 <= k < 70:
    print("22:0" + str(k-60))
if k >= 70:
    print("22:" + str(k-60))
