n = int(input())

s = input().strip() # in a form "3 4 5 6 2"

def reverse(s, a, b):
    if a == b:
        return s[a]
    elif a > b:
        return ''
    else:
        left_number = s[a:b+1][:s[a:b+1].index(" ")]
        right_number = s[a:b+1][s[a:b+1].rindex(" ") + 1:]
        return right_number + ' ' + reverse(s, a + len(left_number) + 1, b - len(right_number) -1) + ' ' + left_number

print(reverse(s, 0, len(s) - 1))