def factorial(n):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

n = int(input())
k = int(input())
print(int(factorial(n)/factorial(k)/factorial(n-k)))