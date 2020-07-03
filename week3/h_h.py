s = str(input())
a = s.find('h')
b = s.rfind('h')
b = b + 1
print(s[0:a] + s[b:])
