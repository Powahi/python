n = int(input())
if n == 1:
    for i in reversed(range(10)):
        if i % 2 != 0:
            print(i, end=' ')
elif n == 2:
    for i in reversed(range(100)):
        if i % 2 != 0:
            print(i, end=' ')
            if i < 12:
                break
elif n == 3:
    for i in reversed(range(1000)):
        if i % 2 != 0:
            print(i, end=' ')
            if i < 102:
                break
elif n == 4:
    for i in reversed(range(10000)):
        if i % 2 != 0:
            print(i, end=' ')
            if i < 1002:
                break
