list1 = map(int, input().split())
list2 = map(int, input().split())

print(len(set(list1).intersection(set(list2))))