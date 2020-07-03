p = int(input())
r = int(input())
c = int(input())
k = int(input())
i = k
sum1 = 100 * r + c
sum2 = 0
sum3 = 0
while i > 0:
    sum2 = int(sum1 * (100 + p) / 100)
    sum3 += sum2
    i -= 1
#print(sum3 // 100, sum3 % 100)
#print(sum2)
print(sum3)