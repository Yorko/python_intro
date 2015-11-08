a = float(input())
b = float(input())
 
if a == 0 and b == 0:
    print('INF')
elif a != 0 and b % a == 0:
    print(int(-b / a))
else:
    print('NO')