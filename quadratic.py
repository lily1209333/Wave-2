import math
a = int(input("input a number for variable 'a': "))
b = int(input("input a number for variable 'b': "))
c = int(input("input a number for variable 'c': "))
dis = (b**2) - (4 * a * c)
if dis < 0:
    print("no real roots")
elif dis > 0:
    print("2 real roots")
    root1 = (-b + math.sqrt(dis))/2 * a
    root2 = (-b - math.sqrt(dis))/2 * a
    print(round(root1, 3), "and", round(root2, 3))
elif dis == 0:
    print("1 real root")
    root = (-b + math.sqrt(dis))/2 * a
    print(round(root, 3))
