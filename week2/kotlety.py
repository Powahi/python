k = int(input())
m = int(input())
n = int(input())
if k == 1:
    s = k + 1
    a = s * m
    b = a * n
    print(b)
elif k > 1:
    s = k * 2
    a = s * m
    b = a - ((n * 2) * m)
    print(b)
