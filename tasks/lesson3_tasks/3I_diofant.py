# insert four integers separated by commas
a, b, c, d = [int(i) for i in input().split(',')]

for i in range(0,1001):
    if a*(i ** 3) + b*(i ** 2) + c*i + d == 0:
        print(i)
