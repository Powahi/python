a, b, c = int(input()), int(input()), int(input())
if a == b and b == c:
    print(3)
elif a == b and b != c:
    print(2)
elif a == c and c != b:
    print(2)
elif b == c and a != c:
    print(2)
elif a != b and b != c and a != c:
    print(0)
