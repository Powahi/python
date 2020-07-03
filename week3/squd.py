a = float(input())
b = float(input())
c = float(input())
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print()
elif discriminant == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    if x1 > x2:
        print(x2, x1)

    else:
        print(x1, x2)
