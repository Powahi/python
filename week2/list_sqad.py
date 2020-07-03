a = int(input())
i = 1
while i <= a:
    x = i * i
    i = i + 1
    if x > a:
        break
    print(x)
