a, b, c = [int(s) for s in input().split(',')]
 
if b < a: 
    a, b = b, a
if c < b: 
    c, b = b, c
if b < a: 
    a, b = b, a
 
print(" ".join([a, b, c]))