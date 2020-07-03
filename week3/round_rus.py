import math
n = float(input())
y = float(n) - int(n)
if y < 0.5:
    print(int(n))
elif y >= 0.5:
    print(math.ceil(n))
