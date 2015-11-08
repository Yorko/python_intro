from math import sqrt, ceil

n = int(input())

def isPrime(n):
    if n == 2:
        return True
    else:
        for i in range(2, ceil(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

print("YES" if isPrime(n) else "NO")