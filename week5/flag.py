n = int(input())
s1 = "+___ "
s2 = "|"
s23 = " / "
s3 = "|__\ "
s4 = "|    "
print(s1 * n)
for i in range(n):
    print(s2, i + 1, s23, sep='', end='')
print()
print(s3 * n)
print(s4 * n)
