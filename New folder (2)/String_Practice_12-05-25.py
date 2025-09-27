'''s='abcde'
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        print(s[si:ei])'''
'''s='abcde'
si=0
while si!=len(s):
    ei=si+1
    while ei!=len(s)+1:
        print(s[si:ei])
        ei+=1
    si+=1'''

'''s='abcba'
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        if s[si:ei]==s[si:ei][::-1]:
            print(s[si:ei])'''

'''
#Using Slicing
s='abcba'
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word=s[si:ei]
        if word==word[::-1]:
            print(word)'''
'''#Using Indexing
s='abcba'
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word=''
        for ind in range(si,ei):
            word+=s[ind]
        print(word)'''
'''s='abcba'
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word=''
        for ind in range(si,ei):
            word+=s[ind]
        #print(word)
        rev=''
        for ind in range(-1,-len(word)-1,-1):
            rev+=word[ind]
        #print(rev)
        if word==rev:
            print(word)'''
'''#Using Built-in Methods
s='hi hello good bye'
print(' '.join(s.split()[::-1]))'''

s='hi hello good bye'
word=''
L=[]
result=''
for ch in s:
    if ch==' ':
        L=L+[word]
        word=' '
    else:
        word+=ch
L=L+[word]
#print(L)
rev=[]
for word in L:
    rev=[word]+rev
#print(rev)
ind=0
while ind!=len(rev):
    if ind==len(rev)-1:
        result=result+rev[ind]
    else:
        result+=rev[ind]+' '
    ind+=1
print(result)
