def IsPointInSquare(x, y):
    a = (x + y)
    return - 1 <= a <= 1


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
