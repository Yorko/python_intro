n = int(input())
m = int(input())
k = int(input())
 
if k <= n * m and (k % n == 0 or k % m == 0):
    print('YES')
else:
    print('NO')