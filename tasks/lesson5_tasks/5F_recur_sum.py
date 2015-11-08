a, b = int(input()), int(input())

def sum(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        a += 1
        b -= 1
        return sum(a, b)
    
print(sum(a,b))