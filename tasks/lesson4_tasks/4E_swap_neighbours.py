a_list = [int(x) for x in input().split(sep=' ')]
for i in range(0, len(a_list) - 1, 2):
    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
print(*a_list)