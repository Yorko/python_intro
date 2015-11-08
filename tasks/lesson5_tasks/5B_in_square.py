x, y = float(input()), float(input())

def IsPointInSquare(x, y):
    return y >= abs(x) - 1 and y <= 1 - abs(x)

print("YES" if IsPointInSquare(x, y) else "NO")