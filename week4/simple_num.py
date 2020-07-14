def IsPrime(n):
    i = 1
    while i <= n:
        i = i + 1
        if n % i == 0:
            if i == n:
                print("YES")
                break
            else:
                print("NO")
                break


a = int(input())
IsPrime(a)
