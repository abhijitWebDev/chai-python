import math
def areaCir(r):
    area= math.pi * r * r
    circumference = math.pi * 2 * r
    return area, circumference

a, c = areaCir(20)

print(round(a, 2))
print(round(c,2))
