# insert three integers separated by commas
a, b, c = [int(i) for i in input().split(',')]

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)