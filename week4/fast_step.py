def fast():
    a = float(input())
    n = int(input())
    if n % 2 != 0:
        an = a * a ** (n - 1)
        print(an)
    elif n % 2 == 0:
        if a % 2 == 0:
            an = (a * 2) ** (n / 2)
            print(an)
        else:
            an = a ** n
            print(an)


fast()
