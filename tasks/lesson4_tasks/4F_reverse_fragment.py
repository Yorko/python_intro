s = input()
f, l= s.index('h') + 1, s.rindex('h')
print(s[:f] + s[f:l][::-1] + s[l:])