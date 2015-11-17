# insert four integers separated by commas
x1, y1, x2, y2 = [int(i) for i in input().split(',')]

print("YES" if (x1 == x2 or y1 == y2) else "NO")