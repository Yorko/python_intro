def vary_word_form(n):
    r = n % 10
    if r == 1 and (n not in range(11, 15)):
        return 'korova'
    elif n not in range(11, 15) and r in (2, 3, 4):
        return 'korovy'
    else:
        return 'korov'
 
 
n = int(input())
print(str(n) + ' ' + vary_word_form(n))