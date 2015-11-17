nums = map(int, input().split())

s = set()

for n in nums:
    if n in s:
        print('YES')
    else:
        s.add(n)
        print('NO')