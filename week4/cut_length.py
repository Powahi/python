def distance(x11, y11, x22, y22):
    a1 = max(x11, y11)
    a2 = min(x11, y11)
    b1 = max(x22, y22)
    b2 = min(x22, y22)
    print(a1 - a2, b1 - b2)


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
distance(x1, y1, x2, y2)
