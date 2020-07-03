p = int(input())
r = int(input())
c = int(input())
sum1 = 100 * r + c
sum2 = int(sum1 * (100 + p) / 100)
print(sum2 // 100, sum2 % 100)
