num_students = int(input())

everybody, at_least_one = set(), set()

for i in range(num_students):
    langs = set()
    for j in range(int(input())):
        langs.add(input())
 
    at_least_one = at_least_one.union(langs)
    if i == 0:
        everybody = everybody.union(langs)
    else:
        everybody = everybody.intersection(langs)
 
print(len(everybody))
print(*everybody, sep='\n')
print(len(at_least_one))
print(*at_least_one, sep='\n')