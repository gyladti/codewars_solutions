from math import *

def triangle_type(a, b, c):
    cos_a = (a**2 + b**2 - c**2) / (2 * a * b)
    a1 = round(degrees(acos(cos_a)))
    cos_b = (b**2 + c**2 - a**2) / (2 * b * c)
    b1 = round(degrees(acos(cos_b)))
    cos_c = (a**2 + c**2 - b**2) / (2 * a * c)
    c1 = round(degrees(acos(cos_c)))
    print(a1, b1, c1)
    if a1 == 90 or b1 == 90 or c1 == 90:
        return 2
    elif a1 >= 180 or b1 >= 180 or c1 >=180:
        return 0
    elif a1 > 90 or b1 > 90 or c1 > 90:
        return 3
    else:
        return 1


print(triangle_type(2,4,6))
