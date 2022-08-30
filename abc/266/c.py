import math
 
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())
 
 
def getxy_RD(x, y, X, Y):
    _x, _y = (X-x), (Y-y)
    r = math.sqrt(_x**2+_y**2)
    rad = math.atan2(_y, _x)
    degree = math.degrees(rad)
    if degree < 0:
        degree += 360
    return degree
 
 
anslist = []
# 角Aのなす角
anslist.append((getxy_RD(Ax, Ay, Dx, Dy)-getxy_RD(Ax, Ay, Bx, By)) % 360)
 
# 角Bのなす角
anslist.append((getxy_RD(Bx, By, Ax, Ay) - getxy_RD(Bx, By, Cx, Cy)) % 360)
 
# 角Cのなす角
anslist.append((getxy_RD(Cx, Cy, Bx, By)-getxy_RD(Cx, Cy, Dx, Dy)) % 360)
 
# 角Dのなす角
anslist.append((getxy_RD(Dx, Dy, Cx, Cy) - getxy_RD(Dx, Dy, Ax, Ay)) % 360)
 
for i in anslist:
    if i > 180:
        print("No")
        exit()
 
print("Yes")
