numberbob = 0
for i in range(0,len(s)):
    if s[i:i+3] == 'bob':
        numberbob +=1
print 'Number of times bob occurs is:', numberbob
