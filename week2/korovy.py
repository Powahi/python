k = int(input())
if k >= 5 and k <= 20 or k % 10 == 0 or k % 10 == 5 or k % 10 == 6 or k % 10 == 7 or k % 10 == 8 or k % 10 == 9:
    print(k, "korov")
elif k % 10 == 1:
    print(k, "korova")
elif k >= 2 and k <= 4 or k % 10 == 2 or k % 10 == 3 or k % 10 == 4:
    print(k, "korovy")
