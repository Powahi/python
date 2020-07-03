s = str(input())
a = s.find('f')
b = s.rfind('f')
if a >= 0 and b == a:
    print(a)
elif b >= -1 and a >= 0 and a != b:
    print(a, b)
else:
    print("")
