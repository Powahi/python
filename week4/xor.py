def xor(x, y):
    if x == 1 and y == 1:
        return False
    elif x == 0 and y == 1:
        return True
    elif x == 1 and y == 0:
        return True
    elif x == 0 and y == 0:
        return False


x = int(input())
y = int(input())
if xor(x, y):
    print(1)
else:
    print(0)
