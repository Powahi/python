def ReduceFraction():
    import math
    n = int(input())
    m = int(input())
    k = math.gcd(n, m)
    print(n // k, m // k)


ReduceFraction()
