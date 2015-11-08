s = input()
print(s[:s.index('h')] + s[s.rindex('h') + 1:])