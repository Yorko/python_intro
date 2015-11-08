# insert three integers separated by commas
a, b, c = [int(i) for i in input().split(',')]

d = max(a, b, c)

print("YES" if a + b + c > 2 * d else "NO")