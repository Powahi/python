a = int(input())
b = int(input())
c = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
s1 = a + b + c
s2 = a2 + b2 + c2
if s1 == s2:
    print("Boxes are equal")
elif s1 < s2:
    print("The first box is smaller than the second one")
elif s1 > s2:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
