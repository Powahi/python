n = int(input())
i = 0
while n != 0:
    s = 1 / (n ** 2)
    i = i + s
    n = n - 1
print(i)
