n = int(input())
sn = 0
b = 0
while n != 0:
    sn = sn + n
    if n % 2 == 0:
        b = b + 1
    n = int(input())
print(b)
