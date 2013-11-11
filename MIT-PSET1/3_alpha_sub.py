n_s = s[0]
res = ''
for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        n_s += s[i]
        if len(res) < len(n_s):
            res = n_s
            n_s = s[i]
    else:
        n_s = s[i]
print 'Longest substring in alphabetical order is:', res