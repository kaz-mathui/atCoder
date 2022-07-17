import math

a,b,d = map(int,input().split())

cos = math.cos(math.radians(d))
sin = math.sin(math.radians(d))
rot_x = (a * cos) - (b * sin)
rot_y = (a * sin) + (b * cos)
print(rot_x,rot_y)
# if 0 < d <= 90:
#     print(-b* math.sin(math.radians(d)) + a* math.cos(math.radians(d)),a* math.sin(math.radians(d)) +b * math.cos(math.radians(d)))
# elif 90 < d <= 180:
#     print(2)
#     print(b* math.sin(math.radians(d)) + a* math.cos(math.radians(d)),a* math.sin(math.radians(d)) +b * math.cos(math.radians(d)))
# elif 180 < d <= 270:
#     print(3)
#     print(-b* math.sin(math.radians(d)) + a* math.cos(math.radians(d)),-a* math.sin(math.radians(d)) -b * math.cos(math.radians(d)))
# else:
#     print(a* math.cos(math.radians(d)) - b* math.sin(math.radians(d)),a* math.sin(math.radians(d)) +b * math.cos(math.radians(d)))