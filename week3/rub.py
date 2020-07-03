import math
n = float(input())
y = n - math.floor(n)
r = int(n)
c = round(y, 2) * 100
print(int(r), int(c))
