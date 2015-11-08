a_list = [int(x) for x in input().split()]
print(*a_list[::2], sep=' ')