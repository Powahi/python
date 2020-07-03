s = str(input())
a = s.find('f')
b = s.rfind('f')
if a >= 0 and a == b:
    print(-1)
elif b != a:
    ss = (s[a:])
    print(len(s) - len(ss) + 1)
else:
    print(-2)
