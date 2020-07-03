s = str(input())
a = s.find('h')
b = s.rfind('h')
a = a + 1
print(s[0:b] + s[a:])
