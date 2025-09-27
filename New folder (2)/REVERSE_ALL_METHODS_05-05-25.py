s='Hello world'
print(s[::-1])

s='hello world'
rev=''
for ind in range(len(s)-1,-1,-1):
    rev+=s[ind]
print(rev)

s='hello world'
rev=''
for ind in range(-1,len(s)-1,-1):
    rev+=s[ind]
print(rev)

s='hello world'
rev=''
for ch in s:
    rev=ch+rev
print(rev)

s='malayala'
for ind in range(0,len(s)//2):
    if s[ind]!=s[-ind-1]:
        print('Not Palindrome')
        break
else:
    print('Palindrome')

s='a@bCd32$Da'
count=0
ind=0
while ind!=len(s):
    if 'A'<=s[ind]<='Z':
        count+=1
    ind+=1
print(count)
