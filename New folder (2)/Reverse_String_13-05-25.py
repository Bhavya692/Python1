'''#Using Built-in-Methods
s='hi hello good bye'
result=s.split()
rev=[]
for ele in result:
    rev.append(ele[::-1])
print(' '.join(rev))'''

'''#Without Using Built-in-Methods
s='hi hello good bye'
L=[]
word=''
revL=[]
for ch in s:
    if ch==' ':
        L=L+[word]
        word=''
    else:
        word+=ch
L=L+[word]
print(L)
for ele in L:
    rev=''
    for ch in ele:
        rev=ch+rev
    revL=revL+[rev]
print(revL)
rev=''
ind=0
while ind!=len(revL):
    if ind==len(revL)-1:
        rev+=revL[ind]
    else:
        rev+=revL[ind]+' '
    ind+=1
print(rev)'''

s=''
b=3
for val in range(ord('a'),ord('z')+1):
    s+=chr(val)
print(s)
for ind in range(0,len(s),b):
    print(s[ind:ind+b])
        


