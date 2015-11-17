# insert four integers separated by commas
row1, col1, row2, col2 = [int(i) for i in input().split(',')]

horse_steps = [(-2, 1), (-1, 2), (1, 2), (2, 1),
               (2, -1), (1, -2), (-1, -2), (-2, -1)]

print("YES" if (row2 - row1, col2 - col1) in horse_steps else "NO")