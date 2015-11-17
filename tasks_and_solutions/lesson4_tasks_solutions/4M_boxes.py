m, n = map(int, input().split())
A, B = set(), set()
 
for i in range(m):
    A.add(int(input()))
for i in range(n):
    B.add(int(input()))

a_and_b = sorted(A.intersection(B))
only_a  = sorted(A.difference(B))
only_b = sorted(B.difference(A))
 
print(len(a_and_b))
print(*a_and_b)
print(len(only_a))
print(*only_a)
print(len(only_b))
print(*only_b)