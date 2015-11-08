n, k = int(input()), int(input())

def C(n, k):
    if n == k:
        return 1
    elif k == 0:
        return 1
    else: 
        return C(n-1, k-1) + C(n-1, k)
    
print(C(n, k))